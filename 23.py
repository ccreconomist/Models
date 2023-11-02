import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime

# Ruta y nombre del archivo principal
nombre_archivo_principal = "C:\\Users\\MX49954\\C&A.xlsx"

# Nombres de las hojas
nombres_hojas = ['BK-D', 'BK-C', 'PLCC-D', 'PLCC-C', 'PL-D']

# Leer cada hoja y agregar tres ceros a la columna 'CuentaReal'
dfs = []
for nombre_hoja in nombres_hojas:
    df = pd.read_excel(nombre_archivo_principal, sheet_name=nombre_hoja)
    df['CuentaReal'] = '000' + df['CuentaReal'].astype(str)
    dfs.append(df)

# Procesar cada DataFrame
for i, df in enumerate(dfs):
    # Filtrar por fechas
    df['DAT_ATIVACAO_CTAF'] = pd.to_datetime(df['DAT_ATIVACAO_CTAF'])
    df_filtered = df[(df['DAT_ATIVACAO_CTAF'] >= '2022-09-01') & (df['DAT_ATIVACAO_CTAF'] <= '2023-09-17')]

    # Agrupar por CuentaReal y sumar MONTOREAL
    df_sum = df_filtered.groupby('CuentaReal')['MONTOREAL'].sum().reset_index()

    # Guardar el DataFrame en un nuevo archivo
    new_filename = f"C:\\Users\\MX49954\\C&A_{nombres_hojas[i]}_results.xlsx"
    with pd.ExcelWriter(new_filename, engine='openpyxl') as writer:
        df_sum.to_excel(writer, sheet_name='Resultados', index=False)
        writer.book.save(new_filename)  # Save using the workbook directly


