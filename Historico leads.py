import pandas as pd
import warnings
import os
from pathlib import Path

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel y la carpeta de destino
carpeta_destino = r"W:\2024\BD"  # Cambia la ruta según tu estructura de carpetas
ruta_bd_leads = os.path.join(carpeta_destino, "2.BD-Leads.xlsx")  ### BASE CRM
ruta_Leads_MKT = os.path.join(carpeta_destino, "1.Leads_MKT.xlsx")  ## BASE MKT
ruta_CP = os.path.join(carpeta_destino, "3.Clientes Potenciales.xlsx")  ## Clientes Potenciales
ruta_4_ventas = os.path.join(carpeta_destino, "4.Ventas.xlsx")  ## 4.Ventas
ruta_resultado = os.path.join(carpeta_destino, "5.Concentrado Leads.xlsx")  ## Resultado Final

# Crear la carpeta de destino si no existe
Path(carpeta_destino).mkdir(parents=True, exist_ok=True)

# Borrar el archivo '5.Concentrado Leads.xlsx' si ya existe
if os.path.exists(ruta_resultado):
    os.remove(ruta_resultado)

# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')
df_Leads_MKT = pd.read_excel(ruta_Leads_MKT, engine='openpyxl')
df_CP = pd.read_excel(ruta_CP, engine='openpyxl')
df_4_ventas = pd.read_excel(ruta_4_ventas, engine='openpyxl')

# Seleccionar las columnas relevantes de cada DataFrame
columnas_bd_leads = ['CORREO', 'NOMBRE', 'CELULAR', 'ESTADO', 'CANAL DE PROCEDENCIA', 'FECHA DE CREACIÓn']
columnas_leads_mkt = ['CORREO', 'Nombre', 'CELULAR', 'Canal de Procedencia', 'Fecha-MKT']
columnas_CP = ['CORREO', 'NOMBRE', 'CELULAR', 'CANAL DE PROCEDENCIA', 'CREADO']
columnas_4_ventas = ['Nombre', 'Correo', 'Telefono', 'Procedencia de venta', 'Asesor', 'Fecha Venta', 'Equipo']

# Crear un DataFrame con todos los correos únicos
df_todos_correos = pd.DataFrame({'CORREO': pd.concat([df_bd_leads['CORREO'], df_Leads_MKT['CORREO'], df_CP['CORREO']], ignore_index=True).drop_duplicates()})

# Agregar la nueva columna 'ORIGEN' antes de la columna 'CORREO'
df_todos_correos.insert(0, 'ORIGEN', '')

# Marcar el origen de los correos en la columna 'ORIGEN'
df_todos_correos.loc[df_todos_correos['CORREO'].isin(df_bd_leads['CORREO']), 'ORIGEN'] = 'BD_LEADS'
df_todos_correos.loc[df_todos_correos['CORREO'].isin(df_Leads_MKT['CORREO']), 'ORIGEN'] += ' LEADS_MKT'
df_todos_correos.loc[df_todos_correos['CORREO'].isin(df_CP['CORREO']), 'ORIGEN'] += ' CP'

# Fusionar DataFrames utilizando outer join
df_combinado = pd.merge(df_todos_correos, df_bd_leads[columnas_bd_leads], on='CORREO', how='left', indicator='_merge_BD')
df_combinado = pd.merge(df_combinado, df_Leads_MKT[columnas_leads_mkt], on='CORREO', how='left', indicator='_merge_MKT')
df_combinado = pd.merge(df_combinado, df_CP[columnas_CP], left_on='CORREO', right_on='CORREO', how='left', indicator='_merge_CP')

# Filtrar las filas que están presentes solo en BD-Leads o Leads_MKT o Clientes Potenciales
df_unidos = df_combinado[(df_combinado['_merge_BD'] != 'both') | (df_combinado['_merge_MKT'] != 'both') | (df_combinado['_merge_CP'] != 'both')].drop(['_merge_BD', '_merge_MKT', '_merge_CP'], axis=1)

# Eliminar duplicados basados en la columna 'CORREO'
df_unicos = df_combinado.drop_duplicates(subset=['CORREO']).drop(['_merge_BD', '_merge_MKT', '_merge_CP'], axis=1)

