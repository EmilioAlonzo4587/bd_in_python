# agregar columna a la tabla existente....
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
        cur.execute("ALTER TABLE estudiantes ADD COLUMN edad INT;")
        print("La Columna 'edad' fue agregada en estudiantes.")
