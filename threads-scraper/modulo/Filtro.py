import json
import csv
import datetime

# Cargar el archivo JSON
with open('results/thread.json', 'r', encoding='utf-8') as file:
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
csv_filename = 'data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Texto', 'Fecha', 'Nombre de Usuario', 'Fuente']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'Texto': text, 'Fecha': published_on, 'Nombre de Usuario': nombre_usuario, 'Fuente': fuente})

    writer.writerows(replies_data)

print(f'Los datos se han guardado en {csv_filename}')
