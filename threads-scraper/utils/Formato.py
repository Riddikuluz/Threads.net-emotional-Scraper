import pandas as pd
from sentiment_analysis_spanish import sentiment_analysis
# Lee el CSV original
df = pd.read_csv('combined_data.csv')

# Realiza la transformación de columnas
df.rename(columns={'Fecha': 'Fecha', 'Nombre de Usuario': 'Nombre Usuario', 'Fuente': 'Fuente'}, inplace=True)
df['Concepto_asociado'] = 'N/E'  # Agrega la columna Concepto asociado
df['Género'] = 'N/E'  # Agrega la columna Género
df['Grupo_Étareo'] = 'N/E'  # Agrega la columna Grupo Étareo
df['Escolaridad'] = 'N/E'  # Agrega la columna Escolaridad

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('Formatiado.csv', index=False)
