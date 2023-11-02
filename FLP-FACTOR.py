import pandas as pd

# Ruta del archivo Excel y nombre de la hoja
nombre_archivo = "C:\\Users\\MX49954\\C&A-ONUS.xlsx"
nombre_hoja = 'Datos'
df = pd.read_excel(nombre_archivo, sheet_name=nombre_hoja)

# Fechas a analizar (formato día/mes/año)
fechas_a_analizar = ['18/01/2023', '18/02/2023', '18/03/2023', '18/04/2023', '18/05/2023', '18/06/2023', '18/07/2023',
                     '18/08/2023', '18/09/2023']

# Inicializar una lista para almacenar el crecimiento de la facturación para cada fecha
crecimiento_por_fecha = []

# Calcular el crecimiento de la facturación para cada fecha
for fecha in fechas_a_analizar:
    # Convertir la fecha al formato que utiliza el DataFrame
    fecha_formato_dataframe = pd.to_datetime(fecha, format='%d/%m/%Y', dayfirst=True)

    # Filtrar los datos para la fecha actual
    datos_fecha_actual = df[df['FECHA'] == fecha_formato_dataframe]

    # Verificar si hay datos para la fecha actual
    if not datos_fecha_actual.empty:
        # Calcular el crecimiento para "FACTURADO"
        crecimiento_facturado = ((datos_fecha_actual['FACTURADO'].values[-1] - datos_fecha_actual['FACTURADO'].values[0]) /
                                datos_fecha_actual['FACTURADO'].values[0]) * 100

        # Agregar el crecimiento a la lista
        crecimiento_por_fecha.append((fecha, crecimiento_facturado))
    else:
        crecimiento_por_fecha.append((fecha, "No hay datos"))

# Imprimir el crecimiento de la facturación para cada fecha
print("\nCrecimiento de la facturación para cada fecha:")
for fecha, crecimiento_facturado in crecimiento_por_fecha:
    print(f"Fecha: {fecha}")
    print(f"Crecimiento Facturado: {crecimiento_facturado if crecimiento_facturado != 'No hay datos' else 'No hay datos disponibles'}")
    print()

