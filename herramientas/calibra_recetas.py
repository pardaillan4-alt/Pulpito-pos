#!/usr/bin/env python3
"""Calibración de recetas con conteos físicos (Púlpito POS).

Compara, para cada insumo contado dos veces, el consumo real
(contado al inicio + compras - mermas - contado al final) contra lo que
descuentan las recetas por lo vendido en ese periodo (con la misma lógica
del POS, ejecutando index.html en un navegador sin pantalla).
Con eso propone el factor de ajuste por insumo (config/ajrec), moviéndolo
solo la mitad del camino hacia el dato real cada vez.

Uso:
  PULPITO_CORREO=... PULPITO_CLAVE=... python3 calibra_recetas.py [--aplicar] [--dias 21]

Sin --aplicar solo imprime el resultado en JSON (no escribe nada).
Con --aplicar escribe config/ajrec (requiere que la regla de Firestore
permita a ese usuario escribir ese documento).
Lecturas aproximadas: recetas, insumos y config completas (~300) + líneas,
compras y mermas solo del periodo entre conteos (~150 por día).
"""
import asyncio, json, os, sys, time, urllib.request, pathlib

KEY = "AIzaSyC4DpdS49DUpKBT2agRdLaS-na9vBh0DGY"
PROJ = "pulpito-pos"
BASE = f"https://firestore.googleapis.com/v1/projects/{PROJ}/databases/(default)/documents"
HTML = pathlib.Path(__file__).resolve().parent.parent / "index.html"
PASO = 0.5           # fracción del camino hacia el dato real que se mueve cada vez
MIN_F, MAX_F = 0.5, 1.6
TOL = 0.08           # diferencias menores a 8% no se ajustan
UNID = ("kg", "l", "lt", "litro", "litros")   # solo insumos que se pesan/miden: en piezas u órdenes la diferencia es merma o captura, no receta
MIN_TEO = 1.0        # consumo mínimo según recetas en el periodo para ajustar
RANGO_OK = (0.4, 2.5)  # fuera de esto se marca para revisar, no se ajusta
AJ0_AT = 1795543200000  # 24/11/2026 12:00 (CDMX): valores iniciales de AJ0 en index.html


def post(url, data, tok=None):
    h = {"Content-Type": "application/json"}
    if tok: h["Authorization"] = "Bearer " + tok
    return json.load(urllib.request.urlopen(urllib.request.Request(url, json.dumps(data).encode(), h)))


def login():
    r = post(f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={KEY}",
             {"email": os.environ["PULPITO_CORREO"], "password": os.environ["PULPITO_CLAVE"], "returnSecureToken": True})
    return r["idToken"]


def val(v):
    k, x = next(iter(v.items()))
    if k == "mapValue": return {a: val(b) for a, b in x.get("fields", {}).items()}
    if k == "arrayValue": return [val(b) for b in x.get("values", [])]
    if k == "integerValue": return int(x)
    if k == "nullValue": return None
    return x


def enc(v):
    if isinstance(v, bool): return {"booleanValue": v}
    if isinstance(v, int): return {"integerValue": str(v)}
    if isinstance(v, float): return {"doubleValue": v}
    if isinstance(v, str): return {"stringValue": v}
    if isinstance(v, dict): return {"mapValue": {"fields": {a: enc(b) for a, b in v.items()}}}
    if isinstance(v, list): return {"arrayValue": {"values": [enc(b) for b in v]}}
    return {"nullValue": None}


def todo(tok, col):
    out, pt = [], ""
    while True:
        u = f"{BASE}/{col}?pageSize=300" + (f"&pageToken={pt}" if pt else "")
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"Authorization": "Bearer " + tok})))
        for doc in d.get("documents", []):
            out.append({"id": doc["name"].split("/")[-1], "d": {a: val(b) for a, b in doc.get("fields", {}).items()}})
        pt = d.get("nextPageToken")
        if not pt: return out


def rango(tok, col, a, b):
    f = [{"fieldFilter": {"field": {"fieldPath": "at"}, "op": op, "value": {"integerValue": str(int(t))}}}
         for op, t in (("GREATER_THAN_OR_EQUAL", a), ("LESS_THAN", b))]
    q = {"structuredQuery": {"from": [{"collectionId": col}], "where": {"compositeFilter": {"op": "AND", "filters": f}}}}
    res = post(f"{BASE}:runQuery", q, tok)
    return [{**{k: val(v) for k, v in r["document"].get("fields", {}).items()}} for r in res if r.get("document")]


def handler(src, col):
    tag = f'c.collection("{col}").onSnapshot('
    j = src.index(tag) + len(tag); d = 0; k = j
    while True:
        ch = src[k]
        if ch in "({[": d += 1
        elif ch in ")}]":
            if d == 0: break
            d -= 1
        k += 1
    return src[j:k]


