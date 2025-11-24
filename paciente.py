import math
from typing import Dict, Any
from analizador import AnalizadorSalud

class Paciente:
    def __init__(self, nombre: str, apellido: str, edad: int, es_hombre: bool, parametros: Dict[str, float]):
        """
        Inicializa un nuevo Paciente. Los parámetros deben incluir las claves
        Glucosa, Colesterol_LDL y Hemoglobina.
        """
        self.nombre = nombre
        self.apellido= apellido
        self.edad = edad
        self.es_hombre = es_hombre
        self.parametros = parametros
        self.resultados: Dict[str, Any] = {}


    def analizar(self, analizador : AnalizadorSalud):

        self.resultados = analizador.deteccion_riesgo_inmediato(self.parametros)


    def proyeccion_riesgo(self, analizador: AnalizadorSalud, tiempo_meses: int = 60):
        proyecciones = {}
        for k, valor in self.parametros.items():
            ref = analizador.rangos[k]['Normal'] if k != 'Hemoglobina' else analizador.rangos[k]['Min_Normal']
            proyecciones[k] = analizador.proyeccion_riesgo_exponencial(valor, ref, tiempo_meses)
        return proyecciones