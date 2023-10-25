import pandas as pd
from sentiment_analysis_spanish import sentiment_analysis

def analisis_sentimientos(df):
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
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

    df['Concepto_asociado'] = df['Texto'].apply(lambda x: sentiment_to_emotion(sentiment.sentiment(x)))
    
def procesar_archivos_formatiado():
    df_formatiado = pd.read_csv('csv/Formatiado.csv')
    analisis_sentimientos(df_formatiado)
