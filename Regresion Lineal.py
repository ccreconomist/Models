# Importa las bibliotecas necesarias
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Ejemplo de datos de ventas y variables predictoras
# Puedes reemplazar esto con tus propios datos
ventas = np.array([10, 20, 30, 40, 50])
publicidad = np.array([1, 2, 3, 4, 5])

# Convierte los datos de las variables predictoras a una matriz 2D (necesario para scikit-learn)
publicidad = publicidad.reshape(-1, 1)

# Crea un modelo de regresión lineal
modelo = LinearRegression()

# Ajusta el modelo a tus datos
modelo.fit(publicidad, ventas)

# Realiza una predicción utilizando el modelo
nueva_publicidad = np.array([[6]])  # Valor de la variable predictora para predecir
prediccion_ventas = modelo.predict(nueva_publicidad)

# Imprime la pendiente y la intersección en el eje y del modelo
print("Pendiente (coeficiente):", modelo.coef_)
print("Intersección en el eje y:", modelo.intercept_)

# Realiza una gráfica de los datos reales y la línea de regresión
plt.scatter(publicidad, ventas, color='b', label="Datos reales")
plt.plot(publicidad, modelo.predict(publicidad), color='r', label="Línea de regresión")
plt.xlabel("Gasto en Publicidad")
plt.ylabel("Ventas")
plt.legend()
plt.show()

# Realiza una predicción
print("Predicción de ventas para un gasto en publicidad de 6:", prediccion_ventas[0])
