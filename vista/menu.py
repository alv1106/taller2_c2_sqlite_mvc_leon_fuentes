"""
La comunicacion dentro del programa la pensamos primero vista(main), tan le pide
x cosa, entonces ejecuta cierta funcion de controlador(gestor), entonces gestor
dice a abueno quieren hacer esta accion, que parametro o condicion necesita etc.
una vez hecho esto dice a bueno todo correcto, y ejecuta la funcion de 
modelo(estudiante), esta es quien dice a bueno tengo estos datos, o tengo que hacer
tal cosa con estos datos, listo lo borro dela base de datos, agrego etc, asi es como
se da el flujo y comunicacion ajajja.
Cuando pensamos el ejercicio fue asi como lo pensamos, pero creemos que quizas gestor
no se diferencia lo suficiente de estudiante, podriamos plantiar las clases de otra
forma.
Teniamos un error persistente en el que era como que main no encontraba a gestor o
estudiantes, es por ello si se fija, cambiamos poco el orden poniendo todo en vista,
gracia a ello se arreglo el error.

"""

from controlador.gestor import (
    Crea,
    Agregar,
    Mostrar,
    Consulta,
    Actualizar,
    Eliminar,
    Promedio,
    Buscar,
    Orden
)

def mostrar_menu():
    print("---  Gestor Estudiantes  ---")
    print("1. Crear base de datos")
    print("2. Agregar estudiante")
    print("3. Listar estudiantes")
    print("4. Consultar por nota minima")
    print("5. Actualizar nota")
    print("6. Eliminar estudiante por nombre")
    print("7. Eliminar estudiantes con nota < 3.0")
    print("8. Eliminar estudiantes con nota > 3.0")
    print("9. Buscar estudiante por una cadena de texto")
    print("10. Mostrar estudiantes ordenados por nota descendente")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opcion invalida ingrese un numero")
            continue

        if opcion == 1:
            Crea.crear_base()

        elif opcion == 2:
            Agregar.agregar_estudiante()

        elif opcion == 3:
            Mostrar.listar_estudiantes()

        elif opcion == 4:
            Consulta.consultar()

        elif opcion == 5:
            Actualizar.actualizar_nota()

        elif opcion == 6:
            Eliminar.eliminar_estudiante()

        elif opcion == 7:
            Promedio.eliminar_promedio_bajo()

        elif opcion == 8:
            Promedio.eliminar_promedio_alto()

        elif opcion == 9:
            Buscar.buscar_estudiante()

        elif opcion == 10:
            Orden.mostrar_ordenados()

        elif opcion == 0:
            print("Saliendo del sistema")
            break

        else:
            print("Opción no valida, intente nuevamente")