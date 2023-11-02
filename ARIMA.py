import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Datos de ejemplo (fechas y valores)
fechas = pd.date_range(start='2020-01-01', periods=12, freq='M')
ventas = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]

# Crear una serie de tiempo a partir de los datos
serie_temporal = pd.Series(ventas, index=fechas)

# Ajustar el modelo ARIMA (por ejemplo, ARIMA(1,1,1))
modelo_arima = ARIMA(serie_temporal, order=(1, 1, 1))
modelo_arima_fit = modelo_arima.fit()

# Resumen del modelo ARIMA
print(modelo_arima_fit.summary())

# Visualizar resultados del ajuste
modelo_arima_fit.plot_predict(dynamic=False)
plt.show()

# Hacer predicciones para el futuro (por ejemplo, para los próximos 12 meses)
predicciones = modelo_arima_fit.forecast(steps=12)
print("Predicciones para los próximos 12 meses:")
print(predicciones)



