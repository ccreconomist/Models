import matplotlib.pyplot as plt

# Crear una figura para la gráfica de bigotes
plt.figure(figsize=(10, 5))

# Graficar la variación diaria en el monto facturado utilizando un boxplot
plt.boxplot(df_filtered['Variacion'], vert=False, labels=['Variación Diaria'], patch_artist=True,
            boxprops=dict(facecolor='purple', color='purple'))

# Agregar punto en las fechas 18 de agosto y 18 de septiembre
plt.plot(df_filtered[df_filtered['FECHA'] == datetime(2023, 8, 18)]['Variacion'], 1, 'ro')
plt.plot(df_filtered[df_filtered['FECHA'] == datetime(2023, 9, 18)]['Variacion'], 1, 'ro')
plt.text(df_filtered[df_filtered['FECHA'] == datetime(2023, 8, 18)]['Variacion'].values[0] - 20000000, 1, 'FLP', color='red')

# Establecer el título y etiquetas de los ejes
plt.title('Variación Diaria en Monto Facturado')
plt.xlabel('Variación Diaria')
plt.yticks([])  # Quitar etiquetas del eje y

plt.grid(False)  # Quitar las líneas cuadriculadas
plt.show()

