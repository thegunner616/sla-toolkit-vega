---
title: "Informe Técnico de Verificación de SLA — Caso Agrícola Valle de Elqui SpA"
subtitle: "Carrera: Ingeniería en Telecomunicaciones | Asignatura: Infraestructura de Telecomunicaciones Avanzada | Inacap Sede La Serena"
author: "Estudiante: Vicente Vega Yáñez | Docente: Daniel Ruz"
date: "Fecha de entrega: 18/11/2026 — Repositorio: https://github.com/thegunner616/sla-toolkit-vega (Tag v1.1)"
geometry: margin=2cm
---

# Informe Técnico de Verificación de Cumplimiento SLA

## 01. Identificación
- **Servicio:** Internet dedicado simétrico de 200 Mbps (Cláusula 2.1).
- **Cliente:** Agrícola Valle de Elqui SpA (Planta exportadora en Vicuña).
- **Proveedor:** NorteNet Telecomunicaciones.
- **Período evaluado:** 01 al 30 de septiembre de 2026 (30 días calendario = 43.200 minutos).
- **Punto de demarcación:** Puerto LAN del CPE instalado en la planta Vicuña (Cláusula 2.2).
- **Integrante:** Vicente Vega Yáñez (Carrera: Ingeniería en Telecomunicaciones | Asignatura: Infraestructura de Telecomunicaciones Avanzada | Sección: DCIT06 | Docente: Daniel Ruz | Sede La Serena | Entrega: 18/11/2026).
- **Repositorio:** https://github.com/thegunner616/sla-toolkit-vega (Tag v1.1).

## 02. Resumen ejecutivo
El servicio **no cumple** el SLA durante septiembre de 2026. Se verificó el incumplimiento de **disponibilidad** (99,63 % frente al objetivo ≥ 99,9 %) y de **tiempo de respuesta** (66 min en el ticket INC-2672 frente al límite ≤ 60 min); las métricas de latencia (27,4 ms), jitter (9,92 ms), throughput (180,75 Mbps) y MTTR (75 min máx.) cumplen, mientras que la pérdida de paquetes presenta evidencia insuficiente. Corresponde aplicar un crédito de servicio total del **15 %**, equivalente a **$180.000 CLP neto** sobre el cargo mensual.

## 03. Alcance y referencias
- **Cláusulas evaluadas:** Cláusulas 2.1 (servicio), 2.2 (demarcación), 3.1 (disponibilidad), 3.2 (latencia), 3.3 (jitter), 3.4 (pérdida), 3.5 (throughput), 4.1 (tiempo de respuesta), 4.2 (MTTR), 5.1 (validez ≥ 90 %), 6.1 y 6.2 (exclusiones y cómputo), 7.2 (respaldo UPS) y 8.1 a 8.4 (créditos y tope).
- **Normas aplicadas:** ITU-T E.860, ITU-T Y.1540, RFC 3393, RFC 5357 (TWAMP) y RFC 6349.

## 04. Metodología

### a) Variables y parámetros contractuales por métrica
| Métrica | Operador y umbral | Unidad | Período | Punto de medición | Herramienta | Estadístico |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Disponibilidad (3.1) | ≥ 99,9 | % | Mensual (30 d) | Puerto LAN CPE | NMS + Tickets | Mensual |
| Latencia (3.2) | ≤ 30 | ms | Mensual (cada 60 s) | CPE a servidor La Serena | ICMP (Zabbix) | Promedio |
| Jitter (3.3) | ≤ 10 | ms | Mensual | Demarcación (CPE) | TWAMP (RFC 3393) | Promedio |
| Pérdida (3.4) | ≤ 0,5 | % | Mensual | Demarcación (CPE) | TWAMP (RFC 5357) | Mensual |
| Throughput (3.5) | ≥ 180 (90% de 200) | Mbps | Mensual (mín. 4) | Demarcación (CPE) | iperf3 TCP (RFC 6349) | Promedio |
| Tiempo respuesta (4.1) | ≤ 60 | min | Por incidente | Mesa de ayuda | Tickets proveedor | 100% incidentes |
| MTTR (4.2) | ≤ 240 (4 h) | min | Por incidente atrib. | Demarcación / NMS | NMS + Tickets | Por incidente |

