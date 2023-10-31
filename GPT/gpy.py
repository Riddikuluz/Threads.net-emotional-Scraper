import os
import json
import requests
import time
import re
import pandas as pd
from dotenv import load_dotenv
import openai

load_dotenv()  # Toma las variables de entorno desde .env

# Obtener el valor de la clave de la API de OpenAI desde las variables de entorno
api_key = os.getenv("OPENAI_API_KEY")


sentimientos_permitidos = [
        "abandono", "abatimiento", "abrumamiento", "aburrimiento", "abuso", "aceptación",
        "acompañamiento", "admiración", "adoración", "afectación", "afecto", "aflicción",
        "agobio", "agradecimiento", "agravio", "agresión", "alarma", "alborozo", "alegría",
        "alivio", "alteración", "amabilidad", "amargura", "ambivalencia", "amor", "angustia",
        "anhelo", "ansiedad", "añoranza", "apatía", "apego", "apoyo", "aprobación", "armonía",
        "arrepentimiento", "arrogancia", "arrojo", "asco", "asombro", "atracción", "ausencia",
        "autonomía", "aversión", "benevolencia", "bondad", "calma", "cansancio", "cariño",
        "celos", "censura", "cercanía", "cólera", "compasión", "competencia", "comprensión",
        "compromiso", "concentración", "condescendencia", "confianza", "confusión", "congoja",
        "consideración", "consuelo", "contento", "contrariedad", "correspondencia", "cuidado",
        "culpa", "curiosidad", "decepción", "dependencia", "depresión", "derrota", "desaliento",
        "desamor", "desamparo", "desánimo", "desasosiego", "desconcierto", "desconfianza",
        "desconsideración", "desconsuelo", "desdén", "desdicha", "desencanto", "deseo",
        "desesperación", "desgano", "desidia", "desilusión", "desmotivación", "desolación",
        "desorientación", "desprecio", "desprestigio", "desprotección", "destrucción",
        "desvalimiento", "desventura", "devaluación", "dicha", "dignidad", "disforia",
        "disgusto", "diversión", "dolor", "dominación", "duda", "duelo", "ecuanimidad",
        "embelesamiento", "emoción", "empatía", "enamoramiento", "encanto", "enfado",
        "engaño", "enjuiciamiento", "enojo", "enternecimiento", "entusiasmo", "envidia",
        "espanto", "esperanza", "estima", "estremecimiento", "estupor", "euforia",
        "exaltación", "exasperación", "excitación", "expectativa", "éxtasis", "extrañeza",
        "fastidio", "felicidad", "fervor", "firmeza", "fobia", "fortaleza", "fracaso",
        "fragilidad", "frenesí", "frustración", "furia", "generosidad", "gozo", "gratitud",
        "hastío", "herida", "honestidad", "honorabilidad", "horror", "hostilidad", "humildad",
        "humillación", "ilusión", "impaciencia", "imperturbabilidad", "impotencia", "impresión",
        "incapacidad", "incomodidad", "incompatibilidad", "incomprensión", "inconformidad",
        "incongruencia", "incredulidad", "indiferencia", "indignación", "inestabilidad",
        "infelicidad", "inferioridad", "injusticia", "inquietud", "insatisfacción", "inseguridad",
        "insuficiencia", "integridad", "interés", "intimidad", "intolerancia", "intranquilidad",
        "intrepidez", "intriga", "invasión", "ira", "irritación", "jocosidad", "júbilo", "justicia",
        "lamento", "lástima", "libertad", "logro", "lujuria", "manipulación", "melancolía",
        "menosprecio", "mezquindad", "miedo", "molestia", "motivación", "necesidad", "nerviosismo",
        "nostalgia", "obligación", "obnubilación", "obstinación", "odio", "omnipotencia",
        "opresión", "optimismo", "orgullo", "ostentación", "paciencia", "pánico", "parálisis",
        "pasión", "pavor", "paz", "pena", "pereza", "persecución", "pertenencia", "pesadumbre",
        "pesimismo", "placer", "plenitud", "preocupación", "prepotencia", "pudor", "rabia",
        "rebeldía", "recelo", "rechazo", "regocijo", "remordimiento", "rencor", "repudio",
        "resentimiento", "reserva", "resignación", "respeto", "resquemor", "revelarse", "romance",
        "satisfacción", "seguridad", "serenidad", "simpatía", "soledad", "solidaridad", "sometimiento",
        "sorpresa", "sosiego", "suficiencia", "sumisión", "susto", "temor", "templanza", "tentación",
        "ternura", "terquedad", "terror", "timidez", "tolerancia", "traición", "tranquilidad",
        "tristeza", "triunfo", "turbación", "unidad", "vacilación", "vacío", "valentía", "valoración",
        "venganza", "verguenza", "violencia", "vulnerabilidad"
]

