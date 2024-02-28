import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_cp = r"W:\2024\BD\Clientes_Potenciales.xlsx"
ruta_leads = r"W:\2024\BD\Leads.xlsx"

# Leer los archivos Excel
df_cp = pd.read_excel(ruta_cp, engine='openpyxl')
df_leads = pd.read_excel(ruta_leads, engine='openpyxl')

# Unir la tabla Cliente potencial con la tabla Leads por nombre o correo
df_resultado = pd.merge(df_cp, df_leads, how='left', on=['NOMBRE', 'CORREO'], suffixes=('', '_Leads'))

# Imprimir las primeras filas del DataFrame resultante
print(df_resultado.head())

# Guardar el DataFrame resultante en la tabla Cliente potencial
df_resultado.to_excel(ruta_cp, index=False, engine='openpyxl')
