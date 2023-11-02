import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

ruta_archivos = "C:\\Users\\MX49954\\Adq + Act-Pro.xlsx"
hoja_nombre = "Adq + Act"

# Cargar el archivo Excel en un DataFrame
datos = pd.read_excel(ruta_archivos, sheet_name=hoja_nombre)

# Agregar columnas "Date", "Año" y "Day"
datos['Date'] = pd.to_datetime(datos['Date'])
datos['Año'] = datos['Date'].dt.year
datos['Day'] = datos['Date'].dt.day

# Filtrar las columnas de interés
columnas_interes = ['Date', 'Año', 'Day', 'A-PLCC', 'A-BK']
datos_interes = datos[columnas_interes]

# Filtrar los datos para los años 2022 y 2023
datos_2022 = datos_interes[datos['Año'] == 2022]
datos_2023 = datos_interes[datos['Año'] == 2023]

# Calcular el Year-To-Date para ambos años
ytd_2022 = datos_2022.iloc[:, 3:].cumsum()
ytd_2023 = datos_2023.iloc[:, 3:].cumsum()

# Gráficos de líneas
plt.figure(figsize=(12, 16))

# Gráfico de líneas para totales A-PLCC
plt.subplot(3, 2, 1)
datos_2022.plot(x='Date', y='A-PLCC', ax=plt.gca(), label='A-PLCC 2022', marker='o')
datos_2023.plot(x='Date', y='A-PLCC', ax=plt.gca(), label='A-PLCC 2023', marker='o')
plt.title('A-PLCC Totales')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.legend()

# Gráfico de líneas para totales A-BK
plt.subplot(3, 2, 2)
datos_2022.plot(x='Date', y='A-BK', ax=plt.gca(), label='A-BK 2022', marker='x')
datos_2023.plot(x='Date', y='A-BK', ax=plt.gca(), label='A-BK 2023', marker='x')
plt.title('A-BK Totales')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.legend()

# Gráfico de líneas para porcentajes de crecimiento A-PLCC
plt.subplot(3, 2, 3)
crecimiento_plcc = datos_interes['A-PLCC'].pct_change() * 100
plt.plot(datos_interes['Date'], crecimiento_plcc, label='Crecimiento A-PLCC', marker='o')
plt.title('Porcentaje de Crecimiento Diario - A-PLCC')
plt.xlabel('Fecha')
plt.ylabel('Porcentaje')
plt.legend()

# Gráfico de líneas para porcentajes de crecimiento A-BK
plt.subplot(3, 2, 4)
crecimiento_bk = datos_interes['A-BK'].pct_change() * 100
plt.plot(datos_interes['Date'], crecimiento_bk, label='Crecimiento A-BK', marker='x')
plt.title('Porcentaje de Crecimiento Diario - A-BK')
plt.xlabel('Fecha')
plt.ylabel('Porcentaje')
plt.legend()

# Gráficos de tendencias A-PLCC y A-BK
plt.subplot(3, 1, 3)
tendencias = {}
for columna in ['A-PLCC', 'A-BK']:
    slope, _, _, _, _ = linregress(range(len(datos_interes)), datos_interes[columna])
    tendencias[columna] = slope
pd.Series(tendencias).plot(kind='bar', ax=plt.gca(), color=['blue', 'orange'])
plt.title('Tendencias A-PLCC y A-BK')
plt.xlabel('Columna')
plt.ylabel('Tasa de Cambio')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
