import pandas as pd
import data_extraction
import data_transformation
import sentiment_analysis
import data_storage

# Procesar archivos JSON
data_extraction.procesar_archivos_json()

# Procesar archivos CSV
data_transformation.procesar_archivos_csv()

# Procesar archivos Formatiado
df_formatiado = pd.read_csv('csv/Formatiado.csv')
sentiment_analysis.analisis_sentimientos(df_formatiado)

# Guardar datos en Excel
data_storage.guardar_datos(df_formatiado)