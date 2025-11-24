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
    proyecciones = paciente.proyeccion_riesgo(analizador)
    
    # Preparar respuesta
    response = {
        'resultados': paciente.resultados,
        'proyecciones': proyecciones,
        'parametros': paciente.parametros
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)