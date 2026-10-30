# Registro de cambios

## 2026-10-29 (v79) — Confirmar al quitar un gasto en el corte de caja
Desde: conversación de desarrollo de la app.
- Al quitar un gasto/ingreso del corte de caja (`delMov`) ahora se pregunta "¿Seguro que quieres quitar…?" mostrando concepto e importe; si se cancela no se borra nada. Después sigue la autorización normal.

## 2026-10-29 (v78) — Olla para café de olla (4 tazas)
Desde: conversación de desarrollo de la app.
- Nueva preparación **※ Olla café de olla** (rinde 4 tazas: café, piloncillo, canela; cantidades estimadas).
- Café > Café de olla ahora descuenta 1 taza de la olla en lugar del café suelto. "Agua para té" no cambia.

## 2026-10-29 (v77) — Aguas frescas ligadas a las tandas
Desde: conversación de desarrollo de la app.
- Agua fresca del menú: al elegir sabor (Jamaica, Horchata, Piña, Tamarindo) descuenta y costea la **tanda** correspondiente: Vaso 0.4 lt, Jarra 1 lt, Jarra 2 lt. Botella de agua no usa tanda.
- Sustituye al "Jarabe de sabor" genérico cuando hay sabor elegido (no se cuenta doble). Si no hay sabor, queda como antes.
- Constantes `AGUAT` / `AGUAT_L` en `recDe`.

## 2026-10-29 (v76) — Tandas de aguas frescas (4 litros)
Desde: conversación de desarrollo de la app.
- Nuevas preparaciones con costo: **※ Tanda agua de jamaica**, **de horchata**, **de piña** y **de tamarindo**; cada una rinde 4 litros (cantidades estimadas, ajustables).
- No se ligaron automáticamente a las aguas frescas del menú; solo son preparaciones con costo por litro.

## 2026-10-29 (v75) — Porción de camarones y Porción de ostión
Desde: conversación de desarrollo de la app.
- Renombrada **※ Porción camarones** → **※ Porción de camarones** (se migra solo en los dispositivos).
- Nueva **※ Porción de ostión** (0.1 kg estimado), ligada a la opción Ostiones de la Cerveza.

## 2026-10-29 (v74) — Preparaciones: Michelada, Porción camarones, Porción de clamato
Desde: conversación de desarrollo de la app.
- Nuevas preparaciones con costo: **※ Michelada**, **※ Porción camarones** y **※ Porción de clamato** (cantidades estimadas, ajustables en Recetas y costos).
- Ligadas solo al producto **Cerveza**: al elegir la opción Michelada, Camarón o Clamato se descuentan y se suman al costo. No afectan a otros productos con "Clamato" o "Camarón" (jugos, caldos, cócteles).
- `SALSA0` admite campo `n` (producto) y `salsaR` lo respeta; `migSalsas` agrega las nuevas reglas sin tocar las existentes.

## 2026-10-29 — conversación del desarrollo de la app (v73)
- Preparación nueva con costo: ※ Tanda de flan (rinde 6 pz de flan de postre), ligada a Postres → Flan napolitano (1 pz por venta). El huevo (0.04) que estaba directo en esa receta pasó a la tanda.

## 2026-10-29 — conversación del desarrollo de la app (v72)
- Preparaciones nuevas con costo: ※ Porción carne chile en nogada y ※ Salsa nogada, ligadas al estilo «En nogada» de Chiles (`SALSA0`). La carne molida (0.084) que estaba directo en la receta de Chiles pasó a la porción para no contarla doble.

## 2026-10-28 — conversación del desarrollo de la app (v71)
- Recetas y costos, agregar ingrediente: la lista de sugerencias vuelve a incluir las preparaciones/salsas base (※) y el buscador `insFind` las encuentra sin escribir el símbolo ※ (p. ej. «salsa vera» → ※ Salsa Veracruz).

