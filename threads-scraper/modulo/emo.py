import pandas as pd
from sentiment_analysis_spanish import sentiment_analysis

# Cargar el archivo CSV
df = pd.read_csv('Formatiado.csv')

# Inicializar el analizador de sentimientos
sentiment = sentiment_analysis.SentimentAnalysisSpanish()

# Reemplazar los valores NaN en la columna 'Texto' con una cadena vacía
df['Texto'] = df['Texto'].fillna('')

def sentiment_to_emotion(sentiment_score):
    if sentiment_score < 0.2:
        return 'Muy Negativo'
    elif sentiment_score < 0.4:
        return 'Negativo'
    elif sentiment_score < 0.6:
        return 'Neutral'
    elif sentiment_score < 0.8:
        return 'Positivo'
    else:
        return 'Muy Positivo'

# Aplicar el análisis de sentimientos a la columna 'Texto'
df['Concepto_asociado'] = df['Texto'].apply(lambda x: sentiment_to_emotion(sentiment.sentiment(x)))

# Guardar el DataFrame modificado como un nuevo archivo CSV
df.to_csv('Final.csv', index=False)
