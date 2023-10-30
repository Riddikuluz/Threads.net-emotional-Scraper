import pandas as pd
from pathlib import Path

def transformar_datos(df):
    df.rename(columns={'Fecha': 'Fecha', 'Nombre de Usuario': 'Nombre Usuario', 'Fuente': 'Fuente'}, inplace=True)
    df['Concepto_asociado'] = 'N/E'
    df['Género'] = 'N/E'
    df['Grupo_Étareo'] = 'N/E'
    df['Escolaridad'] = 'N/E'
    return df

def procesar_archivos_csv():
    csv_files = Path('csv').glob('*.csv')
    all_data = pd.DataFrame()
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df_transformado = transformar_datos(df)
        all_data = pd.concat([all_data, df_transformado], ignore_index=True)
    all_data.to_csv('csv/Formatiado.csv', index=False)
    print('Los datos se han guardado en csv/Formatiado.csv')
