# Historial de Cambios (CHANGELOG)

Todos los cambios relevantes de este toolkit se documentan en este archivo.

## [1.0] - 2026-11-18
### Agregado
- Método de diseño de SLA en 6 pasos (`docs/metodo.md`).
- Marco normativo ITIL 4, ISO/IEC, ITU-T, MEF e IETF (`docs/normas.md`) y glosario (`docs/glosario.md`).
- Plantillas reutilizables de SLA, checklist de requisitos e informe técnico (`plantillas/`).
- Fórmulas de disponibilidad, serie/paralelo, latencia, jitter, pérdida, throughput y créditos (`formulas/formulas.md`).
- Calculadora `herramientas/calc_sla.py` y caso base `ejemplos/enlace-dedicado/`.

## [1.1] - 2026-11-18
### Agregado
- Caso de estudio completo `ejemplos/caso-valle-elqui/` (`sla.md`, `objetivos.yaml`, `mediciones.csv`, `salida_calc.txt`, `informe.md`, `informe.pdf`).
- Validación de cobertura mínima (`EVIDENCIA INSUFICIENTE`) y evaluación de `tiempo_respuesta` y `mttr` en `calc_sla.py`.
### Pendiente
- `calc_sla.py`: cálculo automático de promedio ponderado de jitter directamente desde subperíodos semanales sin preprocesamiento.
- `calc_sla.py`: clasificación automática de eventos atribuibles vs. excluidos según horas de aviso previo.
