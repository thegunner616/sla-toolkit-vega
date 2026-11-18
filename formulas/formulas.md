# Fórmulas de Cálculo y Verificación de SLA

## 1. Disponibilidad mensual ($A$)
- **Norma de origen:** ITU-T E.860 / ITU-T Y.1540.
- **Fórmula:**
  $$A = \left( \frac{T_{\text{total}} - T_{\text{caída\_atribuible}}}{T_{\text{total}}} \right) \times 100$$
- **Variables y unidades:**
  - $A$: Disponibilidad porcentual del período ($\%$).
  - $T_{\text{total}}$: Minutos totales del mes calendario ($\text{días} \times 1.440\text{ min}$).
  - $T_{\text{caída\_atribuible}}$: Suma de minutos de interrupciones atribuibles al proveedor ($\text{min}$). Las caídas excluidas por contrato se consideran tiempo disponible.
- **Ejemplo resuelto:** En un mes de 30 días ($43.200\text{ min}$) con $60\text{ min}$ de caída atribuible:
  $$A = \left( \frac{43.200 - 60}{43.200} \right) \times 100 = 99,86\%$$

## 2. Caída máxima permitida ($T_{\text{permitido}}$) y exceso
- **Norma de origen:** ITU-T E.860.
- **Fórmulas:**
  $$T_{\text{permitido}} = T_{\text{total}} \times \left( 1 - \frac{SLO_A}{100} \right)$$
  $$\text{Exceso} = T_{\text{caída\_atribuible}} - T_{\text{permitido}}$$
- **Variables y unidades:**
  - $SLO_A$: Disponibilidad objetivo comprometida ($\%$).
  - $T_{\text{permitido}}$: Tiempo máximo de indisponibilidad tolerado ($\text{min}$).
  - $\text{Exceso}$: Minutos por sobre el límite permitido ($\text{min}$).
- **Ejemplo resuelto:** Para $T_{\text{total}} = 43.200\text{ min}$ y $SLO_A = 99,9\%$:
  $$T_{\text{permitido}} = 43.200 \times (1 - 0,999) = 43,2\text{ min}$$
  Si hubo $60\text{ min}$ atribuibles, $\text{Exceso} = 60 - 43,2 = 16,8\text{ min}$.

## 3. Disponibilidad en serie ($A_{\text{serie}}$)
- **Norma de origen:** Ingeniería de confiabilidad / ITU-T Y.1541.
- **Fórmula:**
  $$A_{\text{serie}} = \prod_{i=1}^{n} A_i = A_1 \times A_2 \times \dots \times A_n$$
- **Variables y unidades:**
  - $A_i$: Disponibilidad individual de cada componente en serie expresada en proporción decimal ($0\text{ a }1$).
- **Ejemplo resuelto:** Enlace con CPE ($0,9995$), fibra ($0,9990$) y router PE ($0,9999$):
  $$A_{\text{serie}} = 0,9995 \times 0,9990 \times 0,9999 = 0,9984 \text{ (}99,84\%\text{)}$$

## 4. Disponibilidad en paralelo ($A_{\text{paralelo}}$)
- **Norma de origen:** Ingeniería de confiabilidad / ITU-T Y.1541.
- **Fórmula:**
  $$A_{\text{paralelo}} = 1 - \prod_{i=1}^{n} (1 - A_i)$$
- **Variables y unidades:**
  - $A_i$: Disponibilidad individual de cada ruta o equipo redundante en proporción decimal ($0\text{ a }1$).
  - $(1 - A_i)$: Indisponibilidad individual de cada rama.
- **Ejemplo resuelto:** Fibra principal ($0,9980$) respaldada en paralelo por radioenlace ($0,9950$):
  $$A_{\text{paralelo}} = 1 - (1 - 0,9980)(1 - 0,9950) = 1 - (0,0020 \times 0,0050) = 0,99999 \text{ (}99,999\%\text{)}$$

## 5. Throughput efectivo y eficiencia ($\eta$)
- **Norma de origen:** RFC 6349 (Framework for TCP Throughput Testing).
- **Fórmulas:**
  $$TH_{\text{prom}} = \frac{1}{N} \sum_{i=1}^{N} TH_i \qquad ; \qquad \eta = \left( \frac{TH_{\text{prom}}}{BW_{\text{contratado}}} \right) \times 100$$
- **Variables y unidades:**
  - $TH_i$: Resultado de cada prueba `iperf3` TCP válida ($\text{Mbps}$).
  - $N$: Número total de pruebas válidas en el período (adimensional).
  - $BW_{\text{contratado}}$: Ancho de banda nominal contratado ($\text{Mbps}$).
  - $\eta$: Eficiencia porcentual respecto al nominal ($\%$).
