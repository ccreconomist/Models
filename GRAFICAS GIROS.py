import matplotlib.pyplot as plt

# Datos proporcionados
categorias = ['Otros', 'Supermercado', 'On Line', 'Agregador', 'Departamental', 'Ropa', 'Telefonía', 'Conveniencia',
              'Farmcias', 'Servicios', 'Entretenimiento', 'Uber / Didi / Rappi', 'Aerolínea', 'Calzado', 'Gasolinera',
              'Airbnb', 'Autobuses', 'Restaurante']

ingresos_2021 = [969851314, 408599729, 245822936, 86086322, 97125216, 77625481, 85423388, 41149079, 37306789, 46814565,
                 36773671, 73467025, 29784852, 15806611, 12869037, 5516296, 5809198, 3217042]

ingresos_2022 = [1499403941, 631217763, 251100071, 165994921, 154945134, 125448366, 77131968, 77783470, 54926231, 46462485,
                 44412580, 41417087, 31085321, 22855963, 22198932, 9958988, 2590888, 4344719]

ingresos_2023 = [1477237782, 591771095, 286104062, 213376220, 147266174, 137690562, 69855823, 68792418, 55042121, 51227667,
                 40492860, 38910816, 29803815, 20892518, 20679422, 9559229, 6871498, 4526758]

# Crear gráfico de barras horizontales para mostrar los ingresos por categoría
plt.figure(figsize=(12, 10))

plt.barh(categorias, ingresos_2021, label='2021')
plt.barh(categorias, ingresos_2022, left=ingresos_2021, label='2022')
plt.barh(categorias, ingresos_2023, left=[a + b for a, b in zip(ingresos_2021, ingresos_2022)], label='2023')

plt.xlabel('Ingresos (en pesos)')
plt.ylabel('Giro')
plt.title('Ingresos por categoría (2021-2023)')
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()






