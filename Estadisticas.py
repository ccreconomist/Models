import pandas as pd

# Ruta y nombre del archivo principal
nombre_archivo_principal = "C:\\Users\\MX49954\\C&A-NUEVO.xlsx"
nombre_hoja1 = 'BASE-22-23'
df_union = pd.read_excel(nombre_archivo_principal, sheet_name=nombre_hoja1)