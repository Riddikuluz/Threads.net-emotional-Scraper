import pandas as pd
import numpy as np  # Asegúrate de tener esta línea

# Carga tu archivo csv
df = pd.read_csv('final.csv')

# Divide el dataframe en tres partes iguales
dfs = np.array_split(df, 3)

# Guarda cada parte en un archivo csv distinto
for i, df in enumerate(dfs):
    df.to_csv(f'archivo_{i+1}.csv', index=False)
