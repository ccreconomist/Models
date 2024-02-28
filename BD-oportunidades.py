import pandas as pd
import warnings

# Desactivar advertencias de deprecación de PyArrow
warnings.simplefilter(action='ignore', category=FutureWarning)

# Rutas de los archivos Excel
ruta_bd_leads = r"W:\2024\BD\Oportunidades.xlsx"

# Leer los archivos Excel
df_bd_leads = pd.read_excel(ruta_bd_leads, engine='openpyxl')

# Paso 1: Agregar una columna con un ID único para cada cliente potencial
df_bd_leads['ID_Cliente'] = df_bd_leads.groupby('Cliente potencial').ngroup()

# Paso 2: Ordenar el DataFrame por Cliente potencial y Fecha actualizado en orden descendente
df_bd_leads.sort_values(by=['Cliente potencial', 'Actualizado'], ascending=[True, False], inplace=True)

# Paso 3: Crear la columna 'Fecha_Actualizada' con solo la fecha
df_bd_leads['Fecha_Actualizada'] = pd.to_datetime(df_bd_leads['Actualizado']).dt.date

# Paso 4: Marcar como "Reciente" el registro más reciente para cada cliente potencial
df_bd_leads['Estado'] = 'Antiguo'
df_bd_leads.loc[df_bd_leads.groupby('Cliente potencial')['Actualizado'].idxmax(), 'Estado'] = 'Reciente'

# Establecer el formato de fecha antes de guardar en el nuevo archivo Excel
df_bd_leads['Actualizado'] = df_bd_leads['Actualizado'].dt.strftime('%Y-%m-%d')

# Guardar el DataFrame modificado en un nuevo archivo Excel
ruta_bd_leads_modificado = r"W:\2024\BD\Oportunidades_Modificado.xlsx"
df_bd_leads.to_excel(ruta_bd_leads_modificado, index=False, engine='openpyxl')
