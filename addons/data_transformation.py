import pandas as pd
from pathlib import Path
import re

def transformar_datos(df):
    df['Concepto asociado'] = 'N/E'
    df['Género'] = 'N/E'
    df['Grupo Étareo'] = 'N/E'
    df['Escolaridad'] = 'N/E'
    return df
    
def procesar_archivos_csv():
    csv_files = Path('csv').glob('*.csv')
    all_data = pd.DataFrame()
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        # Eliminar las filas con 'Texto' vacío
        df = df[df['Texto'].notna()]
        # Eliminar los enlaces del 'Texto'
        df['Texto'] = df['Texto'].apply(lambda x: re.sub(r'http\S+|www.\S+', '', x, flags=re.MULTILINE))
        # Eliminar las filas que solo contienen emojis
        df = df[df['Texto'].str.contains(r'[a-zA-Z0-9]')]
        df = df[df['Texto'].str.len() >= 10]
        # Filtrar filas con texto que cumple el patrón
        patron = r'\b\w+\b [^\W\d_]+ \w+\b'
        df = df[df['Texto'].str.match(patron, na=False)]
        # Elimina las filas donde la columna 'Texto' contiene un hashtag o un arroba
        df = df[~df['Texto'].str.contains('#')]
        df = df[~df['Texto'].str.contains('@')]
        df_transformado = transformar_datos(df)
        df_transformado = df_transformado.sort_values(by=['Texto', 'Fecha', 'Nombre Usuario', 'Fuente', 'Concepto asociado', 'Género', 'Grupo Étareo', 'Escolaridad'])
        all_data = pd.concat([all_data, df_transformado], ignore_index=True)
    # Eliminar duplicados
    all_data.drop_duplicates(inplace=True)
    all_data.to_csv('csv/Formatiado.csv', index=False)
    print('Los datos se han guardado en csv/Formatiado.csv')