JS = """(a)=>{const D=a.D,snap=x=>({docs:x.map(y=>({id:y.id,data:()=>JSON.parse(JSON.stringify(y.d))}))});window.catFix=()=>{};
(eval(a.cfg))(snap(D.cfg));(eval(a.ins))(snap(D.ins));(eval(a.rec))(snap(D.rec));
const out=[];D.L.forEach(l=>{if(l.anul)return;const r=lineRec(l);if(!r)return;let ex;try{ex=ajR(expP(recDe(r.it,r.vi,r.ms)))}catch(e){return}ex.forEach(([i,q])=>out.push([i,q*r.q,l.at]))});
return {out,aj:AJ}}"""


async def teorico(D):
    from playwright.async_api import async_playwright
    src = HTML.read_text(encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
        await pg.goto(HTML.as_uri()); await pg.wait_for_timeout(1200)
        r = await pg.evaluate(JS, {"D": D, "cfg": handler(src, "config"), "ins": handler(src, "insumos"), "rec": handler(src, "recetas")})
        await b.close(); return r


def main():
    aplicar = "--aplicar" in sys.argv
    dias = int(sys.argv[sys.argv.index("--dias") + 1]) if "--dias" in sys.argv else 21
    tok = login(); ahora = time.time() * 1000; a0 = ahora - dias * 864e5
    cn = sorted(rango(tok, "conteos", a0, ahora + 1), key=lambda c: c["at"])
    # para cada insumo, sus dos conteos más recientes dentro del periodo
    pares = {}
    for c in cn:
        for r in c.get("rows", []):
            pares.setdefault(r["n"], []).append((c["at"], r))
    cfg = todo(tok, "config")
    ult = next((int(c["d"].get("at") or 0) for c in cfg if c["id"] == "ajrec"), 0) or AJ0_AT
    # solo pares cuyo conteo final es posterior a la última calibración (información nueva)
    pares = {n: v[-2:] for n, v in pares.items() if len(v) >= 2 and v[-1][0] > ult}
    if not pares:
        print(json.dumps({"ok": True, "mensaje": "No hay insumos con dos conteos en el periodo", "ajustes": []}, ensure_ascii=False)); return
    ini = min(v[0][0] for v in pares.values()); fin = max(v[1][0] for v in pares.values())
    D = {"cfg": cfg, "ins": todo(tok, "insumos"), "rec": todo(tok, "recetas"),
         "L": rango(tok, "lineas", ini, fin + 1)}
    Cp = rango(tok, "compras", ini, fin + 1); Me = rango(tok, "mermas", ini, fin + 1)
    T = asyncio.run(teorico(D)); aj = T["aj"]
    res = []; nuevo = {k: v for k, v in aj.items()}
    for n, ((a, r0), (b, r1)) in pares.items():
        comp = sum(float(x["q"]) for x in Cp if x["n"] == n and a <= x["at"] < b)
        mer = sum(float(x["q"]) for x in Me if x["n"] == n and a <= x["at"] < b)
        teo = sum(q for i, q, t in T["out"] if i == n and a <= t < b)
        real = float(r0["fis"]) + comp - mer - float(r1["fis"])
        f0 = float(aj.get(n, 1) or 1)
        fila = {"insumo": n, "u": r1.get("u", ""), "desde": a, "hasta": b, "compras": round(comp, 3), "mermas": round(mer, 3),
                "recetas": round(teo, 3), "real": round(real, 3), "factor_actual": f0}
        u = str(r1.get("u", "")).lower().strip()
        if teo <= 0 or real <= 0:
            fila["nota"] = "sin ventas con receta o consumo real no positivo; no se ajusta"
        else:
            ratio = real / teo; fila["real_entre_recetas"] = round(ratio, 3)
            if u not in UNID:
                fila["nota"] = "se cuenta por pieza/orden: la diferencia es merma, cortesía o compra sin capturar, no receta"
            elif teo < MIN_TEO:
                fila["nota"] = "poco consumo en el periodo; se espera más información"
            elif not (RANGO_OK[0] <= ratio <= RANGO_OK[1]):
                fila["nota"] = "diferencia demasiado grande para ser receta: revisar compras, unidad o conteo"
            elif abs(ratio - 1) >= TOL:
                f1 = min(MAX_F, max(MIN_F, f0 * (1 + PASO * (ratio - 1))))
                fila["factor_nuevo"] = round(f1, 3); nuevo[n] = round(f1, 3)
        res.append(fila)
    salida = {"ok": True, "periodo": [ini, fin], "ajustes": res, "factores": nuevo}
    if aplicar:
        nota = "calibrado " + time.strftime("%d/%m/%Y")
        body = {"fields": {"f": enc({k: float(v) for k, v in nuevo.items()}), "nota": enc(nota), "at": enc(int(ahora))}}
        req = urllib.request.Request(f"{BASE}/config/ajrec", json.dumps(body).encode(),
                                     {"Content-Type": "application/json", "Authorization": "Bearer " + tok}, method="PATCH")
        urllib.request.urlopen(req); salida["aplicado"] = nota
    print(json.dumps(salida, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
