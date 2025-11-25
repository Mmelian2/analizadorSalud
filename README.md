# AnalizadorSalud 

## Descripción  
Este proyecto permite analizar datos de salud tales como glucosa, hemoglobina y colesterol. Está desarrollado en Python usando el micro-framework Flask, y fue ideado para ser una herramienta sencilla y clara para uso local o como base para un desarrollo más grande.  

## Tecnologías utilizadas  
- Python 3.x  
- Flask  
- Paquetes definidos en `requirements.txt`  
- Carpetas principales:  
  - `templates/` → para los archivos HTML de la interfaz  
  - Archivos principales en la raíz: `app.py`, `analizador.py`, `paciente.py`, `validacion.py`, `data.py`, etc.  
- Entorno virtual recomendado para manejar dependencias.

## Requisitos del entorno  
- Tener instalado Python 3 (recomendado: 3.9 o superior)  
- Tener instalado pip  
- Tener acceso a la terminal / consola  

## Instalación y puesta en marcha  

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/Mmelian2/analizadorSalud.git
   cd analizadorSalud
   
2. Crear y activar el entorno virtual
   En Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
  
  En Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
         
3. Instalar las dependencias
    ```bash
   pip install -r requirements.txt

4. Ejecutar la aplicación
   ```bash
   python app.py
