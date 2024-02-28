import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_bd_leads = r"W:\2024\BD\BD-Leads.xlsx"  ### BASE CRM
ruta_Leads_MKT = r"W:\2024\BD\Leads_MKT.xlsx" ## BASE MKT

# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')
df_Leads_MKT = pd.read_excel(ruta_Leads_MKT, engine='openpyxl')

# Validar coincidencias y marcar como registrado o nuevo
df_bd_leads['Estado'] = 'Nuevo'
df_bd_leads.loc[df_bd_leads['CORREO1'].isin(df_Leads_MKT['CORREO2']), 'Estado'] = 'Registrado'

# Crear una tabla con correos únicos y asignar ID único
df_correos_unicos = pd.concat([df_bd_leads['CORREO1'], df_Leads_MKT['CORREO2']]).unique()
df_resultado = pd.DataFrame({'ID': range(1, len(df_correos_unicos) + 1), 'Correo': df_correos_unicos})

# Fusionar la información de estado con la tabla resultante
df_resultado = df_resultado.merge(df_bd_leads[['CORREO1', 'Estado']], left_on='Correo', right_on='CORREO1', how='left')

# Llenar los valores nulos en 'Estado' con 'Nuevo'
df_resultado['Estado'].fillna('Nuevo', inplace=True)

# Eliminar columnas innecesarias
df_resultado.drop(['CORREO1'], axis=1, inplace=True)

# Guardar el resultado en un nuevo archivo Excel
ruta_resultado = r"W:\2024\BD\Resultado.xlsx"
df_resultado.to_excel(ruta_resultado, index=False, engine='openpyxl')