### b) Validez y cobertura de la evidencia (Cláusula 5.1 ≥ 90 %)
- **Disponibilidad:** Cobertura del **100 %** (43.200 / 43.200 min) cruzando Anexo 1 (NMS del cliente) y Anexo 2 (tickets y avisos del proveedor). **Válida.**
- **Latencia (Anexo 3):** Zabbix del cliente registró 42.725 muestras válidas de 43.200 esperadas:
  $$\text{Cobertura}_{\text{latencia}} = \frac{42.725}{43.200} \times 100 = 98,90\% \ge 90\% \quad \Rightarrow \quad \textbf{Válida}$$
  *(Las 475 muestras faltantes coinciden con los 475 minutos totales de interrupción en el mes).*
  Se **descarta** el reporte del proveedor (22,1 ms) porque mide entre su PE y su core en Santiago, incumpliendo el tramo pactado en la Cláusula 3.2 (CPE a servidor en La Serena).
- **Jitter (Anexo 4):** Colector TWAMP del cliente desde la demarcación sumó $9.870 + 10.025 + 9.900 + 12.930 = 42.725$ muestras válidas:
  $$\text{Cobertura}_{\text{jitter}} = \frac{42.725}{43.200} \times 100 = 98,90\% \ge 90\% \quad \Rightarrow \quad \textbf{Válida}$$
- **Pérdida de paquetes (Anexo 5):** El colector TWAMP del cliente operó solo 18 días (01 al 18-sep = 25.920 min brutos) antes de detenerse por disco lleno:
  $$\text{Cobertura}_{\text{pérdida}} = \frac{18}{30} \times 100 = 60,00\% < 90\% \quad \Rightarrow \quad \textbf{No válida (Evidencia insuficiente)}$$
  Se **descarta** el reporte del proveedor (0,18 %) porque mide entre PE y core en Santiago, fuera de la demarcación exigida en la Cláusula 3.4.
- **Throughput (Anexo 6):** Se ejecutaron 4 pruebas iperf3 TCP (4 flujos, 60 s) en el puerto LAN del CPE (05, 12, 19 y 26-sep), cumpliendo el mínimo de 4 pruebas mensuales (**100 % válidas**). Se **descarta** la medición del 18-sep (95 Mbps) por realizarse con Speedtest web desde un notebook por Wi-Fi, incumpliendo herramienta, punto y medio físico de la Cláusula 3.5.

### c) Información faltante
- **Métrica afectada:** Pérdida de paquetes (Cláusula 3.4).
- **Dato faltante:** Registros TWAMP desde el puerto LAN del CPE entre el 19 y el 30 de septiembre (12 días / 17.280 min), perdidos por disco lleno en el colector del cliente. Se requieren al menos 12.960 muestras adicionales en la demarcación para alcanzar el 90 % mínimo (38.880 muestras).

## 05. Resultados

### a) Clasificación de eventos de caída (Anexos 1 y 2)
| Evento | Fecha y tramo | Duración | Ticket / Aviso | Clasificación | Fundamento contractual |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **E1** | 03-sep 02:00–05:30 | 210 min (3,5 h) | MNT-0903 (aviso 29-ago 10:00) | **Excluido** | Cláusula 6.1a: mantención programada avisada con 112 h (≥ 72 h) y duración 3,5 h (≤ 4 h/mes). |
| **E2** | 09-sep 14:12–15:07 | 55 min | INC-2611 | **Atribuible** | Corte de fibra en tramo de acceso del proveedor; no existe declaración de fuerza mayor (6.1b). |
| **E3** | 15-sep 10:40–12:25 | 105 min | INC-2648 | **Excluido** | Cláusulas 6.1c y 7.2: corte eléctrico interno en planta del cliente; respaldo UPS es responsabilidad del cliente. |
| **E4** | 21-sep 22:05–23:20 | 75 min | INC-2672 | **Atribuible** | Falla interna de tarjeta de línea en router PE La Serena del proveedor. |
| **E5** | 27-sep 08:30–09:00 | 30 min | INC-2690 (aviso 26-sep 18:00) | **Atribuible** | Cláusula 6.1a: mantención de emergencia avisada con solo 14,5 h de anticipación (< 72 h exigidas). |

