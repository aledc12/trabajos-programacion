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
# IMPORTANTE: Madre mia no mu mal
#   main() debe contener el bucle principal
#   que permita al usuario interactuar hasta que elija salir.
# =================================================

from models import (
    obtener_tareas_pendientes,
    obtener_tareas_completadas
)

from storage_sqlite import (
    obtener_tareas,
    obtener_tareas_pendientes as obtener_tareas_pendientes_bd,
    obtener_tareas_completadas as obtener_tareas_completadas_bd,
    añadir_tarea_bd,
    marcar_completada_bd,
    eliminar_tarea_bd,
    obtener_conexion
)


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
    if not tareas:
        print("No hay tareas.")
        return
    
    for tarea in tareas:
        estado = "✓ Completada" if tarea.get("completada") else "○ Pendiente"
        print(f"  ID: {tarea.get('id')} | {tarea.get('descripcion')} | Prioridad: {tarea.get('prioridad')} | {estado}")


def main():
    """
    Bucle principal del programa.
    Aquí se inicializa la lista de tareas,
    se muestran opciones y se llaman funciones según la elección del usuario.
    """
    print("✓ Conectando a la base de datos...")
    obtener_conexion()  # Verifica/crea la BD
    print("✓ Base de datos preparada.\n")

    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige una opción: ")

        if opcion == 1:
            descripcion = input("Descripción de la tarea: ")
            prioridad = pedir_entero("Prioridad de la tarea (número): ")
            añadir_tarea_bd(descripcion, prioridad)
            print("✓ Tarea añadida correctamente.\n")

        elif opcion == 2:
            print("\n--- TAREAS PENDIENTES ---")
            tareas = obtener_tareas_pendientes_bd()
            mostrar_lista(tareas)

        elif opcion == 3:
            print("\n--- TAREAS COMPLETADAS ---")
            tareas = obtener_tareas_completadas_bd()
            mostrar_lista(tareas)

        elif opcion == 4:
            print("\n--- MARCAR TAREA COMO COMPLETADA ---")
            tareas = obtener_tareas_pendientes_bd()
            mostrar_lista(tareas)
            if tareas:
                tarea_id = pedir_entero("Introduce el ID de la tarea a marcar como completada: ")
                marcar_completada_bd(tarea_id)
                print("✓ Tarea marcada como completada.\n")

        elif opcion == 5:
            print("\n--- ELIMINAR TAREA ---")
            tareas = obtener_tareas()
            mostrar_lista(tareas)
            if tareas:
                tarea_id = pedir_entero("Introduce el ID de la tarea a eliminar: ")
                eliminar_tarea_bd(tarea_id)
                print("✓ Tarea eliminada correctamente.\n")

        elif opcion == 0:
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()


