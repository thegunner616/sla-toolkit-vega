# Extracto de Contrato SLA — Agrícola Valle de Elqui SpA

- **Cliente:** Agrícola Valle de Elqui SpA (Planta Vicuña)
- **Proveedor:** NorteNet Telecomunicaciones
- **Período evaluado:** Septiembre de 2026 (30 días = 43.200 minutos)

## Cláusulas contractuales
- **2.1 Servicio:** Internet dedicado simétrico de 200 Mbps.
- **2.2 Demarcación:** Puerto LAN del CPE instalado en la planta Vicuña.
- **3.1 Disponibilidad:** ≥ 99,9 % mensual (mes calendario).
- **3.2 Latencia:** RTT promedio mensual ≤ 30 ms, medido por ICMP cada 60 s entre el CPE y el servidor de medición del proveedor en La Serena.
- **3.3 Jitter:** Promedio mensual ≤ 10 ms (RFC 3393), medido con TWAMP desde la demarcación.
- **3.4 Pérdida:** ≤ 0,5 % mensual, medida con TWAMP desde la demarcación.
- **3.5 Throughput:** Promedio de las pruebas del mes ≥ 90 % del contratado (≥ 180 Mbps). Pruebas `iperf3` TCP (RFC 6349) en la demarcación, mínimo 4 por mes.
- **4.1 Tiempo de respuesta:** ≤ 60 min desde la apertura del ticket, en el 100 % de los incidentes.
- **4.2 MTTR:** ≤ 4 h (240 min) por incidente atribuible al proveedor.
- **5.1 Validez de la medición:** Un período de medición es válido solo si cubre al menos el 90 % del mes (≥ 38.880 min).
- **6.1 Exclusiones:** a) Mantenciones programadas avisadas con ≥ 72 h de anticipación, máximo 4 h/mes. b) Fuerza mayor declarada. c) Fallas atribuibles al cliente.
- **6.2 Tiempo excluido:** Se considera tiempo disponible; no se descuenta del período.
- **7.2 Energía:** El respaldo eléctrico (UPS) del CPE es responsabilidad del cliente.
- **8.1 Créditos por disponibilidad:** 99,5 % a < 99,9 %: 10 % | 99,0 % a < 99,5 %: 25 % | < 99,0 %: 50 %.
- **8.2 Otros créditos:** 5 % por cada incumplimiento de latencia, jitter, pérdida, throughput o tiempo de respuesta.
- **8.3 Tope:** 50 % del cargo mensual.
- **8.4 Cargo mensual:** $1.200.000 neto.
