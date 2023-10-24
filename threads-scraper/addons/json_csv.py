import json
import csv
import datetime
from pathlib import Path
import pandas as pd

# Obtener la lista de archivos JSON en la carpeta 'results'
json_files = Path('results').glob('*.json')

for json_file in json_files:
    # Cargar el archivo JSON
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extraer los datos relevantes de la publicación principal (thread)
    thread_data = data['thread']
    text = thread_data['text']
    published_on_timestamp = thread_data['published_on']
    nombre_usuario = thread_data['username']
    fuente = thread_data['url']

    # Convertir la marca de tiempo en una fecha y hora legible
    published_on = datetime.datetime.fromtimestamp(published_on_timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Inicializar una lista para almacenar las respuestas
    replies_data = []

    # Verificar si hay respuestas y, si es así, extraer y guardar los datos de cada respuesta
    if 'replies' in data:
        replies = data['replies']
        for reply in replies:
            reply_text = reply['text']
            reply_published_on_timestamp = reply['published_on']
            reply_published_on = datetime.datetime.fromtimestamp(reply_published_on_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            reply_username = reply['username']
            replies_data.append({
                'Texto': reply_text,
                'Fecha': reply_published_on,
                'Nombre de Usuario': reply_username,
                'Fuente': fuente
            })

    # Guardar los datos en un archivo CSV con codificación UTF-8
    csv_filename = f'csv/{json_file.stem}.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Texto', 'Fecha', 'Nombre de Usuario', 'Fuente']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerow({'Texto': text, 'Fecha': published_on, 'Nombre de Usuario': nombre_usuario, 'Fuente': fuente})

        writer.writerows(replies_data)

    print(f'Los datos se han guardado en {csv_filename}')

# Obtener la lista de archivos CSV en la carpeta 'csv'
csv_files = Path('csv').glob('*.csv')

# Inicializar un DataFrame vacío para almacenar todos los datos
all_data = pd.DataFrame()

for csv_file in csv_files:
    # Lee el archivo CSV
    df = pd.read_csv(csv_file)

    # Realiza la transformación de columnas
    df.rename(columns={'Fecha': 'Fecha', 'Nombre de Usuario': 'Nombre Usuario', 'Fuente': 'Fuente'}, inplace=True)
    df['Concepto_asociado'] = 'N/E'  # Agrega la columna Concepto asociado
    df['Género'] = 'N/E'  # Agrega la columna Género
    df['Grupo_Étareo'] = 'N/E'  # Agrega la columna Grupo Étareo
    df['Escolaridad'] = 'N/E'  # Agrega la columna Escolaridad

    # Añade los datos al DataFrame principal
    all_data = pd.concat([all_data, df], ignore_index=True)

# Guarda el DataFrame modificado en un nuevo archivo CSV
all_data.to_csv('csv/Formatiado.csv', index=False)

print('Los datos se han guardado en csv/Formatiado.csv')
