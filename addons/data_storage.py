import pandas as pd

def guardar_datos(df):
    df.to_excel('xlsx/Final.xlsx', index=False)
    df.to_csv('csv/Final.csv', index=False)
    print('Los datos se han guardado en xlsx/Final.xlsx y csv/Final.csv')
