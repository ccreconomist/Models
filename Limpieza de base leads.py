import pandas as pd
import warnings



# PARTE 1 (MODIFICACION DE LEADS)


# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_bd_leads = r"W:\2024\BD\BD-Leads.xlsx"  ### BASE CRM
ruta_Leads_MKT = r"W:\2024\BD\Leads_MKT.xlsx" ## BASE MKT
# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')
df_Leads_MKT = pd.read_excel(ruta_Leads_MKT, engine='openpyxl')
##df_Leads_2223 = pd.read_excel(ruta_Leads_2223, engine='openpyxl')
# Obtener la tabla con correos únicos y asignar ID único
df_correos_unicos = pd.concat([df_bd_leads['CORREO1'], df_Leads_MKT['CORREO2']]).unique() #df_Leads_2223['CORREO3']
df_resultado = pd.DataFrame({'Correo': df_correos_unicos})
# Agregar una columna de ID único
df_resultado['ID'] = range(1, len(df_resultado) + 1)
# Buscar en DB_LEADS y obtener las columnas requeridas
df_resultado_db_leads = df_resultado.merge(df_bd_leads[['CORREO1', 'NOMBRE', 'CLIENTE POTENCIAL', 'ASESOR',
'FECHA DE CREACIÓn', 'CANAL DE PROCEDENCIA', 'ULTIMO CONTACTO', 'ESTATUS','CAMPAÑA', 'FOLIO']], left_on='Correo', right_on='CORREO1', how='left', suffixes=('', '_BD'))

# Contar cuántas veces se repite cada correo en la combinación de 'CORREO1' y 'CORREO2'
df_repeticiones = pd.concat([df_bd_leads['CORREO1'], df_Leads_MKT['CORREO2']]).value_counts().reset_index()
df_repeticiones.columns = ['Correo', 'Repeticiones']

# Unir la información de repeticiones con df_resultado_db_leads
df_resultado_db_leads = df_resultado_db_leads.merge(df_repeticiones, left_on='Correo', right_on='Correo', how='left')


# Agregar la columna 'Estado' con valor 'Nuevo' por defecto
df_resultado_db_leads['Estado'] = df_resultado_db_leads.apply(lambda row: 'Registrado' if row['Correo'] in df_Leads_MKT['CORREO2'].values else 'Nuevo', axis=1)

# Llenar los valores nulos en las nuevas columnas con valores por defecto
df_resultado_db_leads['FECHA DE CREACIÓn'].fillna(pd.to_datetime('1900-01-01'), inplace=True)
df_resultado_db_leads['CLIENTE POTENCIAL'].fillna('No', inplace=True)
df_resultado_db_leads['ASESOR'].fillna('N/A', inplace=True)
df_resultado_db_leads['CANAL DE PROCEDENCIA'].fillna('N/A', inplace=True)
df_resultado_db_leads['ULTIMO CONTACTO'].fillna(pd.to_datetime('1900-01-01'), inplace=True)
# Eliminar duplicados basados en la columna 'Correo'
df_resultado_db_leads.drop_duplicates(subset=['Correo'], keep='first', inplace=True)
# Eliminar columnas innecesarias
df_resultado_db_leads.drop(['CORREO1'], axis=1, inplace=True)
# Guardar el resultado en un nuevo archivo Excel
ruta_resultado = r"W:\2024\BD\Nleads.xlsx"
df_resultado_db_leads.to_excel(ruta_resultado, index=False, engine='openpyxl')



