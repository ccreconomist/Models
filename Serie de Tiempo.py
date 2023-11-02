import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Crear una lista de fechas mensuales
fechas = pd.date_range(start='2022-01-01', periods=12, freq='M')

# Crear una lista de valores de ventas correspondientes
ventas = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# Crear un DataFrame de pandas con las fechas y las ventas
serie_de_tiempo = pd.DataFrame({'Fecha': fechas, 'Ventas': ventas})

# Establecer la fecha como el índice
serie_de_tiempo = serie_de_tiempo.set_index('Fecha')

plt.figure(figsize=(10, 5))
plt.plot(serie_de_tiempo['Ventas'])
plt.title('Serie de Tiempo de Ventas')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.show()

decomposition = sm.tsa.seasonal_decompose(serie_de_tiempo['Ventas'], model='additive')
tendencia = decomposition.trend
estacionalidad = decomposition.seasonal
residuos = decomposition.resid

plt.figure(figsize=(12, 8))

plt.subplot(411)
plt.plot(serie_de_tiempo['Ventas'], label='Ventas', color='blue')
plt.legend(loc='best')
plt.title('Serie de Tiempo Original')

plt.subplot(412)
plt.plot(tendencia, label='Tendencia', color='blue')
plt.legend(loc='best')
plt.title('Tendencia')

plt.subplot(413)
plt.plot(estacionalidad, label='Estacionalidad', color='blue')
plt.legend(loc='best')
plt.title('Estacionalidad')

plt.subplot(414)
plt.plot(residuos, label='Residuos', color='blue')
plt.legend(loc='best')
plt.title('Residuos')

plt.tight_layout()
plt.show()
