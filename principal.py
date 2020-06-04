from controlador import Controlador


if __name__ == "__main__":
    print('Gestión de estudiantes')

    controlador = Controlador()
    
    while True:
        print()
        print('Seleccione una opción')
        print('a. Agregar estudiante')
        print('b. Mostrar estudiantes por código')
        print('c. Mostrar estudiantes por nombre')
        print('d. Eliminar estudiante')
        print('e. Salir')
        print()
        opcion = input('Opción: ')

        if not opcion in ['a', 'b', 'c', 'd', 'e']:
            print('Opción incorrecta, por favor intente de nuevo.')

        if opcion == 'a':
            controlador.agregar_estudiante()

        if opcion == 'b':
            controlador.mostrar_estudiantes_codigo()

        if opcion == 'c':
            controlador.mostrar_estudiantes_nombre()

        if opcion == 'd':
            controlador.eliminar_estudiante()

        if opcion == 'e':
            print('Salir')
            break
