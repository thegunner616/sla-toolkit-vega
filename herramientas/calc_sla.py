#!/usr/bin/env python3
import argparse
import csv
import sys
import yaml


def evaluar_operador(medido, operador, objetivo):
    if operador == ">=":
        return medido >= objetivo
    if operador == "<=":
        return medido <= objetivo
    if operador == ">":
        return medido > objetivo
    if operador == "<":
        return medido < objetivo
    raise ValueError(f"Operador no soportado: {operador}")


def calcular_credito_disponibilidad(valor_disp, tramos):
    for tramo in tramos:
        desde = float(tramo["desde"])
        hasta = float(tramo["hasta"])
        if desde <= valor_disp < hasta:
            return float(tramo["credito"])
    return 0.0


def main():
    parser = argparse.ArgumentParser(description="Calculadora de cumplimiento SLA y creditos")
    parser.add_argument("-o", "--objetivos", required=True, help="Ruta al archivo objetivos.yaml")
    parser.add_argument("-m", "--mediciones", required=True, help="Ruta al archivo mediciones.csv")
    args = parser.parse_args()

    with open(args.objetivos, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    minutos_periodo = float(cfg["minutos_periodo"])
    cobertura_minima = float(cfg.get("cobertura_minima", 0.90))
    cargo_mensual = float(cfg["cargo_mensual"])
    tope_credito = float(cfg["tope_credito"])
    credito_otras = float(cfg.get("credito_otras", 0.05))
    tramos_disp = cfg.get("creditos_disponibilidad", [])
    metricas_cfg = cfg["metricas"]

    datos = {}
    with open(args.mediciones, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            metrica = fila["metrica"].strip()
            valor_raw = fila["valor"].strip()
            cob = float(fila["cobertura"].strip()) if fila.get("cobertura") and fila["cobertura"].strip() else 1.0
            datos.setdefault(metrica, []).append((valor_raw, cob))

    print(f"Servicio: {cfg.get('servicio', 'N/A')} | Periodo: {cfg.get('periodo', 'N/A')}")
    print("-" * 74)
    print(f"{'Metrica':<18} {'Objetivo':<14} {'Medido':<14} {'Veredicto':<22}")
    print("-" * 74)

    credito_total = 0.0
    detalle_creditos = []

    for nombre, regla in metricas_cfg.items():
        operador = regla["operador"]
        objetivo = float(regla["objetivo"])
        unidad = regla.get("unidad", "")
        estadistico = regla.get("estadistico", "promedio")
        aplica_credito = regla.get("aplica_credito", True)
        obj_str = f"{operador} {objetivo} {unidad}".strip()

        if nombre == "disponibilidad":
            caidas = datos.get("caida_atribuible", [])
            total_caida = sum(float(v) for v, _ in caidas)
            medido = ((minutos_periodo - total_caida) / minutos_periodo) * 100.0
            cumple = evaluar_operador(medido, operador, objetivo)
            veredicto = "CUMPLE" if cumple else "NO CUMPLE"
            med_str = f"{medido:.2f} {unidad}".strip()
            print(f"{nombre:<18} {obj_str:<14} {med_str:<14} {veredicto:<22}")
            if not cumple:
                cred = calcular_credito_disponibilidad(medido, tramos_disp)
                credito_total += cred
                detalle_creditos.append(f"{int(round(cred * 100))}% (disponibilidad)")
            continue

        registros = datos.get(nombre, [])
        if not registros:
            print(f"{nombre:<18} {obj_str:<14} {'N/D':<14} {'EVIDENCIA INSUFICIENTE':<22}")
            continue

        min_cob = min(c for _, c in registros)
        if min_cob < cobertura_minima or any(v.upper() == "INSUFICIENTE" for v, _ in registros):
            print(f"{nombre:<18} {obj_str:<14} {'Cob < 90%':<14} {'EVIDENCIA INSUFICIENTE':<22}")
            continue

        valores = [float(v) for v, _ in registros]
        if estadistico == "maximo":
            medido = max(valores)
        elif estadistico == "suma":
            medido = sum(valores)
        else:
            medido = sum(valores) / len(valores)

        cumple = evaluar_operador(medido, operador, objetivo)
        veredicto = "CUMPLE" if cumple else "NO CUMPLE"
        med_str = f"{medido:.2f} {unidad}".strip()
        print(f"{nombre:<18} {obj_str:<14} {med_str:<14} {veredicto:<22}")

        if not cumple and aplica_credito:
            credito_total += credito_otras
            detalle_creditos.append(f"{int(round(credito_otras * 100))}% ({nombre})")

    print("-" * 74)
    credito_aplicado = min(credito_total, tope_credito)
    monto_pesos = int(round(credito_aplicado * cargo_mensual))
    desglose = " + ".join(detalle_creditos) if detalle_creditos else "0%"
    print(f"Credito calculado : {desglose} = {int(round(credito_total * 100))}% (Tope: {int(round(tope_credito * 100))}%)")
    print(f"Credito aplicable : {int(round(credito_aplicado * 100))}% -> ${monto_pesos:,} CLP neto".replace(",", "."))


if __name__ == "__main__":
    main()
