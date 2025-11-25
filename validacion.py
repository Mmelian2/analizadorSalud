
def mostrar_informe(nombre, sexo, valores, resultados, analizador):
    print("\n==============================================")
    print(f"           INFORME DE LABORATORIO - {nombre}")
    print("==============================================")
    print(f"Sexo: {'Hombre' if sexo == 'M' else 'Mujer'}\n")

    riesgo_total = 0  # Para calcular riesgo general

    print(f"{'Parámetro':<15} {'Valor':<10} {'Interpretación':<35} {'Proyección 5 años':<15}")
    print("-" * 80)
    for k in valores:
        valor = valores[k]
        interpretacion = resultados[k]

        # Proyección a 5 años
        ref = analizador.rangos[k]['Normal'] if k != 'Hemoglobina' else analizador.rangos[k]['Min_Normal']
        riesgo = analizador.proyeccion_riesgo_exponencial(valor, ref, 60)

        riesgo_total += riesgo
        print(f"{k:<15} {valor:<10} {interpretacion:<35} {riesgo:.1f}/100")

    riesgo_general = riesgo_total / len(valores)
    print("-" * 80)
    print(f"{'Riesgo General del Paciente':<60}: {riesgo_general:.1f}/100")
    print("==============================================\n")

def pedir_sexo():
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            return sexo
        print("Entrada inválida. Escribí M o F.")

def pedir_numero(mensaje: str, minimo: float = 0.1, maximo: float = 500.0) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo or valor > maximo:
                print(f"Valor fuera de rango permitido ({minimo} - {maximo}). Intentá de nuevo.")
                continue
            return valor
        except ValueError:
            print("Debes ingresar un número válido.")

def pedir_valores():
    print("\n--- Ingresar valores del paciente ---")

    glucosa = pedir_numero("Glucosa (mg/dL): ", minimo=40, maximo=400)
    ldl = pedir_numero("Colesterol LDL (mg/dL): ", minimo=40, maximo=350)
    hb = pedir_numero("Hemoglobina (g/dL): ", minimo=5, maximo=20)

    return {
        "Glucosa": glucosa,
        "Colesterol_LDL": ldl,
        "Hemoglobina": hb
    }

def pedir_opcion():
    while True:
        op = input("Elegí una opción (1-5): ").strip()
        if op in ["1", "2", "3", "4", "5"]:
            return op
        print("Opción inválida. Elegí del 1 al 5.")