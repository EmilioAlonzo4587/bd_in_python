# Crear Las Tablas.....
import psycopg

conn_params = {
    "host": "127.0.0.1",
    "port": 5433,
    "dbname": "greenarrow",
    "user": "greenarrow",
    "password": "12345"
}

with psycopg.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                CARNE SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                ID SERIAL PRIMARY KEY,
                titulo VARCHAR(100) NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS catedraticos (
                colegiado SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS escritorios (
                numero SERIAL PRIMARY KEY,
                color VARCHAR(100) NOT NULL
            );
        """)
        print("Las Tablas fueron creadas.")
