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


class importa:
    def importar_datos(csv_file: str, nombre_bd: str = "estudiantes.db") -> None:
        """
        Lee los datos de un archivo CSV e inserta los registros en la base de datos.
        :param csv_file: ruta del archivo CSV de entrada.
        :param nombre_bd: nombre del archivo de base de datos.
        """
        conn = sqlite3.connect(nombre_bd)
        cur = conn.cursor()

        with open(csv_file, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    cur.execute(
                        "INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)",
                        (fila['nombre'], fila['correo'], float(fila['nota']))
                    )
                except sqlite3.IntegrityError:
                    print(f"[ADVERTENCIA] Registro duplicado: {fila['correo']}")

        conn.commit()
        conn.close()
        print("[OK] Registros importados correctamente.")

        
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