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

# Convertir las columnas de fecha a objetos DateTime
df_activaciones['Fecha'] = pd.to_datetime(df_activaciones['Fecha'], format='%Y-%m-%d', errors='coerce')
df_prosa['FECHA_CONSUMO'] = pd.to_datetime(df_prosa['FECHA_CONSUMO'], format='%Y-%m-%d', errors='coerce')

# Definir las columnas de cruce
columnas_cruce = ['tarjeta2', 'Fecha', 'autorizacion2']

# Realizar el cruce y marcar coincidencias con "1"
df_activaciones['Coincidencias'] = 0
for index, row in df_activaciones.iterrows():
    for col in columnas_cruce:
        if (df_prosa['tarjeta1'] == row['tarjeta2']).any() and \
           (df_prosa['FECHA_CONSUMO'] == row['Fecha']).any() and \
           (df_prosa['NUM_AUT'] == row['autorizacion2']).any():
            df_activaciones.at[index, 'Coincidencias'] = 1

# Guardar el resultado en un nuevo archivo
df_activaciones.to_excel("C:\\Users\\MX49954\\bonificaciones-20-25-con-marcas.xlsx", index=False)

print("Se han guardado las filas con las coincidencias marcadas en un nuevo archivo.")
