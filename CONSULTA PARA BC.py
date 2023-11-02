import pyodbc
import pandas as pd

# Establecer la conexión con la primera base de datos (BANKCARD)
conexion_banco = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=MP-VW-DB-004;"
    "Database=BANKCARD;"
    "Trusted_Connection=yes;"
)
cursor_banco = conexion_banco.cursor()

# Definir la consulta SQL
consulta_banco =  """
    SELECT 
        DATEADD(WEEK, DATEDIFF(WEEK, 0, FECHA_CONSUMO), 0) AS Fecha_Agrupada,
        MIN(FECHA_CONSUMO) AS Fecha_Inicio,
        MAX(FECHA_CONSUMO) AS Fecha_Fin,
        COUNT(*) AS Total_Transacciones,
        COUNT(DISTINCT NUM_CUENTA) AS Total_Cuentas_Unicas,
        SUM(IMP_DESTINO) AS Suma_Importes
    FROM PROSA_510
    WHERE 
        DATEPART(WEEKDAY, FECHA_CONSUMO) BETWEEN 5 AND 6  -- Jueves y viernes
        AND FECHA_CONSUMO >= '2022-01-01 00:00:00.000' 
        AND FECHA_CONSUMO <= '2023-08-25 00:00:00.000' 
        AND TIPO_TRANSACCION = '01' 
        AND LEFT(NUM_CUENTA, 6) IN ('481284', '481281', '403750', '464811', '481282', '446351', '469849', '481283') 
    GROUP BY DATEADD(WEEK, DATEDIFF(WEEK, 0, FECHA_CONSUMO), 0)
"""
# Ejecutar la consulta en la primera base de datos
cursor_banco.execute(consulta_banco)
resultados_banco = cursor_banco.fetchall()

# Cerrar la conexión a la primera base de datos
conexion_banco.close()








