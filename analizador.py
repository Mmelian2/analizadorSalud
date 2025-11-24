import math
from typing import Dict, Any

class AnalizadorSalud:
    """
    Clase para analizar parámetros de salud (análisis de sangre) y detectar
    riesgos inmediatos o proyectar riesgos a largo plazo basados en rangos
    de referencia específicos por sexo.

    Parámetros base analizados: Glucosa, Colesterol LDL y Hemoglobina.
    """

    def __init__(self, es_hombre: bool):
        """
        Inicializa el analizador con los rangos de referencia médica,
        dependiendo del sexo del paciente.

        :param es_hombre: True si el paciente es hombre, False si es mujer.
        """
        self.es_hombre = es_hombre
        # RANGOS MÉDICOS NORMALES Y DE RIESGO (valores en mg/dL o g/dL)
        # Glucosa: Normal < 100, Prediabetes 100-125, Diabetes >= 126
        # Colesterol LDL: Óptimo < 100, Alto >= 160
        # Hemoglobina (g/dL): Hombres 13.2-16.6, Mujeres 11.6-15.0

        self.rangos = {
            'Glucosa': {'Normal': 100.0, 'Prediabetes': 126.0},
            'Colesterol_LDL': {'Normal': 100.0, 'Alto': 160.0},
            'Hemoglobina': {
                'Min_Normal': 13.2 if es_hombre else 11.6,
                'Max_Normal': 16.6 if es_hombre else 15.0
            }
        }

    def _evaluar_glucosa(self, valor: float) -> str:
        """
        Evalúa el riesgo de Glucosa.
        :param valor: Nivel de Glucosa en mg/dL.
        :return: Clasificación de riesgo.
        """
        if valor < self.rangos['Glucosa']['Normal']:
            return "Normal"
        elif valor < self.rangos['Glucosa']['Prediabetes']:
            return "Riesgo: Prediabetes"
        else:
            return "Riesgo Alto: Posible Diabetes"

    def _evaluar_colesterol(self, valor: float) -> str:
        """
        Evalúa el nivel de Colesterol LDL (el "malo").
        :param valor: Nivel de Colesterol LDL en mg/dL.
        :return: Clasificación de riesgo.
        """
        if valor < self.rangos['Colesterol_LDL']['Normal']:
            return "Normal/Óptimo"
        elif valor < self.rangos['Colesterol_LDL']['Alto']:
            return "Riesgo: Ligeramente Elevado"
        else:
            return "Riesgo Alto: Colesterol Elevado"

    def _evaluar_hemoglobina(self, valor: float) -> str:
        """
        Evalúa el nivel de Hemoglobina (deficiencia -> anemia).
        :param valor: Nivel de Hemoglobina en g/dL.
        :return: Clasificación de riesgo.
        """
        min_n = self.rangos['Hemoglobina']['Min_Normal']
        max_n = self.rangos['Hemoglobina']['Max_Normal']

        if valor < min_n:
            return "Riesgo Alto: Anemia por Deficiencia"
        elif valor > max_n:
            return "Riesgo: Posible Policitemia (Muy Alto)"
        else:
            return "Normal"

    def deteccion_riesgo_inmediato(self, parametros: Dict[str, float]) -> Dict[str, str]:
        """
        Calcula el riesgo de enfermedad comparando los parámetros con rangos normales.
        Este resultado se utiliza para la 'Presentación de Resultados Inmediatos' (Tarea 2).

        :param parametros: Diccionario con los resultados del paciente
                           (ej: {'Glucosa': 115, 'Colesterol_LDL': 150, 'Hemoglobina': 10.5}).
        :return: Diccionario con la evaluación de riesgo por cada parámetro.
        """
        resultados: Dict[str, str] = {}

        if 'Glucosa' in parametros:
            resultados['Glucosa'] = self._evaluar_glucosa(parametros['Glucosa'])

        if 'Colesterol_LDL' in parametros:
            resultados['Colesterol_LDL'] = self._evaluar_colesterol(parametros['Colesterol_LDL'])

        if 'Hemoglobina' in parametros:
            resultados['Hemoglobina'] = self._evaluar_hemoglobina(parametros['Hemoglobina'])

        return resultados

    def proyeccion_riesgo_exponencial(self, valor_inicial: float, valor_referencia: float, tiempo_meses: int) -> float:
        """
        Proyecta un Índice de Riesgo (0.0 a 100.0) a largo plazo si la desviación
        actual respecto al valor de referencia persiste, utilizando un modelo
        exponencial de crecimiento.

        Este modelo es análogo a la fórmula N(t) = N0 * 2^(t/tau), donde el riesgo
        crece exponencialmente con el tiempo 't'.

        :param valor_inicial: El valor actual del parámetro.
        :param valor_referencia: El valor ideal (ej: mínimo normal de Hemoglobina).
        :param tiempo_meses: Horizonte de tiempo para la proyección (ej: 60 meses para 5 años).
        :return: Un índice de riesgo proyectado (0.0 a 100.0).
        """
        # 1. Calcular la Desviación (Deficiencia/Exceso)
        desviacion = abs(valor_inicial - valor_referencia)

        if desviacion == 0:
            return 0.0

        # 2. Calcular la Constante de Riesgo 'k' (determina la velocidad de crecimiento)
        # Se usa logaritmo para que la desviación no linealice el riesgo de forma excesiva.
        constante_riesgo_k = 0.1 * math.log(desviacion + 1)

        # 3. Aplicar el modelo exponencial: Riesgo(t) = Desviacion * e^(k * tiempo)
        # (Similar a N(t) = N0 * e^(kt), donde Desviación es N0)
        riesgo_proyectado = desviacion * math.exp(constante_riesgo_k * (tiempo_meses / 12)) # Ajustamos el tiempo en AÑOS para el crecimiento

        # 4. Normalización a índice de 0 a 100 (ajuste para visibilidad en el reporte)
        riesgo_normalizado = min(riesgo_proyectado * 5, 100.0) # Se ajusta el multiplicador a 5 para un rango más visible.

        return riesgo_normalizado