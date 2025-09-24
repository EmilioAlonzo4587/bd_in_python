# Eliminar tabla....
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
        cur.execute("DROP TABLE IF EXISTS cursos;")
        print("Tabla 'cursos' eliminada.")
