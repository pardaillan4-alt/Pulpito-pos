# Púlpito POS — reglas para trabajar en este repositorio

Este POS lo modifican **dos conversaciones de Claude** distintas (la del desarrollo de la app y la del curso de administración del restaurante). Para que ninguna borre las mejoras de la otra:

1. **Antes de cambiar cualquier cosa, trae la última versión de GitHub** (`git pull` o volver a descargar `index.html` y `sw.js` del repositorio). Nunca trabajes sobre una copia guardada de una conversación anterior.
2. **Haz los cambios sobre esa versión** y súbelos con un commit que diga claramente qué cambió.
3. **Sube el número de versión en `sw.js`** (`pulpito-vNN`) en cada cambio, para que los celulares tomen la actualización.
4. **Anota el cambio en `CAMBIOS.md`** (fecha, qué se hizo y desde qué conversación).
5. Si no puedes subir a GitHub tú mismo, entrega los archivos completos y pide que se suban **antes** de hacer otro cambio en la otra conversación.

## Funciones que dependen del curso de administración (no quitarlas)
- Estado de resultados en Reportes: el dinero sale solo de lo pagado (gastos de caja); las compras capturadas en inventario solo reparten cada «Pago de compra» entre categorías (`edoRes`). Así nada se cuenta dos veces.
- Categorías obligatorias de gasto en caja (`GCI`, `GCO`, `GPC`) y clasificación automática de gastos viejos (`gcat0`).
- Importar compras: pregunta cómo se pagó (caja / aparte / ya registrado en caja).
- Ingeniería de menú (`ingMenu`, `cLin`) y control de compras capturadas (`ctlC`).
- Cargo de opción por tamaño (`MODP`, `mpx`): campechano con pulpo al precio del cóctel de pulpo.
- Cortesías y consumo interno (`CTS`, campo `cort` en las líneas, sección `cortR` del reporte).
- Preparaciones con costo y caldo base automático en caldos (`PREP0`, `PREPC`, `prepCU`, `expP`, `CALDO0`, `CAPSU0`, `PAELLA0`, `SWAPP`, `SALSAS`/`salsaR`, `prepBox`), guarniciones por opción (`GUARM`, `guar`, `guarNota`, `ARROZ0`).

## Tercera conversación: análisis y reportes automáticos (desde 2026-11-23)
Hay una tercera conversación de Claude que **solo lee** los datos de Firestore para mandar a Jorge reportes y listas de compras automáticas. No modifica el POS salvo que Jorge lo pida (y entonces sigue estas mismas reglas).
- Usa un usuario de **solo lectura**: `guadalupepulpito@gmail.com`. En las reglas de Firestore tiene `allow read` pero no `write` (función `lector()`). **No quitar esa función al editar las reglas** y no darle permiso de escritura. Nadie del personal debe usar ese correo.
- Tareas programadas que leen Firestore: lista de compras para Central (domingo y jueves 8:00 a. m.) y reporte semanal (lunes 7:38 a. m.).
- **Cuota de Firestore:** el proyecto está en el plan gratuito (50,000 lecturas al día, compartidas por el POS y las tareas). El 2026-11-23 se agotó por lecturas completas de colecciones grandes (`lineas` tiene más de 6,500 documentos). Por eso: ningún cambio al POS ni ningún script debe leer colecciones completas de `lineas`, `pagos`, `movs` o `compras`; siempre filtrar por fecha (`where("at", ">=", ...)`) o por límite.
- La lista de compras usa la colección `conteos` (conteos físicos) y los gastos de caja de `movs` para detectar compras hechas como gasto. Si cambia la forma de guardar esos datos, avisar en este archivo.
