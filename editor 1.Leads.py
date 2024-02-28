import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Definir la ruta de la carpeta de destino
carpeta_destino = r'W:\Automatizacion Leads\PS'

# Configurar las credenciales del servicio
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('tu-archivo-de-credenciales.json', scope)
cliente = gspread.authorize(creds)

# Abrir la hoja de cálculo por URL
url_hoja_calculo = 'https://docs.google.com/spreadsheets/d/1t-5IJ-nEOGsM9jWy9nx7Hd4nok-c9GCUQb3to2qtvkU/edit#gid=0'
hoja_calculo = cliente.open_by_url(url_hoja_calculo)

# Descargar el archivo en formato Excel
contenido_excel = hoja_calculo.sheet1.get_all_values()
nombre_archivo = 'hoja_calculo_descargada.xlsx'
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

with open(ruta_completa, 'w') as archivo_excel:
    for fila in contenido_excel:
        archivo_excel.write('\t'.join(fila) + '\n')

print(f'Hoja de cálculo descargada y guardada en: {ruta_completa}')
