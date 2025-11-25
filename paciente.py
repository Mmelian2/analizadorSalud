# -*- coding: utf-8 -*-
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
        self.apellido = apellido
        self.edad = edad
        self.es_hombre = es_hombre
        self.parametros = parametros
        self.resultados: Dict[str, Any] = {}

    def analizar(self, analizador: AnalizadorSalud):
        """Analiza los parámetros del paciente usando el analizador."""
        self.resultados = analizador.deteccion_riesgo_inmediato(self.parametros)

    def proyeccion_riesgo(self, analizador: AnalizadorSalud, plazos: list = None):
        """
        Calcula proyecciones de riesgo para múltiples plazos.
        
        :param analizador: Instancia de AnalizadorSalud
        :param plazos: Lista de plazos en meses (por defecto: [12, 24, 60])
        :return: Diccionario con proyecciones por parámetro y plazo
        """
        if plazos is None:
            plazos = [12, 24, 60]  # 1 año, 2 años, 5 años
        
        proyecciones = {}
        
        for k, valor in self.parametros.items():
            # Obtener valor de referencia según el parámetro
            ref = analizador.rangos[k]['Normal'] if k != 'Hemoglobina' else analizador.rangos[k]['Min_Normal']
            
            # Calcular proyecciones para cada plazo
            for plazo in plazos:
                clave = f"{k}_{plazo}"
                proyecciones[clave] = analizador.proyeccion_riesgo_exponencial(valor, ref, plazo)
        
        return proyecciones