### b) Desarrollo matemático de métricas

1. **Disponibilidad, caída permitida y exceso (Cláusulas 3.1 y 6.2):**
   $$T_{\text{total}} = 30 \times 1.440 = 43.200\text{ min}$$
   $$T_{\text{caída\_atribuible}} = 55\text{ (E2)} + 75\text{ (E4)} + 30\text{ (E5)} = 160\text{ min}$$
   $$A = \left( \frac{43.200 - 160}{43.200} \right) \times 100 = \frac{43.040}{43.200} \times 100 = 99,63\% < 99,9\% \quad \Rightarrow \quad \textbf{NO CUMPLE}$$
   $$T_{\text{permitido}} = 43.200 \times (1 - 0,999) = 43,2\text{ min} \qquad ; \qquad \text{Exceso} = 160 - 43,2 = 116,8\text{ min}$$

2. **Latencia (Cláusula 3.2, Anexo 3):**
   - RTT promedio medido por Zabbix = **$27,4\text{ ms} \le 30\text{ ms}$** $\Rightarrow$ **CUMPLE** (margen de $-2,6\text{ ms}$). El p95 (41,2 ms) y máximo (118 ms) no determinan incumplimiento porque el contrato fija el promedio mensual.

3. **Jitter ponderado por muestras (Cláusula 3.3, Anexo 4):**
   $$J_{\text{mensual}} = \frac{(9,0 \times 9.870) + (10,5 \times 10.025) + (13,8 \times 9.900) + (7,2 \times 12.930)}{9.870 + 10.025 + 9.900 + 12.930}$$
   $$J_{\text{mensual}} = \frac{88.830 + 105.262,5 + 136.620 + 93.096}{42.725} = \frac{423.808,5}{42.725} = 9,92\text{ ms} \le 10\text{ ms} \quad \Rightarrow \quad \textbf{CUMPLE}$$

4. **Pérdida de paquetes (Cláusula 3.4, Anexo 5):**
   - Medición parcial 01 al 18-sep = $0,31\%$, con cobertura $60,0\% < 90\%$ $\Rightarrow$ **EVIDENCIA INSUFICIENTE**.

5. **Throughput promedio (Cláusula 3.5, Anexo 6):**
   $$TH_{\text{prom}} = \frac{186 + 182 + 171 + 184}{4} = \frac{723}{4} = 180,75\text{ Mbps} \ge 180\text{ Mbps} \quad \Rightarrow \quad \textbf{CUMPLE}$$

6. **Tiempo de respuesta y MTTR por incidente (Cláusulas 4.1 y 4.2, Anexo 2):**

| Ticket | Evento | Apertura | Primera respuesta | Tiempo resp. (≤ 60 m) | Restauración | MTTR (≤ 240 m) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| INC-2611 | E2 (Atrib.) | 09-sep 14:18 | 09-sep 14:41 | **23 min** (Cumple) | 55 min caída | **Cumple** |
| INC-2648 | E3 (Cliente) | 15-sep 10:47 | 15-sep 11:20 | **33 min** (Cumple) | 105 min (cliente) | No aplica |
| INC-2672 | E4 (Atrib.) | 21-sep 22:09 | 21-sep 23:15 | **66 min** (**NO CUMPLE**) | 75 min caída | **Cumple** |
| INC-2690 | E5 (Atrib.) | 27-sep 08:33 | 27-sep 08:40 | **7 min** (Cumple) | 30 min caída | **Cumple** |

