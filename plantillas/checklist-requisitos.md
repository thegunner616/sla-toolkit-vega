# Checklist de Levantamiento de Requisitos del Cliente (SLR)

- **Cliente:** [Nombre del cliente]
- **Sitio / Sucursal:** [Dirección o ciudad]
- **Fecha:** [AAAA-MM-DD]

## 1. Criticidad y aplicaciones del negocio
- [ ] Aplicaciones críticas que dependen del enlace (ERP, VoIP, VPN, nube, telemetría): ______________________
- [ ] Horario de operación crítica (ej. 24/7, lunes a viernes 08:00-19:00): ______________________
- [ ] Impacto económico u operativo por cada hora de detención del servicio: ______________________

## 2. Requisitos técnicos y capacidad
- [ ] Ancho de banda de bajada y subida requerido (simétrico / asimétrico): ______________________ Mbps
- [ ] Uso de voz o video en tiempo real (requiere latencia ≤ 150 ms G.114 y jitter bajo): [ ] Sí / [ ] No
- [ ] Nivel de disponibilidad exigido por el negocio (ej. 99,8%, 99,9%, 99,95%): ______________________ %
- [ ] ¿Requiere redundancia física (doble acometida de fibra o respaldo radioenlace/LTE)? [ ] Sí / [ ] No

## 3. Demarcación y condiciones físicas del sitio
- [ ] Ubicación exacta del punto de demarcación (sala de comunicaciones, rack): ______________________
- [ ] ¿El cliente dispone de respaldo eléctrico (UPS) dedicado para el CPE? [ ] Sí / [ ] No
- [ ] ¿Existe puerto libre y acceso físico/lógico para sondas de medición (TWAMP / `iperf3`)? [ ] Sí / [ ] No

## 4. Operación y soporte
- [ ] Tiempo máximo aceptable para primera respuesta ante incidentes: ______________________ min
- [ ] Tiempo máximo aceptable de restauración del servicio (MTTR): ______________________ horas
- [ ] Ventana horaria autorizada para mantenciones programadas: ______________________
