import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Abrir archivo leads modificados en paso 1
ruta_bd_leads = r"W:\2024\BD\NuevaBD-2.xlsx"  ### NUEVA BASE
ruta_bd_venta = r"W:\2024\BD\ventas.xlsx"   ### Historico Ventas CRM
# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')
df_bd_venta = pd.read_excel(ruta_bd_venta, engine='openpyxl')

# Merge de las dos bases de datos por la columna de correo electrónico
df_resultado = pd.merge(df_bd_leads, df_bd_venta, left_on='Correo', right_on='Correo1', how='left')

# Seleccionar las columnas deseadas
columnas_deseadas = ['Equipo', 'Procedencia', 'Precio s/iva','Precio IVA','Ingreso', 'Fecha1']
df_resultado = df_resultado[columnas_deseadas]

# Imprimir las columnas presentes en el DataFrame resultante
print(df_resultado.columns)

# Guardar el resultado en un nuevo archivo Excel
ruta_resultado = r"W:\2024\BD\Resultado.xlsx"
df_resultado.to_excel(ruta_resultado, index=False, engine='openpyxl')
