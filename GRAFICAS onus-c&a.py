import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.ticker as mticker

# Ruta del archivo Excel y nombre de la hoja
nombre_archivo = "C:\\Users\\MX49954\\C&A-ONUS.xlsx"
nombre_hoja = 'Datos'

# Cargar datos desde el archivo Excel
df = pd.read_excel(nombre_archivo, sheet_name=nombre_hoja)

# Filtrar por el período específico (del 1/09/2023 al 31/10/2023)
df_filtered = df[(df['FECHA'] >= datetime(2023, 8, 1)) & (df['FECHA'] <= datetime(2023, 10, 15))]

# Llenar valores NaN en la columna FACTURADO con la media
df_filtered['FACTURADO'].fillna(df_filtered['FACTURADO'].mean(), inplace=True)

# Calcular el porcentaje de facturación (% Facturacion)
df_filtered['dif Facturacion'] = (df_filtered['FACTURADO'] / df_filtered['FACTURADO'].sum()) * 100

# Definición de las fechas a resaltar
fechas_resaltar = [
    (datetime(2023, 10, 10), datetime(2023, 10, 12), '10/10/2023 al 12/10/2023'),
    (datetime(2023, 9, 18), datetime(2023, 10, 1), '18/09/2023 al 01/10/2023'),
    (datetime(2023, 9, 16), datetime(2023, 9, 18), '16/09/2023 al 18/09/2023'),
    (datetime(2023, 8, 25), datetime(2023, 8, 27), '25/08/2023 al 27/08/2023'),
    (datetime(2023, 8, 18), datetime(2023, 8, 20), '18/08/2023 al 20/08/2023')
]

# Calcular la tendencia
fechas_num = np.arange(len(df_filtered['FECHA'])).reshape(-1, 1)
montos = df_filtered['FACTURADO'].values.reshape(-1, 1)

# Eliminar las filas que contienen NaN en montos
valid_indices = ~np.isnan(montos.flatten())
fechas_num = fechas_num[valid_indices]
montos = montos[valid_indices]

modelo = LinearRegression()
modelo.fit(fechas_num, montos)
tendencia = modelo.predict(fechas_num)


# Calcular la variación diaria en el monto facturado
df_filtered['Variacion'] = df_filtered['FACTURADO'].diff()

# Graficar los valores con línea continua y tendencia
plt.figure(figsize=(10, 5))
plt.plot(df_filtered['FECHA'], df_filtered['Variacion'], linestyle='-', color='purple', label='Variación Diaria')

# Graficar los valores con línea continua y tendencia
plt.figure(figsize=(10, 5))
plt.plot(df_filtered['FECHA'], df_filtered['FACTURADO'], linestyle='-', color='blue', label='Facturado')
plt.plot(df_filtered['FECHA'][valid_indices], tendencia, linestyle='--', color='red', label='Tendencia')

# Agregar la gráfica de % Facturacion
plt.plot(df_filtered['FECHA'], df_filtered['% Facturacion'], linestyle='-', color='green', label='% Facturacion')

for fecha_inicio, fecha_fin, etiqueta in fechas_resaltar:
    plt.axvspan(fecha_inicio, fecha_fin, color='gray', alpha=0.4)
    valor_etiqueta = df_filtered[(df_filtered['FECHA'] == fecha_inicio)]['FACTURADO'].values[0]
    plt.annotate(f'{etiqueta}\n${valor_etiqueta:,.1f}',
                 xy=(fecha_inicio, valor_etiqueta),
                 xytext=(fecha_inicio, valor_etiqueta + 10000000),
                 fontsize=8)

# Agregar punto en las fechas 18 de agosto y 18 de septiembre
plt.plot(datetime(2023, 8, 18), df_filtered[df_filtered['FECHA'] == datetime(2023, 8, 18)]['FACTURADO'].values[0], 'ro')
plt.plot(datetime(2023, 9, 18), df_filtered[df_filtered['FECHA'] == datetime(2023, 9, 18)]['FACTURADO'].values[0], 'ro')
plt.text(datetime(2023, 8, 18), df_filtered[df_filtered['FECHA'] == datetime(2023, 8, 18)]['FACTURADO'].values[0] - 10000000, 'FLP', color='red')

plt.xlabel('Fecha')
plt.ylabel('Variación Diaria')
plt.title('Variación Diaria en Monto Facturado')
plt.legend()

# Establecer las etiquetas de las fechas en el eje x
fecha_labels = [fecha.strftime('%d-%m-%Y') for fecha in df_filtered['FECHA']]
plt.xticks(df_filtered['FECHA'], fecha_labels, rotation=90)

plt.grid(False)  # Quitar las líneas cuadriculadas
plt.show()


