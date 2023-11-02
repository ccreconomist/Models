import pandas as pd

# Load the data from the Excel file
nombre_archivo = "C:\\Users\\MX49954\\C&A-ONUS-TRAMITES.xlsx"
nombre_hoja = 'ONUS-C&a'
df = pd.read_excel(nombre_archivo, sheet_name=nombre_hoja)

# Display unique values in the 'FACTURADO' column
unique_facturado_values = df['FACTURADO'].round(2).unique()
print("Unique values in 'FACTURADO' column:")
print(unique_facturado_values)