# Historial de conversación
conversation_history = []

# URL de la API de OpenAI
url = "https://api.openai.com/v1/chat/completions"
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}

def openai_init():
    try:
        # Texto de inicio de la conversación
        input_text = "Por favor, de un texto dado responde con un solo sentimiento de una lista que te daré, es decir, tu respuesta debe ser solo UNA PALABRA. Puede ser cualquier sentimiento de la lista de emociones proporcionada. El texto son comentarios o posts de Threads, una red social.\nLista de emociones:\n" + str(sentimientos_permitidos) + "\nPor ejemplo, si el texto es 'Estoy muy feliz', tu respuesta debe ser 'alegría'.\nSi no sabes que responder, solo escribe 'No sé'."
        
        # Agrega el mensaje del usuario al historial de conversación
        conversation_history.append({"role": "user", "content": input_text})
        
        # Llamada a la API de OpenAI para obtener la respuesta
        data = {
            "model": "gpt-3.5-turbo",
            "messages": conversation_history,
            "temperature": 0.7
        }
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            response = response.json()
            
            if "choices" not in response:
                print("Error en la llamada a la API de OpenAI")
                print("Respuesta de la API:", response)
                tiempo = response.get('estimated_completion_time', 5)
                time.sleep(tiempo + 1)
                
            # Agrega la respuesta del asistente al historial de conversación
            conversation_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
            print("Inicialización exitosa")
        else:
            print("Error en la llamada a la API de OpenAI")
            print("Respuesta de la API:", response)
    
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def obtener_sentimiento(texto):
    try:
        global conversation_history  # Accede a la variable global conversation_history

        # Agrega el mensaje del usuario al historial de conversación
        conversation_history.append({"role": "user", "content": texto})

        # Llamada a la API de OpenAI para obtener la respuesta
        data = {
            "model": "gpt-3.5-turbo",
            "messages": conversation_history,
            "temperature": 0.7
        }
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            response = response.json()
            
            if "choices" not in response:
                print("Error en la llamada a la API de OpenAI")
                print(response)
                tiempo = re.search(r'Please try again in (\d+) seconds.', response['error']['message']).group(1)
                time.sleep(int(tiempo) + 1)
                return obtener_sentimiento(texto)
            
            # Extraer el texto de la respuesta del asistente
            respuesta_asistente = response['choices'][0]['message']['content'].lower()

            # Agregar la respuesta del asistente al historial de conversación
            conversation_history.append({"role": "assistant", "content": respuesta_asistente})

            return respuesta_asistente
        else:
            return obtener_sentimiento(texto)

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def procesar_csv(nombre_archivo):
    try:
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(nombre_archivo, sep=',')

        # Verificar si la columna 'Texto' existe en el DataFrame
        if 'Texto' not in df.columns:
            print("El archivo CSV no tiene una columna 'Texto'.")
            return

        # Iterar a través de cada fila del DataFrame
        for index, row in df.iterrows():
            texto = row['Texto']
            sentimiento = row.get('Concepto asociado', None)

            if sentimiento is None or pd.isnull(sentimiento):
                print(f"Procesando fila {index}...")
                # Obtener el sentimiento del texto
                sentimiento = obtener_sentimiento(texto)

                # Agregar el sentimiento a la columna 'Concepto asociado'
                df.at[index, 'Concepto asociado'] = sentimiento
                print(f"Texto: {texto}\nSentimiento: {sentimiento}")

        # Guardar el DataFrame actualizado en un nuevo archivo CSV o sobrescribir el original
        df.to_csv(nombre_archivo, index=False)
        df.to_excel(f"{nombre_archivo.split('.csv')[0]}" + '.xlsx', index=False)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        df.to_csv(nombre_archivo, encoding="utf-8", index=False)
        df.to_excel(f"{nombre_archivo.split('.csv')[0]}" + '.xlsx', index=False)

if __name__ == "__main__":
    openai_init()
    procesar_csv("GPT/Final.csv")
    