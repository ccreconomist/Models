import pandas as pd
from openpyxl import load_workbook

# Ruta y nombre del archivo principal
nombre_archivo_principal = "C:\\Users\\MX49954\\C&A-NUEVO.xlsx"
nombre_hoja1 = 'BASE-22-23'
df_union = pd.read_excel(nombre_archivo_principal, sheet_name=nombre_hoja1)

# Filtrar por el periodo de interés (01/09/2022 al 01/09/2023)
start_date = '2022-09-01'
end_date = '2023-09-01'
df_filtered = df_union[(df_union['DAT_ATIVACAO_CTAF'] >= start_date) & (df_union['DAT_ATIVACAO_CTAF'] < end_date)]

# Agrupar por 'CuentaReal' y sumar 'MONTOREAL'
df_resumen = df_filtered.groupby('CuentaReal')['MONTOREAL'].sum().reset_index()

# Agregar tres ceros al inicio de la columna 'CuentaReal' y asegurarse de que sea texto
df_resumen['CuentaReal'] = '000' + df_resumen['CuentaReal'].astype(str)

# Merge the 'df_resumen' with 'df_filtered' to bring the date of activation
df_resumen = pd.merge(df_resumen, df_filtered[['CuentaReal', 'DAT_ATIVACAO_CTAF']], on='CuentaReal', how='left')

# Drop duplicates and reset the index
df_resumen = df_resumen.drop_duplicates().reset_index(drop=True)

# Escribir el DataFrame resumen en una nueva hoja llamada 'RESUMEN1'
with pd.ExcelWriter(nombre_archivo_principal, engine='openpyxl', mode='a') as writer:
    df_resumen.to_excel(writer, sheet_name='RESUMEN1', index=False)

    # Guardar el libro de trabajo
    writer.save()

