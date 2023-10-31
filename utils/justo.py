import pandas as pd

# Carga el archivo csv
df = pd.read_csv('csv/Final.csv')

# Conserva solo las primeras 450 filas
df = df.iloc[:451]

# Guarda el dataframe en un nuevo archivo csv
df.to_csv('csv/Final_reducido.csv', index=False)
