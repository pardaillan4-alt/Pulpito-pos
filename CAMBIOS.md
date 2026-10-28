# Registro de cambios

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
