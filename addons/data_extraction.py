import json
import datetime
from pathlib import Path
import csv

def obtener_datos_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def extraer_datos(data):
    thread_data = data['thread']
    text = thread_data['text']
    published_on_timestamp = thread_data['published_on']
    nombre_usuario = thread_data['username']
    fuente = thread_data['url']
    published_on = datetime.datetime.fromtimestamp(published_on_timestamp).strftime('%d-%m-%Y')
    return text, published_on, nombre_usuario, fuente

def extraer_respuestas(data, fuente):
    replies_data = []
    if 'replies' in data:
        replies = data['replies']
        for reply in replies:
            reply_text = reply['text']
            reply_published_on_timestamp = reply['published_on']
            reply_published_on = datetime.datetime.fromtimestamp(reply_published_on_timestamp).strftime('%d-%m-%Y')
            reply_username = reply['username']
            replies_data.append({
                'Texto': reply_text,
                'Fecha': reply_published_on,
                'Nombre Usuario': reply_username,
                'Fuente': fuente
            })
    return replies_data

def guardar_datos_csv(csv_filename, text, published_on, nombre_usuario, fuente, replies_data):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Texto', 'Fecha', 'Nombre Usuario', 'Fuente']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Texto': text, 'Fecha': published_on, 'Nombre Usuario': nombre_usuario, 'Fuente': fuente})
        writer.writerows(replies_data)

def procesar_archivos_json():
    json_files = Path('results').glob('*.json')
    for json_file in json_files:
        data = obtener_datos_json(json_file)
        text, published_on, nombre_usuario, fuente = extraer_datos(data)
        replies_data = extraer_respuestas(data, fuente)
        csv_filename = f'csv/{json_file.stem}.csv'
        guardar_datos_csv(csv_filename, text, published_on, nombre_usuario, fuente, replies_data)
        print(f'Los datos se han guardado en {csv_filename}')