import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_bd_leads = r"W:\2024\BD\BD-Leads.xlsx"  ### BASE CRM

# Leer el archivo Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')

# Convertir las columnas de fechas a tipo datetime
date_columns = ['FECHA DE CONTACTO', 'FECHA DE ASIGNACIÓN', 'FECHA DE CREACIÓn', 'ULTIMO CONTACTO']
df_bd_leads[date_columns] = df_bd_leads[date_columns].apply(pd.to_datetime, errors='coerce')

# Identificar la fecha más antigua excluyendo valores no válidos
df_bd_leads['FECHA INICIAL'] = df_bd_leads[date_columns].min(axis=1)

# Calcular los días desde la fecha inicial
df_bd_leads['DÍAS DESDE ASIGNACIÓN'] = (df_bd_leads['FECHA DE ASIGNACIÓN'] - df_bd_leads['FECHA INICIAL']).dt.days
df_bd_leads['DÍAS DESDE CREACIÓN'] = (df_bd_leads['FECHA DE CREACIÓn'] - df_bd_leads['FECHA INICIAL']).dt.days
df_bd_leads['DÍAS DESDE ÚLTIMO CONTACTO'] = (df_bd_leads['ULTIMO CONTACTO'] - df_bd_leads['FECHA INICIAL']).dt.days

# Identificar la última fecha de contacto
df_bd_leads['ÚLTIMA FECHA DE CONTACTO'] = df_bd_leads[date_columns].max(axis=1)

# Puedes imprimir el DataFrame resultante para revisar los cambios
print(df_bd_leads)
