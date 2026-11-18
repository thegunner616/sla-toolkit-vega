# Método de Diseño de SLA en 6 Pasos

Este método sigue el proceso de Gestión de Niveles de Servicio de **ITIL 4** y la estructura contractual definida en **ITU-T E.860**. Regla base: *no se compromete ningún objetivo que la infraestructura no pueda sostener ni que no se pueda medir con herramientas normadas.*

## Paso 1: Definir el servicio
- **Qué se hace:** Se delimita exactamente qué servicio se entrega (ej. Internet dedicado simétrico), a quién va dirigido, el alcance operativo y el **punto de demarcación** física y lógica donde termina la responsabilidad del proveedor y comienza la del cliente (ej. puerto LAN del CPE).
- **Norma aplicable:** ITU-T E.860 (estructura de acuerdos de nivel de servicio en telecomunicaciones).
- **Entregable que produce:** Ficha de definición del servicio y diagrama/cláusula de demarcación.

## Paso 2: Levantar los requisitos del cliente (SLR)
- **Qué se hace:** Se relevan las necesidades reales del negocio del cliente en su propio lenguaje (aplicaciones críticas como ERP, VoIP o videoconferencia, horarios de operación, tolerancia a cortes).
- **Norma aplicable:** ITIL 4 — *Service Level Management* (levantamiento de Service Level Requirements).
- **Entregable que produce:** Checklist de requisitos del cliente (`checklist-requisitos.md`).

## Paso 3: Elegir las métricas (SLI)
- **Qué se hace:** Se traducen los requisitos del negocio en indicadores técnicos medibles (disponibilidad, latencia, jitter, pérdida de paquetes y throughput), especificando unidad, estadístico (promedio, percentil), frecuencia y protocolo de prueba.
- **Norma aplicable:** ITU-T Y.1540 / Y.1541, MEF 10.4, RFC 7679, RFC 7680, RFC 3393, RFC 5357 (TWAMP), RFC 6349 y ITU-T G.114.
- **Entregable que produce:** Matriz de indicadores SLI y protocolos de medición.

## Paso 4: Fijar objetivos viables (SLO)
- **Qué se hace:** Antes de firmar umbrales, se calcula matemáticamente la capacidad real de la topología (disponibilidad en serie y paralelo de los enlaces/equipos, y retardo físico por distancia de fibra) para asegurar que los objetivos sean técnicamente alcanzables.
- **Norma aplicable:** ITU-T Y.1541 (clases de QoS) e ingeniería de confiabilidad (cálculo MTBF/MTTR y serie/paralelo).
- **Entregable que produce:** Memoria de cálculo de viabilidad técnica y tabla de umbrales SLO comprometidos.

## Paso 5: Definir operación y medición
- **Qué se hace:** Se establecen las reglas de auditoría del contrato: período de evaluación (ej. mes calendario), cobertura mínima válida de muestras (ej. ≥ 90%), exclusiones permitidas (mantenciones programadas con aviso previo, fuerza mayor declarada, fallas del cliente), tiempos máximos de respuesta a tickets, MTTR, escalamiento y formato de reportes.
- **Norma aplicable:** ITIL 4 (gestión de incidentes y niveles de servicio) e ISO/IEC 20000-1.
- **Entregable que produce:** Cláusulas operativas, de exclusión y de soporte del contrato SLA.

## Paso 6: Definir consecuencias y revisión
- **Qué se hace:** Se fijan los tramos de compensación económica (créditos de servicio por incumplimiento de cada métrica y su tope mensual) y se establece el calendario de revisión periódica para aplicar mejora continua.
- **Norma aplicable:** ISO/IEC 20000-1 (ciclo PDCA: Planificar, Hacer, Verificar, Actuar) e ITU-T E.860.
- **Entregable que produce:** Tabla de penalizaciones/créditos y contrato SLA completo (`plantilla-sla.md`).
