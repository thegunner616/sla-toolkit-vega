# SLA Toolkit — Diseño, Modelamiento y Verificación de SLA (`sla-toolkit-vega`)

Toolkit técnico en Python y Markdown para el diseño contractual, modelamiento de disponibilidad y auditoría de cumplimiento de **Acuerdos de Nivel de Servicio (SLA)** en enlaces de telecomunicaciones empresariales.

- **Autor:** Vicente Vega Yáñez
- **Carrera:** Ingeniería en Telecomunicaciones — INACAP Sede La Serena
- **Asignatura:** Infraestructura de Telecomunicaciones Avanzada (Sección DCIT06)
- **Docente:** Daniel Ruz
- **Repositorio:** https://github.com/thegunner616/sla-toolkit-vega

---

## 1. Estructura del repositorio

    sla-toolkit-vega/
    ├── docs/
    │   ├── metodo.md              # Metodología de diseño de SLA en 6 etapas
    │   ├── normas.md              # Marco normativo (ITU-T e IETF RFC)
    │   └── glosario.md            # Definiciones técnicas y contractuales
    ├── plantillas/
    │   ├── plantilla_sla.md       # Modelo base de contrato SLA
    │   ├── checklist_sla.md       # Lista de verificación de requisitos y demarcación
    │   └── plantilla_informe.md   # Estructura estándar para auditorías de cumplimiento
    ├── formulas/
    │   └── formulas.md            # Ecuaciones de disponibilidad, serie/paralelo, QoS y créditos
    ├── herramientas/
    │   └── calc_sla.py            # Calculadora CLI de evaluación de métricas, cobertura y créditos
    ├── ejemplos/
    │   ├── enlace-dedicado/       # Caso base de referencia (v1.0)
    │   └── caso-valle-elqui/      # Auditoría completa Agrícola Valle de Elqui SpA (v1.1)
    │       ├── sla.md             # Extracto de cláusulas contractuales evaluadas
    │       ├── objetivos.yaml     # Umbrales, operadores, cobertura mínima y tramos de crédito
    │       ├── mediciones.csv     # Registros válidos depurados del período
    │       ├── salida_calc.txt    # Reporte generado automáticamente por calc_sla.py
    │       ├── informe.md         # Informe técnico completo en Markdown + LaTeX
    │       └── informe.pdf        # Informe técnico compilado con Pandoc / XeLaTeX
    ├── CHANGELOG.md               # Registro de cambios entre versiones (v1.0 y v1.1)
    └── README.md                  # Documentación principal del proyecto

---

## 2. Marco normativo y métricas soportadas

El toolkit implementa definiciones y métodos de medición alineados con estándares internacionales:

| Norma / RFC | Aplicación dentro del toolkit |
| :--- | :--- |
| **ITU-T E.860** | Estructura contractual de SLA, delimitación de responsabilidades y punto de demarcación. |
| **ITU-T Y.1540** | Definición de parámetros de transferencia y disponibilidad de paquetes IP. |
| **RFC 3393** | Medición de variación de retardo de paquetes IP (*IPDV / Jitter*). |
| **RFC 5357** | Protocolo *Two-Way Active Measurement Protocol* (TWAMP) para jitter y pérdida de paquetes. |
| **RFC 6349** | Metodología de pruebas de *throughput* TCP en punto de demarcación (`iperf3`). |

---

## 3. Guía rápida de uso (`calc_sla.py`)

### Requisitos
- **Python 3.8+** con la librería `PyYAML` (`pip install pyyaml` o `sudo apt install python3-yaml`).
- **Opcional (para compilar informes PDF):** `pandoc` y `texlive-xetex`.

### Ejecución desde terminal

Evaluar el caso base (`v1.0`):

    python3 herramientas/calc_sla.py -o ejemplos/enlace-dedicado/objetivos.yaml -m ejemplos/enlace-dedicado/mediciones.csv

Evaluar el caso de estudio **Agrícola Valle de Elqui SpA** (`v1.1`) y exportar el resultado:

    python3 herramientas/calc_sla.py \
      -o ejemplos/caso-valle-elqui/objetivos.yaml \
      -m ejemplos/caso-valle-elqui/mediciones.csv > ejemplos/caso-valle-elqui/salida_calc.txt

Compilar el informe técnico a PDF:

    pandoc ejemplos/caso-valle-elqui/informe.md -o ejemplos/caso-valle-elqui/informe.pdf --pdf-engine=xelatex

### Capacidades de la calculadora
- **Validación de cobertura de evidencia:** Si una métrica no alcanza el porcentaje mínimo de muestras válidas definido en `cobertura_minima` (ej. `0.90`), la marca automáticamente como `EVIDENCIA INSUFICIENTE` sin aplicar penalización indebida.
- **Evaluación multi-estadístico:** Soporta evaluación por disponibilidad porcentual (`caida_atribuible` sobre `minutos_periodo`), promedio (`latencia`, `jitter`, `perdida`, `throughput`) y valor máximo por incidente (`tiempo_respuesta`, `mttr`).
- **Cálculo de créditos:** Aplica tramos escalonados de disponibilidad más créditos adicionales por incumplimiento de métricas operativas, respetando el tope contractual (`tope_credito`).

---

## 4. Casos de estudio incluidos

### Caso base: `ejemplos/enlace-dedicado/` (`v1.0`)
Plantilla funcional inicial con archivo de objetivos YAML y mediciones CSV para validar el funcionamiento base del motor de cálculo.

### Caso de estudio: `ejemplos/caso-valle-elqui/` (`v1.1`)
Auditoría mensual (septiembre de 2026, 43.200 minutos) del enlace dedicado simétrico de 200 Mbps contratado por **Agrícola Valle de Elqui SpA** (planta Vicuña) con **NorteNet Telecomunicaciones**:
- **Disponibilidad:** 99,63 % (160 min de caída atribuible frente a 43,2 min permitidos) — **No cumple** (crédito del 10 %).
- **Latencia y Jitter:** 27,40 ms y 9,92 ms ponderado (cobertura 98,90 %) — **Cumple**.
- **Pérdida de paquetes:** Cobertura del 60,0 % (18/30 días por disco lleno en colector) — **Evidencia insuficiente**.
- **Throughput:** 180,75 Mbps promedio en 4 pruebas `iperf3` TCP en puerto LAN del CPE — **Cumple**.
- **Tiempo de respuesta y MTTR:** 66 min máximo en `INC-2672` (**No cumple**, crédito del 5 %) y 75 min máximo de restauración (**Cumple**).
- **Resultado global:** **Crédito aplicable del 15 % ($180.000 CLP neto)** y análisis de viabilidad que demuestra la necesidad de respaldo en paralelo (radioenlace) para alcanzar el 99,9 % contractual (99,73 % serie vs. 99,93 % paralelo).

---

## 5. Historial de versiones (Tags)

- **`v1.0`:** Toolkit base con metodología, marco normativo, glosario, plantillas, formulario matemático, calculadora CLI y caso base `enlace-dedicado`.
- **`v1.1`:** Incorporación del caso de estudio `caso-valle-elqui`, soporte de cobertura mínima y métricas de incidentes en `calc_sla.py`, e informe técnico completo en Markdown y PDF.