# Guardar el resultado en un nuevo archivo Excel
df_unicos.to_excel(ruta_resultado, sheet_name='Sheet1', index=False, engine='openpyxl')

# Contar la ocurrencia de cada correo en df_bd_leads y almacenarla en una nueva columna 'OCURRENCIA'
ocurrencia_correo_bd_leads = df_bd_leads['CORREO'].value_counts()
df_bd_leads['OCURRENCIA'] = df_bd_leads['CORREO'].map(ocurrencia_correo_bd_leads)

# Contar la ocurrencia en df_Leads_MKT y sumar a la columna 'OCURRENCIA'
ocurrencia_correo_leads_mkt = df_Leads_MKT['CORREO'].value_counts()
df_Leads_MKT['OCURRENCIA'] = df_Leads_MKT['CORREO'].map(ocurrencia_correo_leads_mkt) + df_Leads_MKT.get('OCURRENCIA', 0)

# Contar la ocurrencia en df_CP y sumar a la columna 'OCURRENCIA'
ocurrencia_correo_cp = df_CP['CORREO'].value_counts()
df_CP['OCURRENCIA'] = df_CP['CORREO'].map(ocurrencia_correo_cp) + df_CP.get('OCURRENCIA', 0)

# Convertir las columnas de fechas a tipo datetime en df_bd_leads
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

# Calcular los días desde la fecha de creación hasta el día de su último contacto
df_bd_leads['DÍAS DESDE CREACIÓN HASTA ÚLTIMO CONTACTO'] = (df_bd_leads['ULTIMO CONTACTO'] - df_bd_leads['FECHA DE CREACIÓn']).dt.days

# Calcular los días desde la fecha de creación hasta el día de hoy
df_bd_leads['DÍAS DESDE CREACIÓN HASTA HOY'] = (pd.to_datetime('today') - df_bd_leads['FECHA DE CREACIÓn']).dt.days

# Marcar los casos donde los días son 0 como misma fecha de creación
df_bd_leads['MISMA FECHA DE INICIO Y CONTACTO'] = (df_bd_leads['DÍAS DESDE CREACIÓN HASTA ÚLTIMO CONTACTO'] == 0) & (df_bd_leads['DÍAS DESDE CREACIÓN HASTA HOY'] == 0)

# Leer los DataFrames de las tres tablas
df_sheet1 = pd.read_excel(ruta_resultado, sheet_name='Sheet1')
ruta_bd_leads = r"W:\2024\BD\2.BD-Leads.xlsx"  ### BASE CRM
ruta_Leads_MKT = r"W:\2024\BD\1.Leads_MKT.xlsx"  ## BASE MKT
ruta_CP = r"W:\2024\BD\3.Clientes Potenciales.xlsx"  ## Clientes Potenciales
ruta_4_ventas = r"W:\2024\BD\4.Ventas.xlsx"  ## Clientes Potenciales

# Obtener correos únicos de las tres tablas
correos_unicos = pd.concat([df_sheet1['CORREO'], df_bd_leads['CORREO'], df_Leads_MKT['CORREO'], df_CP['CORREO']]).unique()

# Filtrar df_bd_leads solo para correos presentes en 'Sheet1'
df_bd_leads_filtrado = df_bd_leads[df_bd_leads['CORREO'].isin(correos_unicos)]

# Asignar un ID único a cada fila basado en correos únicos de las tres tablas
df_bd_leads_filtrado['ID'] = range(1, len(df_bd_leads_filtrado) + 1)

