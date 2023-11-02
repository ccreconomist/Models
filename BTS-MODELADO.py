import pandas as pd

ruta_archivos = "C:\\Users\\MX49954\\bts-enero-marzo.csv"
datos = pd.read_csv(ruta_archivos, low_memory=False)
datos['FECHA_CONSUMO'] = pd.to_datetime(datos['FECHA_CONSUMO'], format='%d/%m/%Y')

# Realizar cálculos antes de la agrupación
total_transacciones = len(datos)
total_cuentas_unicas = datos['NUM_CUENTA'].nunique()
suma_total_imp_destino = datos['IMP_DESTINO'].sum()

# Agrupar los datos por 'FECHA_CONSUMO' y calcular el número de transacciones, cuentas únicas y suma de 'IMP_DESTINO'
resultados = (
    datos.groupby(pd.Grouper(key='FECHA_CONSUMO', freq='D'))
    .agg({'NUM_CUENTA': 'nunique', 'IMP_DESTINO': 'sum'})
    .reset_index()
)
resultados.columns = ['DIA', 'Cuentas_Unicas', 'Suma_IMP_DESTINO']

# Agregar columna de número de transacciones
resultados['Numero_Transacciones'] = resultados['Cuentas_Unicas']

# Ruta y nombre de archivo de salida
ruta_salida = "C:\\Users\\MX49954\\bts-enero-marzo-1.xlsx"

# Exportar los datos a un archivo Excel
resultados.to_excel(ruta_salida, index=False)

print("Datos exportados exitosamente a", ruta_salida)
