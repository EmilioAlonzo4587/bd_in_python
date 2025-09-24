# Conexión a PostgreSQL con Python desde VS Code

Este proyecto documenta los pasos que seguimos para **conectarnos a una base de datos PostgreSQL** usando Python en VS Code.  
También incluye ejemplos de cómo crear tablas y realizar operaciones DDL (agregar, renombrar, eliminar columnas, etc.).

--


Instalar la librería `psycopg2` para conectar Python con PostgreSQL:
   ```bash
   pip install psycopg2
```

---

## Conexión desde Python

Creamos un archivo `conexion.py` con el siguiente contenido:

```python
import psycopg2

try:
    conexion = psycopg2.connect(
        dbname="greenarrow",
        user="admin",
        password="admin",
        host="localhost",
        port="5433"
    )
    print("✅ Conexión exitosa a PostgreSQL")
except Exception as e:
    print("❌ Error al conectar:", e)
```

Ejecutamos el script desde VS Code o desde la terminal:

```bash
python conexion.py
```

---

## Creación de tablas

Creamos un archivo `tablas.py` para crear las tablas:

```python
import psycopg2

conexion = psycopg2.connect(
    dbname="greenarrow",
    user="admin",
    password="admin",
    host="localhost",
    port="5433"
)

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE empleados (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        puesto VARCHAR(50)
    )
''')

cursor.execute('''
    CREATE TABLE proyectos (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        descripcion TEXT
    )
''')

conexion.commit()
conexion.close()

print("✅ Tablas creadas correctamente")
```

---

## Operaciones DDL

Ejemplos de operaciones que aplicamos desde Python:

### ➕ Agregar columnas nuevas
```python
cursor.execute("ALTER TABLE empleados ADD COLUMN salario NUMERIC;")
```

### ✏️ Renombrar columnas
```python
cursor.execute("ALTER TABLE empleados RENAME COLUMN puesto TO cargo;")
```

### ❌ Eliminar columnas
```python
cursor.execute("ALTER TABLE empleados DROP COLUMN salario;")
```

### 🔒 Agregar un CHECK
```python
cursor.execute("ALTER TABLE empleados ADD CONSTRAINT chk_salario CHECK (salario > 0);")
```

### 🗑️ Eliminar una tabla
```python
cursor.execute("DROP TABLE proyectos;")
```

> Cada operación debe ir seguida de `conexion.commit()` para guardar los cambios.

---

## 📌 Ejecución en VS Code

1. Abrir VS Code en la carpeta del proyecto.  
2. Crear los archivos `.py` (por ejemplo: `conexion.py`, `tablas.py`).  
3. Ejecuta cada script uno por uno con el botón **▶️ Run Python File** o usando la terminal integrada.
