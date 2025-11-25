# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from analizador import AnalizadorSalud
from paciente import Paciente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.json
    
    # Obtener datos del request
    sexo = data.get('sexo')
    valores = data.get('valores')
    
    # Crear paciente y analizador
    es_hombre = sexo == 'M'
    paciente = Paciente("Paciente", "Test", 30, es_hombre, valores)
    analizador = AnalizadorSalud(es_hombre=es_hombre)
    
    # Ejecutar análisis
    paciente.analizar(analizador)
    
    # Calcular proyecciones a 12, 24 y 60 meses
    proyecciones = paciente.proyeccion_riesgo(analizador, plazos=[12, 24, 60])
    
    # Preparar respuesta
    response = {
        'resultados': paciente.resultados,
        'proyecciones': proyecciones,
        'parametros': paciente.parametros
    }
    
    return jsonify(response)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)