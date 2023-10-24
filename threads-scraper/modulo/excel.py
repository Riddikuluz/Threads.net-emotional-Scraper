import pandas as pd

# Lista de tus archivos csv
archivos_csv = ['archivo_1.csv', 'archivo_2.csv', 'archivo_3.csv']

for archivo in archivos_csv:
    # Carga el archivo csv
    df = pd.read_csv(archivo)

    # Guarda el dataframe en un archivo Excel
    df.to_excel(archivo.replace('.csv', '.xlsx'), index=False)
