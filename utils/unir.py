import os
import pandas as pd

# Carpeta que contiene los archivos CSV
carpeta = 'coments'

# Lista para almacenar los DataFrames de cada archivo CSV
dataframes = []

# Recorre los archivos en la carpeta
for filename in os.listdir(carpeta):
    if filename.endswith('.csv'):
        # Carga cada archivo CSV en un DataFrame
        filepath = os.path.join(carpeta, filename)
        df = pd.read_csv(filepath)
        dataframes.append(df)

# Combina los DataFrames en uno solo
combined_df = pd.concat(dataframes, ignore_index=True)

# Guarda el DataFrame combinado en un archivo CSV
combined_csv = 'combined_data.csv'
combined_df.to_csv(combined_csv, index=False)

# Imprime la cantidad de filas en el DataFrame combinado
num_filas = len(combined_df)
print(f'Los archivos CSV se han combinado en {combined_csv}')
print(f'El DataFrame combinado tiene {num_filas} filas.')