import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA

# Cargar los datos desde el archivo Excel
ruta_archivo = 'C:\\Users\\MX49954\\BC-cines2.xlsx'
datos = pd.read_excel(ruta_archivo)

# Configurar las columnas de fecha y datos para el análisis
datos['FECHA_CONSUMO'] = pd.to_datetime(datos['FECHA_CONSUMO'])
datos.set_index('FECHA_CONSUMO', inplace=True)
serie_temporal = datos['Suma_IMP_DESTINO']

# Visualización de datos
plt.plot(serie_temporal)
plt.title("Serie Temporal de Suma_IMP_DESTINO")
plt.show()

# Descomposición de serie de tiempo
decomposition = seasonal_decompose(serie_temporal, model='multiplicative')
tendencia = decomposition.trend
estacionalidad = decomposition.seasonal
ruido = decomposition.resid

# Ajuste del modelo ARIMA
modelo = ARIMA(serie_temporal, order=(p, d, q))
modelo_ajustado = modelo.fit(disp=-1)

# Pronóstico
pronostico = modelo_ajustado.forecast(steps=numero_de_pronostico)

# Visualizar el pronóstico
plt.plot(serie_temporal, label='Datos originales')
plt.plot(pronostico, color='red', label='Pronóstico')
plt.legend()
plt.title("Pronóstico utilizando ARIMA")
plt.show()
