import pandas as pd

ruta_archivos = "C:\\Users\\MX49954\\Sept-22-2.csv"
datos = pd.read_csv(ruta_archivos, low_memory=False)
datos['FECHA_CONSUMO'] = pd.to_datetime(datos['FECHA_CONSUMO'], format='%d-%m-%Y')

# Agrupar los datos por 'FECHA_CONSUMO' (día) y calcular las métricas
resultados = (
    datos.groupby(['FECHA_CONSUMO'])
    .agg({'Cuentas_Unicas': 'sum', 'IMP_DESTINO': 'sum', 'Numero_Transacciones': 'sum'})
    .reset_index()
)

# Ruta y nombre de archivo de salida
ruta_salida = "C:\\Users\\MX49954\\Consolidacion-22-2-2.xlsx"

# Exportar los datos a un archivo Excel
resultados.to_excel(ruta_salida, index=False)

print("Datos exportados exitosamente a", ruta_salida)
