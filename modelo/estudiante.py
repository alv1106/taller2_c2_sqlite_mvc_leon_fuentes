import sqlite3

class CrearBase:
    def crear_base(nombre_bd: str = "estudiantes.db") -> None:
        """
        Crea una base de datos SQLite con la tabla 'estudiantes'.
        :param nombre_bd: nombre del archivo de base de datos.
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
    def insertar_estudiante(nombre, correo, nota, nombre_bd="estudiantes.db"):
        """Inserta un nuevo registro en la tabla estudiantes."""
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)", (nombre, correo, nota))
        conn.commit()
        conn.close()

class listar:
    def listar_estudiantes(nombre_bd="estudiantes.db"):
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes")
        datos = cur.fetchall()
        conn.close()
        return datos
        
class consultar:
    def consultar_estudiantes(umbral: float = 4.0, nombre_bd: str = "estudiantes.db") -> None:
        """
        Muestra en consola los estudiantes con nota mayor o igual al umbral.
        :param umbral: nota mínima de filtro.
        :param nombre_bd: base de datos SQLite a consultar.
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
    def actualizar_nota(nombre, nueva_nota, nombre_bd="estudiantes.db"):
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("UPDATE estudiantes SET nota=? WHERE nombre=?", (nueva_nota, nombre))
        conn.commit()
        conn.close()

class Eliminar:
    def eliminar_estudiante(nombre, nombre_bd="estudiantes.db"):
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("DELETE FROM estudiantes WHERE nombre=?", (nombre,))
        conn.commit()
        conn.close()

class Buscar:
    def buscar_por_nombre(cadena, nombre_bd="estudiantes.db"):
        """Busca coincidencias parciales en el nombre (LIKE)."""
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ('%' + cadena + '%',))
        datos = cur.fetchall()
        conn.close()
        return datos
    
class PromedioBajo:
    def eliminar_bajo_promedio(nombre_bd="estudiantes.db"):
        """
        Elimina todos los registros cuya nota sea menor a 3.0.
        SQL: DELETE FROM estudiantes WHERE nota < 3.0
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("DELETE FROM estudiantes WHERE nota < 3.0")
        conn.commit()
        conn.close()
        print("[OK] Registros con nota menor a 3.0 eliminados.")

class PromedioAlto:
    def eliminar_bajo_promedio(nombre_bd="estudiantes.db"):
        """
        Elimina todos los registros cuya nota sea menor a 3.0.
        SQL: DELETE FROM estudiantes WHERE nota < 3.0
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("DELETE FROM estudiantes WHERE nota > 3.0")
        conn.commit()
        conn.close()
        print("[OK] Registros con nota mayor a 3.0 eliminados.")

class JerarquiaNotas:
    def ordenar_por_nota(nombre_bd="estudiantes.db"):
        """
        Devuelve los estudiantes ordenados por nota descendente.
        SQL: SELECT * FROM estudiantes ORDER BY nota DESC
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()
        cur.execute("SELECT * FROM estudiantes ORDER BY nota DESC")
        datos = cur.fetchall()
        conn.close()
        return datos