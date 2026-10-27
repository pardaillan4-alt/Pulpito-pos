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
- Cortesías y consumo interno (`CTS`, campo `cort` en las líneas, sección `cortR` del reporte).
