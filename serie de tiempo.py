import matplotlib.pyplot as plt

# Datos proporcionados
fechas = ["ene-22", "feb-22", "mar-22", "abr-22", "may-22", "jun-22", "jul-22", "ago-22", "sep-22", "oct-22", "nov-22", "dic-22", "ene-23", "feb-23", "mar-23", "abr-23", "may-23", "jun-23", "jul-23"]
valores = [4547, 5218, 5720, 6248, 7123, 6868, 7668, 7267, 7496, 6704, 7814, 7618, 3416, 3164, 3489, 3560, 4538, 4126, 4405]

# Crear la gráfica de líneas
plt.figure(figsize=(10, 6))
plt.plot(fechas, valores, marker='o', color='green')
plt.title('Gráfica de Líneas')
plt.xlabel('Fechas')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Mostrar la gráfica
plt.show()
