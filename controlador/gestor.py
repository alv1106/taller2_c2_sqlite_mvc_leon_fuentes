"""
Módulo: gestor.py
Controlador del sistema Gestor de Estudiantes.
Coordina la lógica entre la vista (menú) y las clases del modelo (estudiante.py).
"""

from controlador import estudiante 


class Crea:
    def crear_base():
        """Crea la base de datos y la tabla 'estudiantes'."""
        estudiante.CrearBase.crear_base()


class Agregar:
    def agregar_estudiante():
        """Solicita datos del usuario e inserta un nuevo estudiante."""
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        nota = float(input("Nota: "))
        estudiante.Insertar.insertar_estudiante(nombre, correo, nota)
        print("[OK] Estudiante agregado correctamente.")


class Mostrar:
    def listar_estudiantes():
        """Muestra todos los estudiantes registrados."""
        datos = estudiante.listar.listar_estudiantes()
        print("\n[INFO] Listado de estudiantes:")
        print("----------------------------------------")
        for fila in datos:
            print(f"{fila[0]} | {fila[1]:10s} | {fila[2]:20s} | Nota: {fila[3]:.2f}")

class Consulta:
    def consultar():
        """Consulta estudiantes con nota mayor o igual al valor dado."""
        umbral = float(input("Ingrese la nota mínima: "))
        estudiante.consultar.consultar_estudiantes(umbral)

class Actualizar:
    def actualizar_nota():
        """Actualiza la nota de un estudiante (UPDATE)."""
        nombre = input("Nombre del estudiante: ")
        nueva = float(input("Nueva nota: "))
        estudiante.Actualizar.actualizar_nota(nombre, nueva)
        print("[OK] Nota actualizada correctamente.")

class Eliminar:
    def eliminar_estudiante():
        """Elimina un estudiante por nombre (DELETE)."""
        nombre = input("Nombre del estudiante a eliminar: ")
        estudiante.Eliminar.eliminar_estudiante(nombre)
        print("[OK] Estudiante eliminado correctamente.")


class Promedio:
    def eliminar_promedio_bajo():
        """Elimina todos los estudiantes con nota menor a 3.0."""
        estudiante.PromedioBajo.eliminar_bajo_promedio()

    def eliminar_promedio_alto():
        """Elimina todos los estudiantes con nota mayor a 3.0."""
        estudiante.PromedioAlto.eliminar_bajo_promedio()

class Buscar:
    def buscar_estudiante():
        """Busca estudiantes cuyo nombre contenga una palabra (LIKE)."""
        cadena = input("Ingrese parte del nombre a buscar: ")
        resultados = estudiante.Buscar.buscar_por_nombre(cadena)
        if resultados:
            print("\n[INFO] Resultados de búsqueda:")
            print("-----------------------------------")
            for fila in resultados:
                print(f"{fila[1]:10s} | {fila[2]:20s} | Nota: {fila[3]:.2f}")
        else:
            print("No se encontraron coincidencias.")


class Orden:
    def mostrar_ordenados():
        """Muestra los estudiantes ordenados por nota descendente (ORDER BY)."""
        datos = estudiante.JerarquiaNotas.ordenar_por_nota()
        print("\n[INFO] Estudiantes ordenados por nota (DESC):")
        print("-----------------------------------------------")
        for fila in datos:
            print(f"{fila[1]:10s} | {fila[2]:20s} | Nota: {fila[3]:.2f}")