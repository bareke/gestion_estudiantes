import sqlite3
from sqlite3 import Error


class BaseDatos:
    nombre = 'base_datos.sqlite3'

    def __init__(self):
        self.crear_tabla()

    def obtener_conexion(self):
        try:
            conexion = sqlite3.connect(self.nombre)
            return conexion

        except Error:
            print(Error)

    def crear_tabla(self):
        conexion = self.obtener_conexion()
        cursor = conexion.cursor()
        consulta_sql = """
        CREATE TABLE IF NOT EXISTS Estudiante
        (
            codigo integer PRIMARY KEY,
            nombres text,
            apellidos text,
            edad integer
        )
        """
        cursor.execute(consulta_sql)
        conexion.commit()
    
    def consulta_registros(self, consulta_sql):
        conexion = self.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(consulta_sql)
        datos = cursor.fetchall()
        return datos
    
    def insertar_registro(self, consulta_sql, datos):
        conexion = self.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(consulta_sql, datos)
        conexion.commit()

    def eliminar_registro(self, consulta_sql):
        conexion = self.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(consulta_sql)
        conexion.commit()