- **Ejemplo resuelto:** Enlace de $100\text{ Mbps}$ con 4 pruebas ($92, 90, 94, 92\text{ Mbps}$):
  $$TH_{\text{prom}} = \frac{92 + 90 + 94 + 92}{4} = 92,0\text{ Mbps} \quad ; \quad \eta = \frac{92,0}{100} \times 100 = 92,0\%$$

## 6. Pérdida de paquetes ($IPLR$)
- **Norma de origen:** ITU-T Y.1540 / RFC 7680 / RFC 5357.
- **Fórmula:**
  $$IPLR = \left( \frac{P_{\text{enviados}} - P_{\text{recibidos}}}{P_{\text{enviados}}} \right) \times 100$$
- **Variables y unidades:**
  - $IPLR$: Tasa de pérdida de paquetes IP ($\%$).
  - $P_{\text{enviados}}$: Total de paquetes de prueba transmitidos ($\text{paquetes}$).
  - $P_{\text{recibidos}}$: Total de paquetes recibidos correctamente ($\text{paquetes}$).
- **Ejemplo resuelto:** Si se envían $40.000$ paquetes TWAMP y llegan $39.920$:
  $$IPLR = \left( \frac{40.000 - 39.920}{40.000} \right) \times 100 = 0,20\%$$

## 7. Jitter (Variación de retardo, promedio ponderado)
- **Norma de origen:** RFC 3393 / ITU-T Y.1540 (IPDV).
- **Fórmulas:**
  $$J_k = |D_k - D_{k-1}| \qquad ; \qquad J_{\text{mensual}} = \frac{\sum_{i=1}^{m} (J_i \times n_i)}{\sum_{i=1}^{m} n_i}$$
- **Variables y unidades:**
  - $D_k$: Retardo unidireccional o RTT del paquete $k$ ($\text{ms}$).
  - $J_i$: Jitter promedio de la semana o subperíodo $i$ ($\text{ms}$).
  - $n_i$: Cantidad de muestras válidas en el subperíodo $i$ ($\text{muestras}$).
- **Ejemplo resuelto:** Semana 1 ($8,0\text{ ms}$ en $10.000$ muestras) y Semana 2 ($10,0\text{ ms}$ en $20.000$ muestras):
  $$J_{\text{mensual}} = \frac{(8,0 \times 10.000) + (10,0 \times 20.000)}{30.000} = 9,33\text{ ms}$$

## 8. Latencia física por distancia ($RTT_{\text{fibra}}$)
- **Norma de origen:** ITU-T G.114 / Física de propagación óptica.
- **Fórmula:**
  $$RTT_{\text{fibra}} = \frac{2 \times d}{v_p} = \frac{2 \times d}{c / n_{\text{fibra}}}$$
- **Variables y unidades:**
  - $d$: Distancia geográfica o longitud de traza de fibra ($\text{km}$).
  - $v_p$: Velocidad de propagación en fibra monomodo ($\approx 200.000\text{ km/s} = 200\text{ km/ms}$, con índice $n_{\text{fibra}} \approx 1,5$).
  - $RTT_{\text{fibra}}$: Tiempo mínimo físico de ida y vuelta ($\text{ms}$).
- **Ejemplo resuelto:** Enlace de fibra entre La Serena y Santiago ($d = 470\text{ km}$):
  $$RTT_{\text{fibra}} = \frac{2 \times 470\text{ km}}{200\text{ km/ms}} = 4,70\text{ ms}$$

## 9. Crédito de servicio ($C_{\text{total}}$)
- **Norma de origen:** ITU-T E.860 / Cláusulas de penalización contractual.
- **Fórmulas:**
  $$C_{\text{porcentaje}} = \min\left( C_{\text{disp}} + \sum C_{\text{otras}}, \; C_{\text{tope}} \right)$$
  $$\text{Monto}_{\text{crédito}} = \left( \frac{C_{\text{porcentaje}}}{100} \right) \times \text{Cargo}_{\text{mensual}}$$
- **Variables y unidades:**
  - $C_{\text{disp}}$: Porcentaje de crédito según tramo de disponibilidad ($\%$).
  - $C_{\text{otras}}$: Porcentaje fijo por cada métrica adicional incumplida ($\%$).
  - $C_{\text{tope}}$: Límite máximo de descuento mensual pactado ($\%$).
  - $\text{Cargo}_{\text{mensual}}$: Renta fija mensual neta del servicio ($\text{CLP}$).
- **Ejemplo resuelto:** Cargo mensual $\$1.000.000$, tramo disponibilidad $10\%$ más $5\%$ por latencia, con tope de $40\%$:
  $$C_{\text{porcentaje}} = \min(10\% + 5\%, 40\%) = 15\% \quad \Rightarrow \quad \text{Monto}_{\text{crédito}} = 0,15 \times 1.000.000 = \$150.000$$
