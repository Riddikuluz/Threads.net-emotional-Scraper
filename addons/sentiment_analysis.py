import pandas as pd
from pysentimiento import create_analyzer

def translate_emotion_to_spanish(emotion):
    translations = {
        'joy': 'alegría',
        'surprise': 'sorpresa',
        'sadness': 'tristeza',
        'fear': 'miedo',
        'anger': 'enojo',
        'disgust': 'asco'
    }
    return translations.get(emotion, emotion)

emotion_analyzer  = create_analyzer(task="emotion", lang="es")

def analisis_sentimientos(df):
    df['Texto'] = df['Texto'].fillna('')
    
    def sentiment_to_emotion(sentiment_score):
        result = emotion_analyzer.predict(sentiment_score)
        if result.output == 'others':
            del result.probas['others']
            max_emotion = max(result.probas, key=result.probas.get)
        
            return translate_emotion_to_spanish(max_emotion)
        else:
            return translate_emotion_to_spanish(result.output)

    df['Concepto_asociado'] = df['Texto'].apply(sentiment_to_emotion)

    
def procesar_archivos_formatiado():
    df_formatiado = pd.read_csv('csv/Formatiado.csv')
    analisis_sentimientos(df_formatiado)