# Crear una hoja nueva con información adicional
with pd.ExcelWriter(ruta_resultado, engine='openpyxl', mode='a') as writer:
    df_sheet1 = pd.read_excel(ruta_resultado, sheet_name='Sheet1')

    # Obtener correos únicos de la hoja 'Sheet1'
    correos_unicos = df_sheet1['CORREO'].unique()

    # Filtrar df_bd_leads solo para correos presentes en 'Sheet1'
    df_bd_leads_filtrado = df_bd_leads[df_bd_leads['CORREO'].isin(correos_unicos)]

    # Fusionar con BD-Leads para obtener información adicional
    df_info_adicional = pd.merge(df_sheet1[['CORREO']],
                                 df_bd_leads_filtrado[['NOMBRE', 'CORREO', 'ASESOR', 'ESTATUS', 'ESTADO', 'CANAL DE PROCEDENCIA', 'FECHA INICIAL', 'DÍAS DESDE ASIGNACIÓN', 'DÍAS DESDE CREACIÓN', 'DÍAS DESDE ÚLTIMO CONTACTO', 'ÚLTIMA FECHA DE CONTACTO', 'OCURRENCIA', 'DÍAS DESDE CREACIÓN HASTA ÚLTIMO CONTACTO', 'DÍAS DESDE CREACIÓN HASTA HOY', 'MISMA FECHA DE INICIO Y CONTACTO']],
                                 on='CORREO',
                                 how='left')

    # Fusionar con Leads_MKT para obtener información adicional
    df_info_adicional = pd.merge(df_info_adicional,
                                 df_Leads_MKT[['CORREO', 'Nombre', 'CELULAR', 'Canal de Procedencia', 'Fecha-MKT']],
                                 on='CORREO',
                                 how='left')

    # Fusionar con CP para obtener información adicional
    df_info_adicional = pd.merge(df_info_adicional,
                                 df_CP[['CORREO', 'NOMBRE', 'CELULAR', 'CANAL DE PROCEDENCIA', 'CREADO']],
                                 on='CORREO',
                                 how='left')

    # Fusionar con la hoja de ventas para obtener información adicional
    df_info_adicional = pd.merge(df_sheet1[['CORREO']],
                                 df_4_ventas[['Nombre', 'Correo', 'Telefono', 'Procedencia de venta', 'Asesor', 'Fecha Venta','Equipo']],
                                 left_on='CORREO',
                                 right_on='Correo',
                                 how='left')
    # Fusionar con la hoja de ventas para obtener información adicional
    df_info_adicional = pd.merge(df_info_adicional,
                                 df_4_ventas[['Nombre', 'Correo', 'Telefono', 'Procedencia de venta', 'Asesor', 'Fecha Venta','Equipo']],
                                 left_on='CORREO',
                                 right_on='Correo',
                                 how='left')

    # Marcar el origen de los correos en la columna 'ORIGEN'
    df_info_adicional.loc[df_info_adicional['CORREO'].isin(df_bd_leads['CORREO']), 'ORIGEN'] = 'BD_LEADS'
    df_info_adicional.loc[df_info_adicional['CORREO'].isin(df_Leads_MKT['CORREO']), 'ORIGEN'] += ' LEADS_MKT'
    df_info_adicional.loc[df_info_adicional['CORREO'].isin(df_CP['CORREO']), 'ORIGEN'] += ' CP'

    # Identificar la fecha más antigua excluyendo valores no válidos
    df_bd_leads['FECHA INICIAL'] = df_bd_leads[date_columns].min(axis=1)

    # Crear una Serie con las fechas iniciales para cada correo
    fechas_iniciales = df_bd_leads.groupby('CORREO')['FECHA INICIAL'].first()

    # Agregar la columna 'FECHA INICIAL' a df_info_adicional utilizando el correo como índice
    df_info_adicional['FECHA INICIAL'] = df_info_adicional['CORREO'].map(fechas_iniciales)

    # Ordenar el DataFrame por 'CORREO' y 'FECHA INICIAL'
    df_info_adicional = df_info_adicional.sort_values(by=['CORREO', 'FECHA INICIAL'], ascending=[True, False])

    # Mantener solo la primera fila para cada grupo de correos (la más reciente)
    df_info_adicional = df_info_adicional.drop_duplicates(subset='CORREO', keep='first')

    # Eliminar duplicados en caso de que haya alguna fila duplicada en 'Sheet1'
    df_sheet1 = df_sheet1.drop_duplicates(subset='CORREO', keep='first')


    # Agregar la información adicional a una nueva hoja
    df_info_adicional.to_excel(writer, sheet_name='Informacion Adicional', index=False, engine='openpyxl')

# Leer todo el contenido del archivo Excel actualizado
df_resultado_actualizado = pd.read_excel(ruta_resultado, sheet_name=None)

# Guardar todo el contenido actualizado en un nuevo archivo Excel
with pd.ExcelWriter(ruta_resultado, engine='openpyxl') as writer:
    for sheet_name, sheet_data in df_resultado_actualizado.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)
