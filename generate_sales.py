import sqlite3
import random
from datetime import datetime, timedelta

# 1. Conexión a la base de datos
conn = sqlite3.connect("retail_sales.db")
cursor = conn.cursor()

# 2. Configuración de valores posibles
clientes = list(range(1, 11))
productos = list(range(1, 11))
canales = ["Online", "Tienda"]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Zaragoza", "Málaga"]

fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2023, 12, 31)
dias_totales = (fecha_fin - fecha_inicio).days

# 3. Obtener el último id_venta existente
cursor.execute("SELECT MAX(id_venta) FROM ventas")
ultimo_id = cursor.fetchone()[0]

# 4. Generar ventas automáticamente
ventas = []

for i in range(ultimo_id + 1, 501):
    fecha = fecha_inicio + timedelta(days=random.randint(0, dias_totales))
    venta = (
        i,
        fecha.strftime("%Y-%m-%d"),
        random.choice(clientes),
        random.choice(productos),
        random.randint(1, 4),
        random.choice(canales),
        random.choice(ciudades)
    )
    ventas.append(venta)

# 5. Insertar ventas en la base de datos
cursor.executemany("""
    INSERT INTO ventas (id_venta, fecha, id_cliente, id_producto, cantidad, canal_venta, ciudad)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", ventas)

# 6. Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Ventas generadas correctamente")
