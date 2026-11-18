# SLA Toolkit — Vicente Vega Yáñez

Herramienta para diseñar, calcular y verificar Acuerdos de Nivel de Servicio (SLA) en redes de telecomunicaciones. Desarrollado para la asignatura **Infraestructura de Telecomunicaciones Avanzada** (Ingeniería en Telecomunicaciones, INACAP Sede La Serena).

## Contenido del repositorio
- `docs/`: Método de diseño de SLA en 6 pasos, marco normativo y glosario técnico.
- `plantillas/`: Plantillas reutilizables de SLA, checklist de requisitos e informe de cumplimiento.
- `formulas/`: Fórmulas matemáticas de disponibilidad, serie/paralelo, latencia, jitter, pérdida, throughput y créditos.
- `herramientas/`: Calculadora automatizada `calc_sla.py` y archivo de configuración `objetivos.yaml`.
- `datos/`: Dataset de mediciones de prueba en formato CSV.
- `ejemplos/`: Casos prácticos aplicados (`enlace-dedicado` en `v1.0` y `caso-valle-elqui` en `v1.1`).

## Requisitos
- Python 3.8 o superior y librería `PyYAML` (`pip install pyyaml`)
- `Pandoc` y `XeLaTeX` (para compilar informes Markdown a PDF)

## Cómo usar la calculadora

    python3 herramientas/calc_sla.py -o herramientas/objetivos.yaml -m datos/mediciones-ejemplo.csv
