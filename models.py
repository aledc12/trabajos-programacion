# models.py
# ================================================
# Aquí irán las funciones relacionadas con la gestión interna de las tareas.
# NO se usan clases Solo listas y diccionarios.
# ola
# Cada tarea será un diccionario con la estructura:
# {
#     "descripcion": "texto",
#     "prioridad": numero,
#     "completada": True/False
# }
#Hello
# Funciones que debes implementar:
#   - crear_tarea(descripcion, prioridad)
#   - añadir_tarea(tareas, descripcion, prioridad)
#   - marcar_completada(tareas, indice)
#   - eliminar_tarea(tareas, indice)
#   - obtener_tareas_pendientes(tareas)
#   - obtener_tareas_completadas(tareas)
# ================================================

from datetime import date

def crear_tarea(descripcion, prioridad):
    
    """
    Debe devolver un diccionario que represente una tarea.
    - descripcion: texto
    - prioridad: número entero
    - completada: inicialmente False
    """

    return{
        "descripcion":descripcion,
        "prioridad": prioridad,
        "completada": False,
        "fecha": date.today()
    }


def añadir_tarea(tareas, descripcion, prioridad):
    """
    Debe añadir una nueva tarea (usando crear_tarea)
    a la lista 'tareas'.
    """
    tarea = crear_tarea(descripcion,prioridad)
    tareas.append(tarea)
    


def marcar_completada(tareas, indice):
    """
    Debe cambiar el valor 'completada' a True
    para la tarea en la posición 'indice'.
    """
    tareas[indice]["completada"]= True
    


def eliminar_tarea(tareas, indice):
    """
    Debe eliminar la tarea que está en la posición 'indice'
    dentro de la lista 'tareas'.
    """
    tareas.pop(indice)
    


def obtener_tareas_pendientes(tareas):
    """
    Debe devolver una lista de tareas cuyo campo 'completada' sea False.
    """
    pendientes = []

    for t in tareas:
        if t["completada"] == False:
            pendientes.append(t)

    return pendientes


def obtener_tareas_completadas(tareas):
    """
    Debe devolver una lista de tareas cuyo campo 'completada' sea True.
    """
    pendientes = []

    for t in tareas:
        if t["completada"] == True:
            pendientes.append(t)

    return pendientes