## 2026-10-28 — conversación del desarrollo de la app (v70)
- Salsas por estilo (`salsaR`): no se agrega la salsa automática si la receta ya trae un ingrediente con el mismo nombre que la preparación (con o sin ※), para no contarla dos veces.

## 2026-10-28 — conversación del desarrollo de la app (v69)
- Preparaciones nuevas con costo: ※ Salsa enamorado y ※ Salsa en su tinta (esta envuelve a ※ Tinta de pulpo). Estilos «Enamorado» y «En su tinta» ligados en `SALSA0`; `migSalsas` actualiza «En su tinta» de ※ Tinta de pulpo a ※ Salsa en su tinta.

## 2026-10-28 — conversación del desarrollo de la app (v68)
- Preparaciones nuevas con costo: ※ Salsa crema chipotle, ※ Salsa cucaracha, ※ Porción coco y ※ Porción ranchero (las dos últimas son porciones, no salsas). Ligadas por estilo en `SALSA0` («Crema chipotle», «Cucaracha», «Coco», «Ranchero»); «Ranchero» pasa de ※ Salsa casera a ※ Porción ranchero (`migSalsas`).

## 2026-10-28 — conversación del desarrollo de la app (v67)
- Preparaciones nuevas con costo: ※ Salsa mantequilla, ※ Salsa ajillo y ※ Salsa enchilada (receta base editable). Se ligan por estilo en `SALSA0`: «Mantequilla», «Ajillo» y «Enchilad» (antes enchilada usaba la salsa guajillo; `migSalsas` lo actualiza sin tocar otros estilos).

## 2026-10-28 — conversación del desarrollo de la app (v66)
- Empanizado con papas: se limita a Filete y Camarones «a secas» (variante sin nombre); Filete Veracruz/Hawaiano/Relleno/Papillón y Camarones Brochetas/Combinado/Hawaiana/Reyna ya no incluyen papas ni muestran la versión empanizada.

## 2026-10-28 — conversación del desarrollo de la app (v65)
- Recetas y costos: en Camarones y Filete cada tarjeta muestra también «Versión empanizado(s)» con su costo y margen incluyendo las papas a la francesa.

## 2026-10-28 — conversación del desarrollo de la app (v64)
- Camarones y Filete: la opción «Empanizado(s)» incluye automáticamente la guarnición ※ Papas (porción de papas a la francesa) en la receta y en el descuento de inventario (`EMPAP` en `guar`). Nueva opción «Sin papas» para quitarla; «Con papas» no duplica la porción.

## 2026-10-28 — conversación del desarrollo de la app (v63)
- Las compras nuevas guardan quién las registró (campo `por`) y la pestaña Compras muestra el nombre.

## 2026-10-28 — conversación del desarrollo de la app (v62)
- Costo de insumos: ahora es el promedio ponderado de las últimas 5 compras (campo `h` en el insumo, función `cuProm`), no solo el de la última compra. La importación del Excel usa el mismo cálculo (`invAlta`).
- Al borrar una compra (pestaña Compras o control de compras en Reportes) el costo se recalcula con las compras que quedan (`recosto`); si no quedan, vuelve al costo base.

## 2026-10-28 — conversación del desarrollo de la app (v61)
- Compra manual en Inventario: ahora pregunta cómo se pagó (de la caja / aparte / ya registrada) y genera sola el gasto «Pago de compra» (mismo tratamiento que importar compras, así no se cuenta doble en el estado de resultados ni en el control de compras).
- Gasto en caja: campo opcional «¿Es compra de inventario?» (insumo + cantidad) que además suma a las existencias y registra la compra; ese gasto se guarda como «Pago de compra».
- Al registrar compras en inventario ya no se pierden el clasificador ni el nombre del concepto (se conserva el resto de sus datos).

