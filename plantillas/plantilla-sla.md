# Acuerdo de Nivel de Servicio (SLA) — [NOMBRE DEL SERVICIO]

## 1. Identificación de las partes
- **Cliente:** [Razón social del cliente]
- **Proveedor:** [Razón social del proveedor]
- **Vigencia:** [Fecha de inicio] al [Fecha de término]

## 2. Definición del servicio y demarcación (ITU-T E.860)
- **2.1 Servicio:** [Descripción técnica, capacidad simétrica/asimétrica, tecnología]
- **2.2 Punto de demarcación:** [Ej. Puerto LAN 1 del CPE instalado en sala técnica del cliente]

## 3. Objetivos de Nivel de Servicio (SLO)
| Cláusula | Métrica (SLI) | Objetivo (SLO) | Herramienta / Norma | Punto de medición |
| :--- | :--- | :--- | :--- | :--- |
| 3.1 | Disponibilidad mensual | ≥ [99,9]% | NMS / Registros de tickets | Demarcación |
| 3.2 | Latencia (RTT promedio) | ≤ [30] ms | ICMP cada 60 s (ITU-T Y.1540) | CPE a servidor proveedor |
| 3.3 | Jitter promedio mensual | ≤ [10] ms | TWAMP (RFC 3393 / RFC 5357) | Demarcación |
| 3.4 | Pérdida de paquetes | ≤ [0,5]% | TWAMP (RFC 5357 / Y.1540) | Demarcación |
| 3.5 | Throughput TCP | ≥ [90]% contratado | `iperf3` TCP 4 flujos (RFC 6349) | Demarcación (mín. 4/mes) |

## 4. Soporte operativo e incidentes
- **4.1 Tiempo de respuesta:** ≤ [60] minutos desde la apertura del ticket en el 100% de los incidentes.
- **4.2 MTTR:** ≤ [4] horas por incidente atribuible al proveedor.

## 5. Validez de las mediciones
- **5.1 Cobertura mínima:** Un período de medición mensual es válido únicamente si cubre al menos el **[90]%** del tiempo o muestras esperadas del mes calendario.

## 6. Exclusiones
- **6.1 Causas excluidas:**
  a) Mantenciones programadas notificadas con al menos **[72] horas** de anticipación, con un tope de **[4] horas/mes**.
  b) Eventos de fuerza mayor formalmente declarados y respaldados.
  c) Fallas originadas en la red interna, configuración o falta de respaldo eléctrico (UPS) del cliente.
- **6.2 Cómputo:** El tiempo excluido se contabiliza como tiempo disponible.

## 7. Créditos de servicio y topes
- **7.1 Tramos por disponibilidad:**
  - [99,5]% a < [99,9]%: **[10]%** de descuento.
  - [99,0]% a < [99,5]%: **[25]%** de descuento.
  - < [99,0]%: **[50]%** de descuento.
- **7.2 Otras métricas:** **[5]%** de descuento por cada métrica incumplida (latencia, jitter, pérdida, throughput o tiempo de respuesta).
- **7.3 Tope mensual:** La suma total de créditos no excederá el **[50]%** del cargo fijo mensual neto.
