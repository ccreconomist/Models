import pandas as pd
import matplotlib.pyplot as plt

ruta_archivos = "C:\\Users\\MX49954\\Historicos.xlsx"

datos = pd.read_excel(ruta_archivos, sheet_name="Hoja1")


datos['FECHA'] = pd.to_datetime(datos['FECHA'], format='%d/%m/%Y')


from numpy.polynomial.polynomial import Polynomial

x = datos.index
y = datos['FACTURA']


datos['TENDENCIA'] = coef(x)


ventana = 7
promedio_movil = datos['FACTURA'].rolling(window=ventana, min_periods=1).mean()


datos['PROMEDIO_MOVIL'] = promedio_movil

# Graficar los datos, la tendencia y el promedio móvil
plt.figure(figsize=(10, 6))
plt.plot(datos['FECHA'], datos['FACTURA'], label='Datos originales')
plt.plot(datos['FECHA'], datos['TENDENCIA'], label='Tendencia')
plt.plot(datos['FECHA'], datos['PROMEDIO_MOVIL'], label=f'Promedio móvil ({ventana} días)')
plt.xlabel('Fecha')
plt.ylabel('Factura')
plt.title('Análisis de Serie de Tiempo')
plt.legend()
plt.show()