## 2026-10-28 — Salsas por estilo, editables (conversación del curso)
- Nueva tarjeta **🌶️ Salsas por estilo** al inicio de Recetas y costos → Preparaciones: si la variante o una opción del platillo contiene la palabra, se descuenta la porción de la preparación. Se guarda en la nube (`config/salsas`) y se puede editar (palabra, preparación, cantidad, agregar/quitar).
- Valores iniciales: Diabla → salsa diabla 100 ml; Mojo → ajo dorado 30 g; Veracruz → salsa Veracruz 100 g; En su tinta → tinta de pulpo 100 ml; BBQ → salsa BBQ 100 ml; Enchilado/a → salsa guajillo 100 ml; Ranchero → salsa casera 100 g (`SALSA0`, `SALSAS`, `salsaR`).

## 2026-10-28 — Salsas y demás preparaciones con costo; platillos con arroz cocido (conversación del curso)
- Nuevas preparaciones con costo por tanda (cantidades estimadas a partir de los ingredientes del procedimiento, editables): pico de gallo, harina preparada (solo 10 kg de harina, no 20), ajo dorado, salsas diabla, Veracruz, mango, tamarindo, vino tinto, espinaca, BBQ, guajillo y casera, tinta de pulpo, huevo para empanizado y pozole.
- Platillo Arroz usa arroz cocido (solo 385 g, con plátano y a la tumbada 180 g, con mariscos/camarón/pulpo/almeja 280 g). Pollo y res toma la guarnición de arroz (se quita con «Sin arroz»).
- `prepRes`: un ingrediente ya no se puede ligar por parecido a una preparación (evitaba que «Capsu» o «Vino tinto» se ligaran a su propia salsa), y el parecido por 5 letras exige que el insumo empiece igual (evita «Harina de trigo» → «Tortillas de harina»).

## 2026-10-28 — Arroz por tanda, sazonador combinado y agua bendita con costo (conversación del curso)
- **※ Arroz cocido**: tanda de 2 kg de arroz crudo (aceite, ajo, cebolla, sal, Knorr Suiza, agua bendita); rinde ~5.5 kg cocido. La guarnición de arroz ahora es 180 g de arroz cocido (≈ los mismos 65 g crudos de antes).
- **※ Sazonador combinado** (1 lt Maggi + 1 lt salsa inglesa + 1 lt agua, rinde 3 lt) y **※ Agua bendita** (3 kg ajo, laurel, canela, clavo, pimienta, 6 lt agua; rinde ~8.5 lt).
- Raspa y ceviche usan estas preparaciones en lugar de los nombres sueltos «Combinado»/«Agua bendita».
- `prepRes`: el parecido por las primeras 5 letras ya no puede caer en una preparación (evita que «Salsa inglesa» se ligue a la salsa capsu).

## 2026-10-28 — Ceviche preparado con tilapia (conversación del curso)
- Nueva preparación **※ Ceviche preparado** según la receta de la casa (5 filetes de tilapia, cuaresmeño, cebolla morada, pepino, morrones, vinagre, combinado y agua bendita a flanera = 150 ml, sal, orégano, jugo de 20 limones, 10 aceitunas); rinde ~1.4 kg (estimado, editable).
- El ceviche ya no se descuenta como raspa: cóctel de ceviche, tostada de ceviche y campechano con ceviche usan el ceviche preparado (`SWAPP`, `SUBM`).
- Combinado y agua bendita se agregan también a la raspa; como son preparaciones de la casa, solo se ligan a un insumo con el nombre exacto (`PREXACT`) para no confundirse con otros (p. ej. «Aguacate»).

## 2026-10-28 — Marlin preparado y raspa de pescado con costo (conversación del curso)
- Nuevas preparaciones con costo: **※ Marlin preparado** (tanda de 750 g de marlin, rinde ~1.3 kg) y **※ Raspa de pescado** (tanda de 2 kg de raspa, rinde ~2.1 kg), con cantidades estimadas a partir del procedimiento.
- Las recetas que usaban «Marlin» crudo (quesadillas, tostada) ahora usan el marlin preparado; las quesadillas de pescado usan la raspa preparada (`SWAPP`). El cóctel de ceviche sigue con raspa cruda.
- Tostada de marlin: sus 80 g ahora se descuentan como marlin preparado.

