import pandas as pd

# Ruta del archivo Excel de activaciones y nombre de la hoja
ruta_activaciones = "C:\\Users\\MX49954\\GCC-BONIFICACIONES-204.xlsx"
nombre_hoja_activaciones = 'Hoja1'

# Cargar los números de tarjeta desde el archivo de activaciones
df_activaciones = pd.read_excel(ruta_activaciones, sheet_name=nombre_hoja_activaciones)
numeros_tarjeta = df_activaciones['tarjeta2'].tolist()

# Ruta del archivo Excel de PROSA y nombre de la hoja
ruta_prosa = "C:\\Users\\MX49954\\PROSA-204GCC.xlsx"
nombre_hoja_prosa = 'PROSA'

# Cargar el archivo Excel de PROSA en un DataFrame
df_prosa = pd.read_excel(ruta_prosa, sheet_name=nombre_hoja_prosa)

# Filtrar el DataFrame de PROSA para dejar solo las filas que contengan los números de tarjeta de las activaciones
df_filtrado = df_prosa[df_prosa['Tarjeta1'].astype(str).isin(map(str, numeros_tarjeta))]

# Si se encontraron números de tarjeta en la columna "TARJETA", guardar en un nuevo archivo
if not df_filtrado.empty:
    df_filtrado.to_excel("C:\\Users\\MX49954\\bonificaciones-20-25.xlsx", index=False)
    print("Se han guardado las filas con los números de tarjeta en un nuevo archivo.")
else:
    print("No se encontraron filas con los números de tarjeta en la columna 'TARJETA' de PROSA.")

# Para eliminar las filas con los números de tarjeta del DataFrame original (opcional)
# df_prosa.drop(df_filtrado.index, inplace=True)