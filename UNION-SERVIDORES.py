import pyodbc

# Establecer la conexión con la base de datos
conexion_string = (
    "Driver={SQL Server Native Client 11.0};"
    "Server=MP-VW-DB-004;"
    "Database=BANKCARD;"
    "Trusted_Connection=yes;"
)

# Definir la consulta SQL
consulta = """
    SELECT 
        NUM_CUENTA, 
        MCC_GIRO_COMERCIO, 
        IMP_DESTINO, 
        RFC_COMERCIO, 
        '000' + SUBSTRING(NUM_CUENTA, 1, LEN(NUM_CUENTA) - 3) + '000' AS NO_DE_CUENTA,
        CASE WHEN RFC_COMERCIO = 'MOS 150123565' THEN 'OnUS' ELSE NULL END AS OnUS
    FROM PROSA_510
    WHERE FECHA_CONSUMO >= '2023-01-01 00:00:00.000' AND 
          FECHA_CONSUMO <= '2023-08-25 00:00:00.000'
"""

# Utilizar un contexto para la conexión y el cursor
with pyodbc.connect(conexion_string) as conexion:
    cursor = conexion.cursor()

    # Ejecutar la consulta
    cursor.execute(consulta)

    # Obtener los resultados
    resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

