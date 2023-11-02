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

# Definir la consulta SQL para la primera base de datos PROSA_510 ***AQUI SE TIENE QUE MODIFCAR LOS PERIODOS DE LAS CONSULTAS
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

# Definir la consulta SQL para la segunda base de datos, ***AQUI SE TIENE QUE MODIFCAR LOS PERIODOS DE LAS CONSULTAS
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

# Crear un diccionario para agrupar cuentas únicas por mes y sumar importes de IMP_DESTINO
aggregated_data = defaultdict(lambda: [set(), 0])

for fila in resultados_banco:
    no_de_cuenta = fila.NO_DE_CUENTA
    cuenta = no_de_cuenta
    otros_datos = resultados_dict.get(cuenta)
    if otros_datos:
        coincide = 1
        fila_resultado = list(fila) + list(otros_datos) + [coincide]
        resultados_finales.append(fila_resultado)
### AQUI SIEMPRE SE REALIZARA UNA MODIFICACION PARA DIFERENTES CONSULTAS
        fecha_consumo = fila.FECHA_CONSUMO.date()
        imp_destino = fila.IMP_DESTINO
        bines_value = int(fila.BINES)
        if bines_value in [403750, 506469]: #### AQUI SE TIENE QUE AGREGAR, QUITAR O MODIFICAR LOS BINES
            aggregated_data[fecha_consumo][0].add(no_de_cuenta)
            aggregated_data[fecha_consumo][1] += imp_destino
    else:
        coincide = 0
        fila_resultado = list(fila) + [None, None, None, None, None] + [coincide]
        resultados_finales.append(fila_resultado)

# Crear un diccionario para los valores de BINES y sus correspondientes nombres
bin_mapping = {
    403750: 'BK Promoda',
    446351: 'BK C&A',
    481281: 'BK Shasa',
    481282: 'BK GCC',
    481283: 'BK Bodega',
    481284: 'BK Suburbia',
    469849: 'BK Bradescard',
    464811: 'BK Lob',
    506369: 'PLCC SUBURBIA',
    506372: 'PLCC SHASA',
    506469: 'PLCC PROMODA',
    506370: 'PLCC GCC',
    286900: 'PLCC C&A',
    506329: 'PLCC C&A',
    506371: 'PLCC BODEGA A.',
    286900: 'C&A PL/PP',
    506330: 'C&A PL/PP',
    506293: 'Bodega PP',
    506290: 'Shasa PP',
    506360: 'Promoda PP',
}
# Definir la lista de nombres de columnas
column_names = [
    "NUM_CUENTA", "MCC_GIRO_COMERCIO", "IMP_DESTINO", "RFC_COMERCIO",
    "FECHA_CONSUMO", "NO_DE_CUENTA", "OnUS", "TIPO_TRANSACCION",
    "BINES", "TARJETA", "ULTC", "RFC_CORTO", "PRODUCTO", "COINCIDE", "ESTADO_CUENTA"
]

# Agregar una columna para el valor correspondiente al BINES
for fila in resultados_finales:
    bines_value = int(fila[-1])  # Ajusta el índice según tu estructura
    bines_name = bin_mapping.get(bines_value)
    fila.append(bines_name)

# Asegurarse de que resultados_finales tenga la misma cantidad de columnas que column_names
for fila in resultados_finales:
    if len(fila) < len(column_names):
        fila.extend([None] * (len(column_names) - len(fila)))

# Crear un DataFrame de Pandas con los resultados finales
resultados_df = pd.DataFrame(resultados_finales, columns=column_names)

# Ruta y nombre de archivo de salida
ruta_salida = "C:\\Users\\MX49954\\cosecha-promoda.xlsx"

# Exportar los datos a un archivo Excel
resultados_df.to_excel(ruta_salida, index=False)

print("Datos exportados exitosamente a", ruta_salida)
