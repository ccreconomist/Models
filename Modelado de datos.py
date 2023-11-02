import pandas as pd

ruta_archivos = "C:\\Users\\MX49954\\Dic-22.csv"
datos = pd.read_csv(ruta_archivos, low_memory=False)
datos['FECHA_CONSUMO'] = pd.to_datetime(datos['FECHA_CONSUMO'], format='%d/%m/%Y')

# Mapeo de NO_DE_CUENTA a PRODUCTOS
mapeo_productos = {
    403750: 'BK Promoda',
    446351: 'BK C&A',
    481281: 'BK Shasa',
    481282: 'BK GCC',
    481283: 'BK Bodega',
    481284: 'BK Suburbia',
    469849: 'BK Bradescard',
    464811: 'BK Lob'
}

# Función para mapear NO_DE_CUENTA a PRODUCTOS
def mapear_productos(numero_cuenta):
    return mapeo_productos.get(numero_cuenta, 'Desconocido')

# Agregar la columna 'PRODUCTOS' al DataFrame
datos['PRODUCTOS'] = datos['NO_DE_CUENTA'].apply(mapear_productos)

# Agrupar los datos por 'FECHA', 'PRODUCTOS' y calcular el número de transacciones,
# la suma de 'IMP_DESTINO', el número de cuentas únicas y la suma de cuentas
resultados = (
    datos.groupby(['FECHA_CONSUMO', 'PRODUCTOS'])
    .agg({'IMP_DESTINO': ['count', 'sum'], 'NUM_CUENTA': ['nunique', 'sum']})
    .reset_index()
)
resultados.columns = ['FECHA_CONSUMO', 'PRODUCTOS', 'Numero_Transacciones', 'Suma_IMP_DESTINO', 'Cuentas_Unicas', 'Suma_Cuentas']

# Ruta y nombre de archivo de salida
ruta_salida = "C:\\Users\\MX49954\\Dic-22-2.xlsx"

# Exportar los datos a un archivo Excel
resultados.to_excel(ruta_salida, index=False)

print("Datos exportados exitosamente a", ruta_salida)
