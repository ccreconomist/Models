import pandas as pd

# Ruta y nombre del archivo principal
nombre_archivo_principal = "C:\\Users\\MX49954\\C&A2.xlsx"
nombre_hoja1 = 'BASE-22-23'

# Leer el archivo y cargar en un DataFrame
df_union = pd.read_excel(nombre_archivo_principal, sheet_name=nombre_hoja1)

# Convertir 'CuentaReal' a tipo numérico
df_union['CuentaReal'] = pd.to_numeric(df_union['CuentaReal'])

# Agregar tres ceros al inicio de la columna 'CuentaReal' y asegurarse de que sea un dato numérico
df_union['CuentaReal'] = '000' + df_union['CuentaReal'].astype(str).str.replace('.', '').str.replace(',', '')

# Agrupar por 'CuentaReal' y sumar 'MONTOREAL'
df_resumen = df_union.groupby('CuentaReal')['MONTOREAL'].sum().reset_index()

# Mostrar el resultado
print(df_resumen)