### c) Tabla consolidada de resultados
| Métrica | Objetivo | Medido | Desviación | Fuente | Veredicto | Crédito |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Disponibilidad | ≥ 99,9 % | 99,63 % | -0,27 pp | Anexos 1 y 2 | **No cumple** | **10 %** |
| Latencia | ≤ 30 ms | 27,40 ms | -2,60 ms | Anexo 3 (Zabbix) | **Cumple** | 0 % |
| Jitter | ≤ 10 ms | 9,92 ms | -0,08 ms | Anexo 4 (TWAMP) | **Cumple** | 0 % |
| Pérdida | ≤ 0,5 % | N/D (60% cob.) | N/D | Anexo 5 (TWAMP) | **Evidencia insuficiente** | 0 % |
| Throughput | ≥ 180 Mbps | 180,75 Mbps | +0,75 Mbps | Anexo 6 (iperf3) | **Cumple** | 0 % |
| Tiempo respuesta | ≤ 60 min (100%) | 66 min máx. | +6 min | Anexo 2 (Tickets) | **No cumple** | **5 %** |
| MTTR | ≤ 240 min | 75 min máx. | -165 min | Anexos 1 y 2 | **Cumple** | 0 % |

## 06. Análisis de incumplimientos
| Métrica incumplida | Cuándo ocurrió | Causa raíz | Impacto en el negocio | Origen |
| :--- | :--- | :--- | :--- | :--- |
| **Disponibilidad** (99,63 %) | 09, 21 y 27 de septiembre (160 min totales) | Corte de fibra en acceso por obras viales (E2), falla de tarjeta de línea en PE La Serena (E4) y mantención de emergencia sin aviso de 72 h (E5). | Interrupción total de ERP, trazabilidad de exportación y telefonía IP en la planta Vicuña por 2 h 40 min. | Proveedor |
| **Tiempo de respuesta** (66 min) | 21-sep entre 22:09 y 23:15 (INC-2672) | Demora en la atención y diagnóstico inicial de primera línea del NOC del proveedor en horario nocturno. | Retraso de 6 minutos sobre el máximo contractual para iniciar el escalamiento y reemplazo de tarjeta en PE. | Proveedor |

## 07. Conclusiones técnicas

### a) Veredicto global y cálculo del crédito de servicio
- **Veredicto global:** **NO CUMPLE** el SLA de septiembre de 2026.
- **Cálculo del crédito aplicable (Cláusulas 8.1 a 8.4):**
  - Tramo por disponibilidad de 99,63 % (ubicado en rango $99,5\%$ a $< 99,9\%$): **$10\%$**.
  - Incumplimiento de tiempo de respuesta en INC-2672 (Cláusula 8.2): **$5\%$**.
  - Suma de créditos: $10\% + 5\% = 15\%$ (dentro del tope contractual de $50\%$ fijado en Cláusula 8.3).
  - **Monto a descontar:** $0,15 \times \$1.200.000 = \mathbf{\$180.000\text{ CLP neto}}$.

### b) Viabilidad del objetivo de disponibilidad (Anexo 7)
- **Topología actual en serie (CPE + Fibra única + PE La Serena + Backbone):**
  $$A_{\text{serie\_actual}} = 0,9995 \times 0,9980 \times 0,9999 \times 0,9999 = 0,997301 \text{ (}99,73\%\text{)}$$
  $$\text{Caída esperada mensual} = (1 - 0,997301) \times 43.200 = 116,58\text{ min/mes} > 43,2\text{ min/mes permitidos}$$
  Con la ruta única de fibra (99,80 %), **no es técnicamente viable** sostener un SLA de 99,9 %.
