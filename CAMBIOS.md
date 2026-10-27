# Registro de cambios

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
