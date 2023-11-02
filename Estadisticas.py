import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

# Cargar los datos
ruta_archivo = 'C:\\Users\\MX49954\\Conjuntos.xlsx'
hoja_2022 = pd.read_excel(ruta_archivo, sheet_name="Datos_2022")
hoja_2023 = pd.read_excel(ruta_archivo, sheet_name="Datos_2023")

hoja_2022['FECHA_CONSUMO'] = pd.to_datetime(hoja_2022['FECHA_CONSUMO'])
hoja_2023['FECHA_CONSUMO'] = pd.to_datetime(hoja_2023['FECHA_CONSUMO'])

# Cálculos estadísticos
promedio_2022 = hoja_2022['IMP_DESTINO'].mean()
total_2023 = hoja_2023['IMP_DESTINO'].sum()

# Correlaciones
correlaciones_2022 = hoja_2022.corr()