- **Topología con respaldo en paralelo (Fibra 99,80 % + Radioenlace 99,50 %):**
  $$A_{\text{acceso\_paralelo}} = 1 - (1 - 0,9980)(1 - 0,9950) = 1 - (0,0020 \times 0,0050) = 0,999990 \text{ (}99,999\%\text{)}$$
  $$A_{\text{total\_con\_respaldo}} = 0,9995 \times 0,999990 \times 0,9999 \times 0,9999 = 0,999290 \text{ (}99,93\%\text{)}$$
  $$\text{Caída esperada con respaldo} = (1 - 0,999290) \times 43.200 = 30,67\text{ min/mes} \le 43,2\text{ min/mes permitidos}$$
  Incorporar el radioenlace de respaldo en paralelo hace **técnicamente viable** cumplir el 99,9 % con un margen positivo de 12,53 min al mes.

### c) Respuesta al correo del Gerente de Operaciones
| Afirmación del gerente | ¿Se sostiene? | Fundamento técnico y contractual |
| :--- | :--- | :--- |
| *"Septiembre fue un desastre. Se cayó varias veces"* | **Parcialmente** | Hubo 5 cortes en NMS, pero 2 están excluidos (E1 mantención con aviso de 112 h y E3 corte eléctrico interno sin UPS). Las 3 caídas atribuibles suman 160 min y sí incumplen disponibilidad (99,63 %). |
| *"hice un Speedtest desde mi notebook y me dio 95 Mbps cuando pagamos 200"* | **No** | El Speedtest por Wi-Fi desde un notebook no es válido. La Cláusula 3.5 exige iperf3 TCP en el puerto LAN del CPE, donde las 4 pruebas oficiales promediaron 180,75 Mbps (cumple ≥ 180 Mbps). |
| *"en Zabbix vi peaks de 118 ms"* | **No** | El máximo puntual fue 118 ms, pero la Cláusula 3.2 evalúa el RTT promedio mensual (≤ 30 ms), el cual cerró en 27,4 ms (cumple). |
| *"Quiero que le exijamos a NorteNet el crédito máximo (50%)"* | **No** | El crédito del 50 % requiere disponibilidad < 99,0 % o acumulación hasta el tope. Por los incumplimientos demostrables (disponibilidad y tiempo de respuesta) corresponde exigir el **15 % ($180.000 neto)**. |

## 08. Recomendaciones priorizadas
| Hallazgo | Recomendación técnica | Qué mejora | Prioridad |
| :--- | :--- | :--- | :--- |
| Disponibilidad teórica en serie de 99,73 % (< 99,9 % pactado) | Contratar el enlace de respaldo inalámbrico (radioenlace 99,50 %) en configuración activo/pasivo con conmutación BGP/BFD. | Eleva la disponibilidad teórica a 99,93 % y elimina el punto único de falla en la fibra de acceso. | **Alta** |
| Corte E3 (105 min) por falta de energía en CPE de planta Vicuña | Instalar una UPS dedicada de doble conversión en el rack de comunicaciones del CPE con monitoreo SNMP. | Evita caídas del servicio por cortes eléctricos internos de la planta. | **Alta** |
| Pérdida de 12 días de datos TWAMP por disco lleno en colector | Configurar rotación automática de logs (logrotate) y alertas de capacidad de disco al 80 % en el servidor colector. | Garantiza cobertura ≥ 90 % (Cláusula 5.1) para auditar pérdida de paquetes sin evidencia insuficiente. | **Media** |
| Jitter mensual muy cercano al umbral (9,92 ms vs 10 ms) | Solicitar al proveedor revisión de colas QoS y priorización DSCP EF para tráfico de telefonía IP. | Reduce la variación de retardo y protege la calidad de llamadas VoIP. | **Media** |
| Mediciones informales por Wi-Fi (Speedtest) | Establecer un procedimiento interno de pruebas iperf3 cableadas directamente en el puerto LAN del CPE. | Asegura evidencia contractualmente válida ante futuros reclamos. | **Baja** |

