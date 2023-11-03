import pandas as pd

# Ruta del archivo Excel de activaciones y nombre de la hoja
ruta_activaciones = "C:\\Users\\MX49954\\Venta 20 al 25 de octubre bonificacion.xlsx"
nombre_hoja_activaciones = 'Hoja1'

# Cargar los números de tarjeta desde el archivo de activaciones
df_activaciones = pd.read_excel(ruta_activaciones, sheet_name=nombre_hoja_activaciones)

# Ruta del archivo Excel de PROSA y nombre de la hoja
ruta_prosa = "C:\\Users\\MX49954\\PROSA-GCC.xlsx"
nombre_hoja_prosa = 'PROSA'

# Cargar el archivo Excel de PROSA en un DataFrame
df_prosa = pd.read_excel(ruta_prosa, sheet_name=nombre_hoja_prosa)

# Convertir las columnas 'tarjeta2' y 'autorizacion2' a texto en ambos DataFrames
df_activaciones['tarjeta2'] = df_activaciones['tarjeta2'].astype(str)
df_activaciones['autorizacion2'] = df_activaciones['autorizacion2'].astype(str)
df_prosa['tarjeta1'] = df_prosa['tarjeta1'].astype(str)
df_prosa['NUM_AUT'] = df_prosa['NUM_AUT'].astype(str)

# Realizar el cruce de datos
df_merged = pd.merge(df_activaciones, df_prosa, how='inner',
                     left_on=['tarjeta2', 'Fecha', 'autorizacion2'],
                     right_on=['tarjeta1', 'FECHA_CONSUMO', 'NUM_AUT'])

# Guardar el resultado en un nuevo archivo
df_merged.to_excel("C:\\Users\\MX49954\\CRUCE.xlsx", index=False)

print("Se han guardado las filas con las coincidencias en un nuevo archivo.")
