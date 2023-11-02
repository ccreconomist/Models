import pyodbc
import csv
import pandas as pd
from collections import defaultdict

# Establecer la conexión con la primera base de datos (BANKCARD)
conexion_banco = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=MP-VW-DB-004;"
    "Database=BANKCARD;"
    "Trusted_Connection=yes;"
)
cursor_banco = conexion_banco.cursor()

# Definir la consulta SQL para la primera base de datos PROSA_510
consulta_banco = """
    SELECT 
        NUM_CUENTA, 
        MCC_GIRO_COMERCIO, 
        IMP_DESTINO, 
        RFC_COMERCIO, 
        FECHA_CONSUMO,
        '000' + SUBSTRING(NUM_CUENTA, 1, LEN(NUM_CUENTA) - 3) + '000' AS NO_DE_CUENTA,
        CASE WHEN RFC_COMERCIO = 'MOS 150123565' THEN 'OnUS' ELSE NULL END AS OnUS,
        '01' AS TIPO_TRANSACCION,
        LEFT(NUM_CUENTA, 6) AS BINES
    FROM PROSA_510
    WHERE FECHA_CONSUMO >= '2023-01-01 00:00:00.000' AND 
          FECHA_CONSUMO <= '2023-08-25 00:00:00.000'
          AND '01' = '01'
"""

# Ejecutar la consulta en la primera base de datos
cursor_banco.execute(consulta_banco)
resultados_banco = cursor_banco.fetchall()

# Cerrar la conexión a la primera base de datos
conexion_banco.close()

# Establecer la conexión con la segunda base de datos (Producto2)
conexion_producto = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=MP-VW-DB-017;"
    "Database=Producto2;"
    "Trusted_Connection=yes;"
)
cursor_producto = conexion_producto.cursor()

# Definir la consulta SQL para la segunda base de datos
consulta_producto = """
    SELECT CUENTA, TARJETA, ULTC, RFC_CORTO, PRODUCTO, ACTIVACION
    FROM IT_CARTERA_PROMODA
    WHERE ACTIVACION >= '2023-01-01 00:00:00.000'
    AND ACTIVACION <= '2023-08-25 00:00:00.000'
"""

# Ejecutar la consulta en la segunda base de datos
cursor_producto.execute(consulta_producto)
resultados_producto = cursor_producto.fetchall()

# Cerrar la conexión a la segunda base de datos
conexion_producto.close()