## 09. Automatización del proceso y declaración de uso de IA

### a) Flujo de automatización
1. **Carga de datos (manual):** Se extrajeron las cláusulas a ejemplos/caso-valle-elqui/sla.md, los umbrales y tramos a ejemplos/caso-valle-elqui/objetivos.yaml y las mediciones válidas a ejemplos/caso-valle-elqui/mediciones.csv.
2. **Cálculo automatizado:** Se ejecutó herramientas/calc_sla.py para evaluar operadores, cobertura mínima, disponibilidad, promedios, tiempos máximos y créditos, exportando el resultado a ejemplos/caso-valle-elqui/salida_calc.txt.
3. **Cálculos complementarios manuales:** Se resolvieron manualmente la clasificación de eventos según cláusulas de exclusión (E1 y E3), el promedio ponderado del jitter por cantidad de muestras y el análisis de viabilidad serie/paralelo.
4. **Compilación a PDF:** Se redactó ejemplos/caso-valle-elqui/informe.md integrando la salida de la calculadora y se compiló a informe.pdf mediante Pandoc y XeLaTeX.

### b) Comandos para regenerar el informe desde cero

    python3 herramientas/calc_sla.py -o ejemplos/caso-valle-elqui/objetivos.yaml \
      -m ejemplos/caso-valle-elqui/mediciones.csv > ejemplos/caso-valle-elqui/salida_calc.txt
    pandoc ejemplos/caso-valle-elqui/informe.md -o ejemplos/caso-valle-elqui/informe.pdf --pdf-engine=xelatex

### c) Declaración de uso de IA
- **Herramienta utilizada:** Gemini (asistente de IA) en la etapa de estructuración del script Python (calc_sla.py) y formato Markdown del informe.
- **Contexto entregado:** Pautas de la actividad, anexos del caso Agrícola Valle de Elqui SpA y estructura del repositorio.
- **Revisión y verificación:** El autor revisó cada fórmula y comprobó que todas las cifras del informe coinciden exactamente con los cálculos manuales y con el archivo ejemplos/caso-valle-elqui/salida_calc.txt.

---

## Anexos

### Anexo A: Contenido completo de ejemplos/caso-valle-elqui/objetivos.yaml

    servicio: "Internet dedicado simetrico 200 Mbps - Agricola Valle de Elqui SpA"
    periodo: "2026-09"
    minutos_periodo: 43200
    cobertura_minima: 0.90
    cargo_mensual: 1200000
    tope_credito: 0.50
    credito_otras: 0.05

    metricas:
      disponibilidad: {operador: ">=", objetivo: 99.9, unidad: "%"}
      latencia: {operador: "<=", objetivo: 30, unidad: "ms", estadistico: promedio}
      jitter: {operador: "<=", objetivo: 10, unidad: "ms", estadistico: promedio}
      perdida: {operador: "<=", objetivo: 0.5, unidad: "%", estadistico: promedio}
      throughput: {operador: ">=", objetivo: 180, unidad: "Mbps", estadistico: promedio}
      tiempo_respuesta: {operador: "<=", objetivo: 60, unidad: "min", estadistico: maximo}
      mttr: {operador: "<=", objetivo: 240, unidad: "min", estadistico: maximo, aplica_credito: false}

    creditos_disponibilidad:
      - {desde: 99.5, hasta: 99.9, credito: 0.10}
      - {desde: 99.0, hasta: 99.5, credito: 0.25}
      - {desde: 0.0,  hasta: 99.0, credito: 0.50}

