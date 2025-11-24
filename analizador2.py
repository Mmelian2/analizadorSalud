# analizador.py

def evaluar_inmediatos(datos):
    resultados = {}

    # Ejemplo LDL
    ldl = datos["ldl"]
    if ldl < 100:
        estado = "Normal/Óptimo"
    elif ldl < 160:
        estado = "Moderado"
    else:
        estado = "Alto"

    resultados["ldl"] = {
        "valor": ldl,
        "estado": estado
    }

    # Glucosa
    glu = datos["glucosa"]
    if glu < 100:
        estado = "Normal"
    elif glu < 125:
        estado = "Pre-Diabetes"
    else:
        estado = "Diabetes"

    resultados["glucosa"] = {
        "valor": glu,
        "estado": estado
    }

    # Hemoglobina
    hb = datos["hemoglobina"]
    if hb < 12:
        estado = "Baja"
    elif hb <= 16:
        estado = "Normal"
    else:
        estado = "Alta"

    resultados["hemoglobina"] = {
        "valor": hb,
        "estado": estado
    }

    return resultados



def proyectar_riesgo_largo_plazo(datos):
    proyecciones = {}

    def escalar(val, minimo, maximo):
        
        if val < minimo: val = minimo
        if val > maximo: val = maximo
        return round(((val - minimo) / (maximo - minimo)) * 100, 1)

    proyecciones["ldl"] = escalar(datos["ldl"], 50, 200)
    proyecciones["glucosa"] = escalar(datos["glucosa"], 70, 200)
    proyecciones["hemoglobina"] = escalar(datos["hemoglobina"], 10, 18)

    return proyecciones



def analizar(datos):
    inmediatos = evaluar_inmediatos(datos)
    proyecciones = proyectar_riesgo_largo_plazo(datos)

    return {
        "resultados_inmediatos": inmediatos,
        "proyecciones": proyecciones
    }
