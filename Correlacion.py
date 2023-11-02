import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel y nombre de la hoja
nombre_archivo = "C:\\Users\\MX49954\\C&A-ONUS.xlsx"
nombre_hoja = 'Hoja1'

# Carga de datos desde el archivo Excel
datos = pd.read_excel(nombre_archivo, sheet_name=nombre_hoja)

# Calcula la correlación entre las columnas 'Total general' y 'FACTURADO'
correlacion = datos['Total general'].corr(datos['FACTURADO'])
print('Correlación entre Total general y FACTURADO:', correlacion)

plt.text(100, 50, f'Correlación: {correlacion:.2f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))


# Crea un gráfico de dispersión
plt.scatter(datos['Total general'], datos['FACTURADO'], color='blue', label='Total General vs Facturado')

plt.xlabel('Total general (Trámites)')
plt.ylabel('FACTURADO')
plt.title('Gráfico de Dispersión: Total general vs FACTURADO')

# Agrega leyenda
plt.legend()
plt.show()





