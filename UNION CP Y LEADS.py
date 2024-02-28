import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_bd_leads = r"W:\2024\BD\BD-Leads.xlsx"
ruta_clientes_potenciales = r"W:\2024\BD\Clientes_Potenciales_2024-02-20 16_00_15.xlsx"

# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')
df_clientes_potenciales = pd.read_excel(ruta_clientes_potenciales, engine='openpyxl')

# Realizar la unión de los DataFrames según las columnas CORREO1 y CORREO2
df_union = pd.merge(df_bd_leads, df_clientes_potenciales, left_on='CORREO1', right_on='CORREO2', how='inner')

# Guardar el resultado en un nuevo archivo Excel
ruta_resultado = r"W:\2024\BD\Union_Resultado.xlsx"
df_union.to_excel(ruta_resultado, index=False)

print("Unión completada. Resultado guardado en:", ruta_resultado)

