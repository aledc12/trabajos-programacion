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
#
# Funciones que debes implementar:
#   - crear_tarea(descripcion, prioridad)
#   - añadir_tarea(tareas, descripcion, prioridad)
#   - marcar_completada(tareas, indice)
#   - eliminar_tarea(tareas, indice)
#   - obtener_tareas_pendientes(tareas)
#   - obtener_tareas_completadas(tareas)
# ================================================

descripcion= "a"
prioridad= 0
completada= False
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
        "Completada": False
    }
    pass


def añadir_tarea(tareas, descripcion, prioridad):
    """
    Debe añadir una nueva tarea (usando crear_tarea)
    a la lista 'tareas'.
    """
    tarea = crear_tarea(descripcion,prioridad)
    tareas.append(tarea)
    pass


def marcar_completada(tareas, indice):
    """
    Debe cambiar el valor 'completada' a True
    para la tarea en la posición 'indice'.
    """
    tareas[indice]["Completada"]= True
    pass


def eliminar_tarea(tareas, indice):
    """
    Debe eliminar la tarea que está en la posición 'indice'
    dentro de la lista 'tareas'.
    """
    tareas.pop(indice)
    pass


def obtener_tareas_pendientes(tareas):
    """
    Debe devolver una lista de tareas cuyo campo 'completada' sea False.
    """
    return[tarea for tarea in tareas if not tarea["Completada"]]
    pass


def obtener_tareas_completadas(tareas):
    """
    Debe devolver una lista de tareas cuyo campo 'completada' sea True.
    """
    return[tarea for tarea in tareas if tarea["Completada"]]
    pass