# Importar las bibliotecas
import gspread
from google.colab import drive
from oauth2client.service_account import ServiceAccountCredentials

# Montar Google Drive
drive.mount('/content/drive')

# URL del archivo en Google Drive que deseas abrir (Google Sheets)
url = 'https://docs.google.com/spreadsheets/d/1t-5IJ-nEOGsM9jWy9nx7Hd4nok-c9GCUQb3to2qtvkU/edit?usp=sharing'

# Obtener el ID del archivo de Google Sheets desde la URL
file_id = url.split('/')[-2]

# Configurar las credenciales usando el archivo JSON en Google Drive
json_credentials_path = '/content/drive/your_path_to_credentials/client_secret.json'

# Configurar las credenciales
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_credentials_path, scope)
gc = gspread.authorize(credentials)

# Abrir el archivo de Google Sheets por ID
spreadsheet = gc.open_by_key(file_id)

# Acceder a una hoja específica (puedes cambiar el nombre de la hoja)
worksheet = spreadsheet.get_worksheet(0)

# Hacer algo con la hoja, por ejemplo, obtener los valores de la celda A1
cell_value = worksheet.acell('A1').value

# Imprimir el valor de la celda
print("Valor de la celda A1:", cell_value)