## 2026-10-27 — Arreglo: los cambios a las preparaciones no se guardaban (conversación del curso)
- La nube (Firestore) no acepta listas dentro de listas, y las preparaciones se mandaban así; el error se tragaba en silencio y los cambios vivían solo en la memoria del celular hasta recargar o actualizar.
- Ahora se guardan como `{i,q}` (`prepOut`) y se leen de vuelta con `prepIn` (acepta también el formato viejo). Si la nube rechaza el guardado, la app muestra un aviso.

## 2026-10-27 — Base paella y arroz en el pulpo (conversación del curso)
- Nueva preparación **※ Base paella** (olla de 4.5 kg, receta del archivo de costos: aceite, cabeza de lomo, tocineta, muslo de pollo, salchicha, jaiba, arroz precocido, almejas, morrón y 5 tiras de pescado).
- Paella Chica lleva 0.45 kg de base y Paella Grande 0.65 kg (renglón «Arroz preparado» del archivo). Se quitaron arroz y almeja sueltos de la receta porque ya vienen dentro de la base; pacotilla chica 0.02 kg.
- La orden de Pulpo lleva guarnición de arroz automáticamente (se quita con «Sin arroz»). Mapas `PAELLA0` y `ARROZ0`.

## 2026-10-27 — conversación del curso de administración (v53)
- Preparaciones: al editar el costo, el campo para agregar insumo ya tiene el mismo buscador por letras que las recetas (lista de insumos y preparaciones).
- Nueva preparación «※ Ensalada base» (rinde 20 porciones: zanahoria 1 kg, pepino 0.6, jícama 0.6, jitomate 0.6, aguacate 0.4, naranja 0.7 kg; pesos estimados).
- Guarniciones como preparaciones editables: «※ Arroz (guarnición)» 67 g de arroz, «※ Papas (guarnición)» 150 g, «※ Plátano (guarnición)» 80 g.
- Pescaditos: las opciones Con arroz / Con ensalada / Con papas / Con todo / combinaciones / Con plátano descuentan su guarnición (`GUARM`, `guar`).
- Mojarra, camarones, filete y pollo y res incluyen arroz y ensalada base salvo «Sin arroz» / «Sin ensalada»; «Con papas» y «Con plátano» agregan la suya.
- Las recetas muestran una nota 🍽 con las guarniciones y botones para ir a cada preparación.
- Si se quita un ingrediente automático (caldo, capsu, guarnición, tortilla) de una receta, se respeta y ya no vuelve a agregarse.

## 2026-10-27 — conversación del curso de administración (v52)
- Nueva preparación con costo «※ Salsa capsu» (rinde 14 L): ½ bote de capsu, 1 L de Mirinda, piloncillo (~300 g) y canela (~30 g), según el procedimiento guardado.
- Los cócteles agregan solos la salsa capsu si su receta no la trae: chico 0.10 L, grande 0.20 L, bola 0.35 L (camarón, campechano, ceviche, jaiba, pulpo); vuelve a la vida 0.10/0.20 L (`CAPSU0`). Con la opción «Sin capsu» no se descuenta.
- Las preparaciones encuentran el insumo aunque el nombre del inventario sea distinto (p. ej. «Canelon de kilo» para canela).

## 2026-10-27 — conversación del curso de administración (v51)
- Recetas y costos: los ingredientes que son preparación (Caldo base, Sazón) muestran el botón «Ver preparación», que lleva a su ficha en Preparaciones.
- El buscador de recetas también encuentra las preparaciones con costo (por nombre o por ingrediente, p. ej. «jitomate»).

