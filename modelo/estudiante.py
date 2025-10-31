import sqlite3


class CrearBase:
    """Clase responsable de la inicializacion de la base de datos"""

    def crear_base(nombre_bd: str = "estudiantes.db") -> None:

        """
        Crea o verifica la existencia de la base de datos

        Args:
            nombre_bd (str): Nombre del archivo de base de datos a crear
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                nota REAL
            )
        """)
        conn.commit()
        conn.close()
        print(f"[OK] Base de datos {nombre_bd} creada y lista para uso.")


class Insertar:


    """
    Clase para operaciones de inserción de nuevos registros
    """

    def insertar_estudiante(nombre, correo, nota, nombre_bd="estudiantes.db"):
        """
        Inserta un nuevo registro de estudiante en la tabla.

        Args:
            nombre (str): Nombre del estudiante.
            correo (str): Correo electrónico (debe ser único).
            nota (float): Nota del estudiante.
            nombre_bd (str, optional): Nombre del archivo de base de datos.
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)", (nombre, correo, nota))
        conn.commit()
        conn.close()


class listar:


    """
    consulta de todos los registros
    """

    def listar_estudiantes(nombre_bd="estudiantes.db"):
        """
        muestra todos los registros de la tabla

        Args:
            nombre_bd (str, optional): Nombre del archivo de base de datos

        Returns:
            list: Una lista con todos los datos de los estudiantes
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes")
        datos = cur.fetchall()
        conn.close()
        return datos


class consultar:


    """

    Consulta y filtro de estudiantes por nota.
    
    """

    def consultar_estudiantes(umbral: float = 4.0, nombre_bd: str = "estudiantes.db") -> None:
        """
        Muestra en consola los estudiantes con nota mayor o igual ala condicion

        Args:
            umbral (float, optional): Nota minima de filtro.
            nombre_bd (str, optional): Base de datos a evaluar
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()

        cur.execute("SELECT nombre, nota FROM estudiantes WHERE nota >= ?", (umbral,))
        resultados = cur.fetchall()

        print(f"\n[INFO] Estudiantes con nota >= {umbral}")
        print("--------------------------------------")
        for nombre, nota in resultados:
            print(f"{nombre:10s} | {nota:.2f}")

        conn.close()


class Actualizar:

    """
    Modificación de registros
    """
    def actualizar_nota(nombre, nueva_nota, nombre_bd="estudiantes.db"):

        """
        Actualiza la nota de un estudiante especifico basandose en su nombre

        Args:
            nombre (str): Nombre del estudiante cuya nota se desea actualizar
            nueva_nota (float): nuevo valor de nota a asignar
            nombre_bd (str, optional): Nombre del archivo de base de datos
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("UPDATE estudiantes SET nota=? WHERE nombre=?", (nueva_nota, nombre))
        conn.commit()
        conn.close()


class Eliminar:

    """
    eliminacion de un registro por su nombre
    """
    def eliminar_estudiante(nombre, nombre_bd="estudiantes.db"):

        """
        Elimina un estudiante

        Args:
            nombre (str): Nombre del estudiante a eliminar
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("DELETE FROM estudiantes WHERE nombre=?", (nombre,))
        conn.commit()
        conn.close()


class Buscar:

    """
    busqueda de registros usando cierta cadena de caracteres
    """

    def buscar_por_nombre(cadena, nombre_bd="estudiantes.db"):

        """
        Busca coincidencias parciales con cierta palabra letra

        Args:
            cadena (str): Subcadena de texto a buscar dentro de los nombres
            nombre_bd (str, optional): Nombre del archivo de base de datos

        Returns:
            list: Una lista con los estudiantes que coinciden con la busqueda
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ('%' + cadena + '%',))
        datos = cur.fetchall()
        conn.close()
        return datos
    

class PromedioBajo:

    """
    Clase para la eliminacion rapida de estudiantes
    """

    def eliminar_bajo_promedio(nombre_bd="estudiantes.db"):

        """
        Elimina todos los registros cuya nota sea menor a 3.0

        Args:
            nombre_bd (str, optional): Nombre del archivo de base de datos
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("DELETE FROM estudiantes WHERE nota < 3.0")
        conn.commit()
        conn.close()
        print("[OK] Registros con nota menor a 3.0 eliminados.")


class PromedioAlto:

    """
    Clase para la eliminacion rapida de estudiantes
    """
    def eliminar_bajo_promedio(nombre_bd="estudiantes.db"):

        """
        Elimina todos los registros cuya nota sea mayor a 3.0.

        Args:
            nombre_bd (str, optional): Nombre del archivo de base de datos
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("DELETE FROM estudiantes WHERE nota > 3.0")
        conn.commit()
        conn.close()
        print("[OK] Registros con nota mayor a 3.0 eliminados.")


class JerarquiaNotas:

    """
    listados de estudiantes ordenados por nota
    """
    def ordenar_por_nota(nombre_bd="estudiantes.db"):

        """
        Devuelve los estudiantes ordenados por nota de forma descendente (de mayor a menor)

        Args:
            nombre_bd (str, optional): Nombre del archivo de base de datos

        Returns:
            list: Una lista con los estudiantes, ordenados por nota
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes ORDER BY nota DESC")
        datos = cur.fetchall()
        conn.close()
        return datos


