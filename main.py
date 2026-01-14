# main.py
# =================================================
# Este archivo se encarga de la interacción con el usuario.
# Aquí NO se gestiona la lógica: eso se hace en models.py.
# Tampoco se guarda/carga directamente: eso lo hace storage.py.
#
# Tareas principales:
#   - Crear el menú
#   - Leer opciones del usuario
#   - Llamar a las funciones de models y storage
#   - Mostrar las tareas por pantalla
#
# Funciones a implementar:
#   - mostrar_menu()
#   - pedir_entero(mensaje)
#   - mostrar_lista(tareas)
#   - main()
#
# IMPORTANTE:
#   main() debe contener el bucle principal
#   que permita al usuario interactuar hasta que elija salir.
# =================================================

from models import (
    añadir_tarea,
    marcar_completada,
    eliminar_tarea,
    obtener_tareas_pendientes,
    obtener_tareas_completadas
)

from storage import guardar_tareas, cargar_tareas


def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    pass


def pedir_entero(mensaje):
    """
    Pide al usuario un número entero.
    Si el usuario introduce algo incorrecto, debe repetirse hasta que sea válido.
    Usa try/except.
    """
    pass


def mostrar_lista(tareas):
    """
    Muestra por pantalla las tareas que reciba como lista.
    Debe incluir su índice y datos principales.
    """
    pass


def main():
    """
    Bucle principal del programa.
    Aquí se inicializa la lista de tareas,
    se muestran opciones y se llaman funciones según la elección del usuario.
    """
    pass


# Ejecutar el programa solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()


# main.py
# =================================================
# Interacción con el usuario
# =================================================

def main():
    """
    Bucle principal del programa.
    """
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opción: ")

        if opcion == 1:
            titulo = input("Título de la tarea: ")
            añadir_tarea(tareas, titulo)
            guardar_tareas(tareas)
            print("Tarea añadida.")

        elif opcion == 2:
            print("\n--- TAREAS PENDIENTES ---")
            pendientes = obtener_tareas_pendientes(tareas)
            mostrar_lista(pendientes)

        elif opcion == 3:
            print("\n--- TAREAS COMPLETADAS ---")
            completadas = obtener_tareas_completadas(tareas)
            mostrar_lista(completadas)

        elif opcion == 4:
            mostrar_lista(tareas)
            indice = pedir_entero("Índice de la tarea a completar: ")
            marcar_completada(tareas, indice)
            guardar_tareas(tareas)
            print("Tarea marcada como completada.")

        elif opcion == 5:
            mostrar_lista(tareas)
            indice = pedir_entero("Índice de la tarea a eliminar: ")
            eliminar_tarea(tareas, indice)
            guardar_tareas(tareas)
            print("Tarea eliminada.")

        elif opcion == 0:
            guardar_tareas(tareas)
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")


# Ejecutar el programa solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