## 2026-10-27 — conversación del curso de administración (v50)
- Preparaciones con costo (sub-recetas): «※ Sazón» (rinde 14 L: jitomate, cebolla, ajo, guajillo, puré de tomate, poro, apio, aceite) y «※ Caldo base» (rinde 15 L: cabeza de camarón, epazote, retazo, sazonador, sal y 3.5 L de sazón), tomadas del Excel de costos. En Recetas y costos → Preparaciones se ve el costo por tanda y por litro, y se pueden editar cantidades, rendimiento e insumos (se guarda en config/prepc).
- Las preparaciones se pueden usar como ingrediente en cualquier receta; al vender, el inventario descuenta sus insumos crudos en proporción (`expP`).
- Caldos, consomés y sopas agregan solos el caldo base si su receta no lo trae: caldo de camarón y de pescado 0.45/0.75 L, combinado 0.4/0.7 L, consomé 0.5 (solo) y 0.45 L, sopas 0.65/0.75 L (`CALDO0`).

## 2026-10-27 — conversación del curso de administración (v49)
- Cóctel campechano: la opción elegida cambia el marisco que se descuenta. Sin opción o «Cam/ost» = camarón + ostión; «Cam/pul» = camarón + pulpo; «Jaiba», «Surimi» y «Ceviche» (raspa) reemplazan al ostión. Si se eligen varias, se reparte la porción entre ellas. Aplica a chico, grande y bola (`SUBM`, `subM`).
- El costo por línea de la ingeniería de menú toma en cuenta esas opciones.

## 2026-10-27 — conversación del desarrollo de la app (v48)
- Recetas y costos: al editar una receta, tocar un insumo carga su cantidad para modificarla directo; el buscador de insumo es un cuadro de texto (escribe una letra y encuentra el más cercano, sin acentos).

## 2026-10-27 — conversación del curso de administración (v47)
- Quesadilla: la variante «Esp/otro» se divide en «Esp/pescado», «Esp/marlin» y «Esp/jaiba» ($32 cada una) para que el inventario descuente el marisco correcto. Receta inicial: 28 g del marisco + 12 g de queso Oaxaca (pendiente de pesar en cocina).
- Toda quesadilla descuenta 1 tortilla de maíz (50 g si el insumo está en kg, 1 pieza si está en piezas), aunque su receta guardada no la tenga.
- Recetas por defecto de la quesadilla realineadas al nuevo orden de variantes.
- Ingeniería de menú: solo usa la variante guardada en la línea si coincide con el texto del ticket (las ventas viejas no se confunden al cambiar variantes).

## 2026-10-27 — conversación del curso de administración (v46)
- Cortesías y consumo interno: al agregar un platillo se puede marcar «🎁 Cortesía / consumo interno» (cortesía a cliente, consumo del personal, uso en cocina). Se cobra en $0, descuenta inventario, pide NIP de administrador y aparece en el reporte.
- Ingeniería de menú: reconoce la variante sin nombre (p. ej. «Camarones» cualquier preparación) y usa la variante guardada en la línea; antes contaba de menos.
- Se agregan `CLAUDE.md` (reglas para no perder cambios entre conversaciones) y este registro.

## 2026-10-25 a 2026-10-27 — conversación del desarrollo de la app (v39 a v45, registrado después)
- Recetas del Excel cargadas (ingredientes y procedimiento por platillo + pestaña «Preparaciones»); buscador en Recetas y en Reporte de costos.
- Préstamos al personal (préstamo / abono / descuento de nómina) con saldos por empleado; no cuentan como gasto.
- Aguacate relleno «Uno y uno»; agotados de agua fresca por sabor; mover mesa a una mesa abierta (suma la cuenta).
- Confirmación al dar de baja merma; pestaña Compras con opción de borrar una compra; gastos fijos con monto (+ Netflix, Internet, Predial).
- Teclado «Siguiente»: la pantalla ya no se redibuja al cambiar de campo (cambio en el manejador de `change` y `draw`).
- Corte de caja: el periodo va desde el último corte (no desde las 00:00) y el fondo inicial es el último conteo físico.

## Antes de esta fecha
Cambios subidos a mano sin registro (corte de caja, pestaña Compras, recetas y costos, gastos fijos, estado de resultados, etc.).
