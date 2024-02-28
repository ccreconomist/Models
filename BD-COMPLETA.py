import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_bd_leads = r"W:\2024\BD\Union_Resultado1.xlsx"
ruta_clientes_potenciales = r"W:\2024\BD\BD-Leads-22-23.xlsx"

# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')
df_bd_22_23 = pd.read_excel(ruta_clientes_potenciales, engine='openpyxl')

# Realizar la unión de los DataFrames según las columnas CORREO1 y CORREO3
df_union = pd.merge(df_bd_leads, df_bd_22_23, left_on='CORREO1', right_on='CORREO3', how='inner')

# Guardar el resultado en un nuevo archivo Excel
ruta_resultado = r"W:\2024\BD\Union_Resultado_Final.xlsx"
df_union.to_excel(ruta_resultado, index=False)

print("Unión completada. Resultado guardado en:", ruta_resultado)
