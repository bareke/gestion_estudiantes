from estudiante import Estudiante
from base_datos import BaseDatos


class Controlador:

    def __init__(self):
        self.base_datos = BaseDatos()
    
    def agregar_estudiante(self):
        codigo = input('Dígite el código: ')
        nombres = input('Dígite los nombres: ')
        apellidos = input('Dígite los apellidos: ')
        edad = input('Dígite la edad: ')

        if not self.validar_codigo(codigo):
            if self.validar_edad(edad):
                estudiante = Estudiante(codigo, nombres, apellidos, edad)
                consulta_sql = """
                INSERT INTO Estudiante
                (
                    codigo,
                    nombres,
                    apellidos,
                    edad
                )
                VALUES(?, ?, ? ,?)
                """
                datos = (estudiante.codigo, estudiante.nombres, estudiante.apellidos, estudiante.edad)
                self.base_datos.insertar_registro(consulta_sql, datos)
                print()
                print('--------------------')
                print('Operación exitosa.')
            else:
                print('--------------------')
                print('Error, la edad no está comprendida entre 1 y 19 años.')
        else:
            print('--------------------')
            print('Error, el código ya existe.')
    
    def mostrar_estudiantes_codigo(self):
        consulta_sql = 'SELECT * FROM Estudiante ORDER BY codigo ASC'
        datos = self.base_datos.consulta_registros(consulta_sql)
        self.imprimir(datos)

    def mostrar_estudiantes_nombre(self):
        consulta_sql = 'SELECT * FROM Estudiante ORDER BY nombres ASC'
        datos = self.base_datos.consulta_registros(consulta_sql)
        self.imprimir(datos)
    
    def eliminar_estudiante(self):
        codigo = input('Dígite el codigo: ')
        if self.validar_codigo(codigo):
            consulta_sql = 'DELETE FROM Estudiante WHERE codigo = {}'.format(codigo)
            self.base_datos.eliminar_registro(consulta_sql)
            print()
            print('--------------------')
            print('Operación exitosa.')
        else:
            print('--------------------')
            print('Error, el código no existe.')        

    def imprimir(self, datos):
        print('--------------------')
        print('Estudiantes')
        for dato in datos:
            print(dato)
        print('--------------------')

    def validar_codigo(self, codigo):
        consulta_sql = 'SELECT * FROM Estudiante WHERE codigo ={}'.format(codigo)
        dato = self.base_datos.consulta_registros(consulta_sql)
        if dato:
            return True
        return False
    
    def validar_edad(self, edad):
        edad = int(edad)
        if 0 < edad < 20:
            return True
        return False