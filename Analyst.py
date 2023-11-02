import pandas as pd

# Ruta del archivo Excel de VALIDACION-C-25 y nombre de la hoja
ruta_Validacion = 'C:\\Users\\MX49954\\VALIDACION-C-25.xlsx'
nombre_hoja_Validacion = 'Hoja1'

# Cargar el archivo Excel de VALIDACION-C-25 en un DataFrame
df_validacion = pd.read_excel(ruta_Validacion, sheet_name=nombre_hoja_Validacion)
cuentas_validacion = df_validacion['CUENTA1'].tolist()

# Ruta del archivo Excel de Corte-25 y nombre de la hoja
ruta_C25 = 'C:\\Users\\MX49954\\Corte-25.xlsx'
nombre_hoja_C25 = 'Hoja1'

# Cargar el archivo Excel de Corte-25 en un DataFrame
df_C25 = pd.read_excel(ruta_C25, sheet_name=nombre_hoja_C25)
cuentas_C25 = df_C25['CUENTA'].tolist()

# Crear una nueva columna 'TIPO' en df_validacion para marcar las coincidencias
df_validacion['TIPO'] = df_validacion['CUENTA1'].isin(cuentas_C25).map({True: 'SI', False: 'NO'})

# Guardar el DataFrame resultante en un nuevo archivo Excel
ruta_resultado = 'C:\\Users\\MX49954\\Resultado.xlsx'
df_validacion.to_excel(ruta_resultado, index=False)

print("Archivo resultante guardado en", ruta_resultado)

