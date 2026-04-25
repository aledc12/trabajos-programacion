# storage_sqlite.py
# =================================================
# Este archivo se encarga de la persistencia de datos usando SQLite.
# Proporciona funciones para crear la base de datos,
# conectarse a ella y realizar operaciones de lectura/escritura.
#
# Funciones a implementar:
#   - crear_bbdd() - Crear la base de datos y tablas si no existen
#   - conectar_bbdd() - Conectar a la base de datos
#   - obtener_conexion() - Obtener conexión activa
#
# IMPORTANTE:
#   Este módulo coexistirá con storage.py (JSON) durante la transición
#   hacia persistencia basada en SQLite.
# =================================================

import sqlite3
import os
from datetime import datetime


DATABASE_FILE = "tareas.db"


def crear_bbdd():
    """
    Crea la base de datos SQLite y la tabla de tareas si no existen.
    """
    conexion = sqlite3.connect(DATABASE_FILE)
    cursor = conexion.cursor()
    
    # Crear tabla de tareas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            prioridad INTEGER,
            completada BOOLEAN DEFAULT 0,
            fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conexion.commit()
    conexion.close()
    print(f"Base de datos '{DATABASE_FILE}' creada/verificada correctamente.")


def conectar_bbdd():
    """
    Conecta a la base de datos SQLite.
    Retorna la conexión.
    """
    conexion = sqlite3.connect(DATABASE_FILE)
    conexion.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    return conexion


def obtener_conexion():
    """
    Obtiene una conexión activa a la base de datos.
    Asegura que la BD existe antes de conectar.
    """
    if not os.path.exists(DATABASE_FILE):
        crear_bbdd()
    return conectar_bbdd()


def obtener_tareas():
    """
    Obtiene todas las tareas almacenadas en la base de datos.
    Retorna una lista de diccionarios representando cada tarea.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tareas ORDER BY prioridad ASC")
    filas = cursor.fetchall()
    
    tareas = []
    for fila in filas:
        fecha_texto = fila["fecha_creacion"]
        fecha_obj = datetime.strptime(fecha_texto, "%Y-%m-%d %H:%M:%S")

        tareas.append({
            "id": fila["id"],
            "descripcion": fila["descripcion"],
            "prioridad": fila["prioridad"],
            "completada": bool(fila["completada"]),
            "fecha": fecha_obj 
        })
    conexion.close()
    return tareas

def obtener_tareas_pendientes():
    """
    Obtiene todas las tareas pendientes (completada = False).
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tareas WHERE completada = 0 ORDER BY prioridad ASC")
    filas = cursor.fetchall()
    
    tareas = []
    for fila in filas:
        fecha_texto = fila["fecha_creacion"]
        fecha_obj = datetime.strptime(fecha_texto, "%Y-%m-%d %H:%M:%S")

        tarea = {
            "id": fila["id"],
            "descripcion": fila["descripcion"],
            "prioridad": fila["prioridad"],
            "completada": bool(fila["completada"]),
            "fecha": fecha_obj 
        }
        tareas.append(tarea)
    
    conexion.close()
    return tareas

def obtener_tareas_completadas():
    """
    Obtiene todas las tareas completadas (completada = True).
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM tareas WHERE completada = 1 ORDER BY prioridad ASC")
    filas = cursor.fetchall()
    
    tareas = []
    for fila in filas:
        fecha_texto = fila["fecha_creacion"]
        fecha_obj = datetime.strptime(fecha_texto, "%Y-%m-%d %H:%M:%S")

        tarea = {
            "id": fila["id"],
            "descripcion": fila["descripcion"],
            "prioridad": fila["prioridad"],
            "completada": bool(fila["completada"]),
            "fecha": fecha_obj
        }
        tareas.append(tarea)
    
    conexion.close()
    return tareas

def añadir_tarea_bd(descripcion, prioridad):
    """
    Añade una nueva tarea a la base de datos.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute(
        "INSERT INTO tareas (descripcion, prioridad, completada) VALUES (?, ?, 0)",
        (descripcion, prioridad)
    )
    
    conexion.commit()
    conexion.close()


def marcar_completada_bd(tarea_id):
    """
    Marca una tarea como completada en la base de datos.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (tarea_id,))
    
    conexion.commit()
    conexion.close()


def eliminar_tarea_bd(tarea_id):
    """
    Elimina una tarea de la base de datos.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
    
    conexion.commit()
    conexion.close()


# Inicializar la BD al importar el módulo
if __name__ != "__main__":
    crear_bbdd()