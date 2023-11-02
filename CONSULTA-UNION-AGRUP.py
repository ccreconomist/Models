import pyodbc
import csv
import pandas as pd
from collections import defaultdict
import datetime

# Obtener la fecha actual
current_date = datetime.datetime.now()
# Obtener la fecha actual
current_date = datetime.datetime.now()

# Calcular el mes y el año del mes anterior
previous_month = current_date.month - 1 if current_date.month > 1 else 12
previous_year = current_date.year if current_date.month > 1 else current_date.year - 1

# Crear una fecha con el mes y el año del mes anterior
previous_month_date = datetime.datetime(previous_year, previous_month, 1)

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
        LEFT(NUM_CUENTA, 6) AS BINES,
        LEFT(NUM_CUENTA, 6) AS BIN
    FROM PROSA_510
    WHERE FECHA_CONSUMO >= '2023-01-01 00:00:00.000' AND 
          FECHA_CONSUMO <= '2023-08-25 00:00:00.000'
          AND '01' = '01'
          AND (LEFT(NUM_CUENTA, 6) = '403750' OR LEFT(NUM_CUENTA, 6) = '506469')
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

# Crear un diccionario para almacenar los resultados de la segunda consulta por CUENTA
resultados_dict = {row.CUENTA: (row.TARJETA, row.ULTC, row.RFC_CORTO, row.PRODUCTO) for row in resultados_producto}

# Unir los resultados de ambas consultas por NO_DE_CUENTA y CUENTA
resultados_finales = []

# Crear un diccionario para almacenar cuentas únicas por mes y sumar importes de IMP_DESTINO
aggregated_data = defaultdict(lambda: [set(), 0])

for fila in resultados_banco:
    no_de_cuenta = fila.NO_DE_CUENTA
    cuenta = no_de_cuenta
    otros_datos = resultados_dict.get(cuenta)
    if otros_datos:
        coincide = 1
        fila_resultado = list(fila) + list(otros_datos) + [coincide]
        resultados_finales.append(fila_resultado)
        fecha_consumo = fila.FECHA_CONSUMO.date()
        imp_destino = fila.IMP_DESTINO
        bines_value = int(fila.BINES)
        if bines_value in [403750, 506469]:
            aggregated_data[fecha_consumo][0].add(no_de_cuenta)
            aggregated_data[fecha_consumo][1] += imp_destino
    else:
        coincide = 0
        fila_resultado = list(fila) + [None, None, None, None, None] + [coincide]
        resultados_finales.append(fila_resultado)

# Crear un diccionario para almacenar si las cuentas son nuevas o no
account_status = defaultdict(str)

# Calcular si las cuentas son nuevas o no
for month, accounts in aggregated_data.items():
    previous_accounts = aggregated_data.get(previous_month_date, [set(), 0])[0]
    new_accounts = accounts[0] - previous_accounts
    for account in new_accounts:
        account_status[account] = "Nueva"
    for account in (accounts[0] - new_accounts):
        account_status[account] = "Vieja"

# Crear una lista para los resultados finales por mes
resultados_por_mes = []

# Generar resultados por mes con cuentas únicas y suma de IMP_DESTINO
for month, (accounts, total_imp_destino) in aggregated_data.items():
    unique_accounts = len(accounts)
    new_accounts = sum(1 for account in accounts if account_status[account] == "Nueva")
    old_accounts = unique_accounts - new_accounts
    resultados_por_mes.append([month, unique_accounts, new_accounts, old_accounts, total_imp_destino])

# Crear un DataFrame de Pandas con los resultados por mes
column_names_por_mes = ["MES", "CUENTAS_UNICAS", "CUENTAS_NUEVAS", "CUENTAS_VIEJAS", "SUMA_IMP_DESTINO"]
resultados_df_por_mes = pd.DataFrame(resultados_por_mes, columns=column_names_por_mes)

# Ruta y nombre de archivo de salida para resultados por mes
ruta_salida_por_mes = "C:\\Users\\MX49954\\cosecha-promoda-por-mes-4.xlsx"

# Exportar los datos por mes a un archivo Excel
resultados_df_por_mes.to_excel(ruta_salida_por_mes, index=False)

print("Datos exportados exitosamente a", ruta_salida_por_mes)



