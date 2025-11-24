from analizador import AnalizadorSalud
from paciente import Paciente
from validacion import mostrar_informe, pedir_opcion, pedir_sexo, pedir_valores
from data import PACIENTES

def menu():
    while True:
        print("\n--- ANALIZADOR DE SALUD ---")
        print("1. Ingresar valores")
        print("2. Paciente saludable")
        print("3. Paciente intermedio")
        print("4. Paciente de riesgo")
        print("5. Salir")

        op = pedir_opcion()

        if op == "5":
            print("Saliendo...")
            break

        if op == "1":
            sexo = pedir_sexo()
            valores = pedir_valores()
            nombre = "Paciente"

        elif op in ["2", "3", "4"]:
            clave = ["saludable", "intermedio", "riesgo"][int(op)-2]
            data = PACIENTES[clave]
            sexo = data["sexo"]
            valores = data["valores"]
            nombre = clave.capitalize()

        else:
            print("Opción inválida.")
            continue


        # Crear el paciente
        paciente = Paciente(nombre, "Test", 30, sexo == "M", valores)

        analizador = AnalizadorSalud(es_hombre=paciente.es_hombre)

        # Ejecutar análisis
        paciente.analizar(analizador)
        proyecciones = paciente.proyeccion_riesgo(analizador)

        # Mostrar informe
        mostrar_informe(
            paciente.nombre,
            sexo,
            paciente.parametros,
            paciente.resultados,
            analizador
        )

if __name__ == "__main__":
    menu()