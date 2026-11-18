# Glosario Técnico de Gestión de SLA

- **SLA (Service Level Agreement):** Contrato formal entre un proveedor de servicios y un cliente que define el servicio, las métricas de calidad, los objetivos comprometidos, las exclusiones y las compensaciones por incumplimiento.
- **SLR (Service Level Requirement):** Requisito de nivel de servicio expresado desde la perspectiva y necesidades del negocio del cliente antes de traducirse a parámetros técnicos.
- **SLI (Service Level Indicator):** Indicador cuantitativo específico utilizado para medir el desempeño del servicio (ej. latencia RTT en ms, tasa de pérdida en %).
- **SLO (Service Level Objective):** Valor umbral o rango objetivo que debe alcanzar un SLI para considerar que el servicio cumple con lo pactado (ej. disponibilidad ≥ 99,9%).
- **OLA (Operational Level Agreement):** Acuerdo interno entre distintas áreas técnicas del mismo proveedor (ej. NOC y planta externa) necesario para sostener los compromisos de un SLA frente al cliente.
- **MTBF (Mean Time Between Failures):** Tiempo medio entre fallas; indicador de confiabilidad que mide el tiempo promedio de operación normal entre dos interrupciones consecutivas.
- **MTTR (Mean Time To Repair / Restore):** Tiempo medio de reparación o restauración; tiempo promedio transcurrido desde que se detecta o reporta una falla hasta que el servicio vuelve a operar con normalidad.
- **Punto de demarcación:** Interfaz física o lógica exacta (ej. puerto LAN del CPE) que separa la red y responsabilidad del proveedor de la red interna del cliente.
- **RTT (Round-Trip Time):** Tiempo de ida y vuelta que tarda un paquete desde el origen hasta el destino y su respuesta de regreso, medido en milisegundos (ms).
- **Jitter (IPDV):** Variación estadística en el retardo de llegada de paquetes consecutivos dentro de un mismo flujo, crítica para tráfico en tiempo real como telefonía IP.
- **Throughput:** Tasa efectiva de transferencia de datos útiles entregados por unidad de tiempo sobre un enlace (medida habitualmente en Mbps).
- **Crédito de servicio:** Descuento porcentual aplicado sobre la facturación mensual del cliente cuando el proveedor incumple uno o más objetivos del SLA.
