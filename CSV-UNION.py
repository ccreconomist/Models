import os
import pandas as pd

# Ruta donde se encuentran los archivos CSV
ruta_archivos = "C:\\Users\\MX49954\\"

# Lista para almacenar DataFrames de cada archivo CSV
dataframes = []

# Archivos a unir
archivos_csv = ['CARTERA-PROMODA.csv', 'CARTERA-SHASA.csv', 'CARTERA-GCC.csv',
                'CARTERA-BODEGA.csv', 'CARTERA-C&A-BK.csv', 'CARTERA-C&A-PLCC.csv']

# Leer cada archivo CSV y cargarlo en la lista de DataFrames
for archivo in archivos_csv:
    archivo_ruta = os.path.join(ruta_archivos, archivo)
    df = pd.read_csv(archivo_ruta)

    # Seleccionar las columnas requeridas
    if 'TARJETA' not in df.columns:
        df = df.rename(columns={'0005064690020047015': 'TARJETA',
                                '1976-02-26': 'FECHA_NACIMIENTO',
                                'W': 'Bloq_Cobr',
                                '2': 'SEXO',
                                'Femenino': 'GENERO',
                                '7': 'EDO_CIVIL',
                                '2023-08-11': 'ULTC',
                                '0005064690020047000': 'CUENTA',
                                '506469': 'BINES',
                                '5064690020047000': 'NUM_CUENTA',
                                'Unnamed: 10': 'BLOQ_OPER',
                                'ATRASO de 1 a 8 días': 'BLOQ_COBR_ETIQUETA',
                                'PROMODA': 'SOCIO',
                                'PLCC': 'PRODUCTO'})
    df['CUENTA'] = df['CUENTA'].apply(lambda x: '{:0>3}'.format(str(x)))
    df['NUM_CUENTA'] = df['NUM_CUENTA'].astype(str).apply(lambda x: '{:0>3}'.format(x))

    dataframes.append(df)

# Unir los DataFrames en uno solo
df_final = pd.concat(dataframes, ignore_index=True)

# Mostrar el DataFrame resultante
print(df_final)
