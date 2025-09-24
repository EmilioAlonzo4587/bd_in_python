# renombrar columna....
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
        cur.execute("ALTER TABLE cursos RENAME COLUMN titulo TO nombre_curso;")
        print("La Columna 'titulo' fue renombrada a 'nombre_curso' en cursos.")