### Anexo B: Contenido completo de ejemplos/caso-valle-elqui/mediciones.csv

    fecha,metrica,valor,unidad,cobertura
    2026-09-09,caida_atribuible,55,min,1.00
    2026-09-21,caida_atribuible,75,min,1.00
    2026-09-27,caida_atribuible,30,min,1.00
    2026-09-30,latencia,27.4,ms,0.989
    2026-09-30,jitter,9.92,ms,0.989
    2026-09-18,perdida,0.31,%,0.600
    2026-09-05,throughput,186,Mbps,1.00
    2026-09-12,throughput,182,Mbps,1.00
    2026-09-19,throughput,171,Mbps,1.00
    2026-09-26,throughput,184,Mbps,1.00
    2026-09-09,tiempo_respuesta,23,min,1.00
    2026-09-15,tiempo_respuesta,33,min,1.00
    2026-09-21,tiempo_respuesta,66,min,1.00
    2026-09-27,tiempo_respuesta,7,min,1.00
    2026-09-09,mttr,55,min,1.00
    2026-09-21,mttr,75,min,1.00
    2026-09-27,mttr,30,min,1.00

### Anexo C: Salida completa de calc_sla.py (ejemplos/caso-valle-elqui/salida_calc.txt)

    Servicio: Internet dedicado simetrico 200 Mbps - Agricola Valle de Elqui SpA | Periodo: 2026-09
    --------------------------------------------------------------------------
    Metrica            Objetivo       Medido         Veredicto             
    --------------------------------------------------------------------------
    disponibilidad     >= 99.9 %      99.63 %        NO CUMPLE             
    latencia           <= 30.0 ms     27.40 ms       CUMPLE                
    jitter             <= 10.0 ms     9.92 ms        CUMPLE                
    perdida            <= 0.5 %       Cob < 90%      EVIDENCIA INSUFICIENTE
    throughput         >= 180.0 Mbps  180.75 Mbps    CUMPLE                
    tiempo_respuesta   <= 60.0 min    66.00 min      NO CUMPLE             
    mttr               <= 240.0 min   75.00 min      CUMPLE                
    --------------------------------------------------------------------------
    Credito calculado : 10% (disponibilidad) + 5% (tiempo_respuesta) = 15% (Tope: 50%)
    Credito aplicable : 15% -> $180.000 CLP neto

### Anexo D: Cálculos manuales complementarios, historial de commits y CHANGELOG.md

#### 1. Resumen de cálculos manuales no cubiertos automáticamente por calc_sla.py
- **Clasificación contractual de exclusiones:** Evaluación de plazos de aviso previo (112 h en MNT-0903 vs 14,5 h en INC-2690 frente a las 72 h de Cláusula 6.1a) y responsabilidad de respaldo eléctrico UPS del cliente (INC-2648, Cláusulas 6.1c y 7.2).
- **Jitter ponderado por muestras:** Ponderación de promedios semanales según cantidad de muestras válidas (423.808,5 / 42.725 = 9,92 ms).
- **Viabilidad de infraestructura (serie vs paralelo):** Cálculo de disponibilidad teórica actual en serie (99,73 %, caída esperada 116,58 min/mes) y con respaldo de radioenlace en paralelo (99,93 %, caída esperada 30,67 min/mes).

#### 2. Extracto de CHANGELOG.md e historial de versiones

    ## [1.0] - 2026-11-18
    ### Agregado
    - Método en 6 pasos (docs/metodo.md), normas (docs/normas.md) y glosario.
    - Plantillas reutilizables (plantillas/) y fórmulas (formulas/formulas.md).
    - Calculadora herramientas/calc_sla.py y caso base ejemplos/enlace-dedicado/.

    ## [1.1] - 2026-11-18
    ### Agregado
    - Caso completo ejemplos/caso-valle-elqui/ (sla, yaml, csv, salida, informe PDF).
    - Validación de cobertura mínima (EVIDENCIA INSUFICIENTE), respuesta y MTTR.
    ### Pendiente
    - calc_sla.py: cálculo automático de jitter ponderado por subperíodos semanales.
    - calc_sla.py: clasificación automática de eventos atribuibles vs. excluidos.
