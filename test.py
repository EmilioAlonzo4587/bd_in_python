# test_db.py
import psycopg

conn = psycopg.connect(
    host="127.0.0.1",
    port=5433,
    dbname="greenarrow",
    user="greenarrow",
    password="12345"
)

with conn, conn.cursor() as cur:
    cur.execute("SELECT current_database(), current_user;")
    print(cur.fetchone())
