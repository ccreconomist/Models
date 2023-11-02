import pandas as pd

ruta_archivos = "C:\\Users\\MX49954\\Datos_2023.csv"
datos = pd.read_csv(ruta_archivos, low_memory=False, encoding="ISO-8859-1")  # Cambio en la codificación
datos['FECHA_CONSUMO'] = pd.to_datetime(datos['FECHA_CONSUMO'], format='%d/%m/%Y')

# Agrupar por grupos de 7 días y sumar las columnas
aggregated_data = datos.groupby(pd.Grouper(key='FECHA_CONSUMO', freq='7D')).agg({
    'Cuentas_Unicas': 'sum',
    'IMP_DESTINO': 'sum',
    'Numero_Transacciones': 'sum'
}).reset_index()

# Guardar los resultados en el archivo Excel
ruta_archivo_salida = "C:\\Users\\MX49954\\Summary.xlsx"
with pd.ExcelWriter(ruta_archivo_salida) as writer:
    aggregated_data.to_excel(writer, sheet_name='Summary', index=False)

print("Proceso completado. Los datos agregados se han guardado en 'Summary.xlsx'.")
