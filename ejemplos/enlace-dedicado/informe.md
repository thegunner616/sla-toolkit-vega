# Informe de Cumplimiento — Enlace Dedicado Base (Julio 2026)

## 1. Resumen
Durante julio de 2026 (44.640 min) se registró una única caída atribuible de 25 minutos, alcanzando una disponibilidad de 99,94% (≥ 99,9%). Todas las métricas técnicas cumplen los umbrales pactados, por lo que no corresponde crédito de servicio ($0 CLP).

## 2. Resultado de `calc_sla.py`
```text
Servicio: Enlace Dedicado Base 100 Mbps | Periodo: 2026-07
--------------------------------------------------------------------------
Metrica            Objetivo       Medido         Veredicto             
--------------------------------------------------------------------------
disponibilidad     >= 99.9 %      99.94 %        CUMPLE                
latencia           <= 30.0 ms     21.50 ms       CUMPLE                
jitter             <= 10.0 ms     4.20 ms        CUMPLE                
perdida            <= 0.5 %       0.12 %         CUMPLE                
throughput         >= 90.0 Mbps   93.50 Mbps     CUMPLE                
--------------------------------------------------------------------------
Credito calculado : 0% = 0% (Tope: 50%)
Credito aplicable : 0% -> $0 CLP neto
