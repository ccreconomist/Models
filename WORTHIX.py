import pandas as pd

# Cargar el archivo Excel en un DataFrame
nombre_archivo = "C:\\Users\\MX49954\\Base Worthix- CYA-BK.xlsx"
nombre_hoja = 'Hoja2'
CYA_BK_WORTHIX = pd.read_excel(nombre_archivo, sheet_name=nombre_hoja)

# Eliminar filas con NaN en la columna 'relative_price_tags'
CYA_BK_WORTHIX = CYA_BK_WORTHIX.dropna(subset=['theme'])

# Filtrar el DataFrame para obtener solo las filas que cumplen con la condición
filtro_db = CYA_BK_WORTHIX[CYA_BK_WORTHIX['theme'].str.startswith('people')]

# Mostrar el resultado del filtro
print(filtro_db)

