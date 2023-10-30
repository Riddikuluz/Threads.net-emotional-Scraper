import pandas as pd

def guardar_datos_excel(df):
    df.to_excel('xlsx/Final.xlsx', index=False)
    print('Los datos se han guardado en xlsx/Final.xlsx')
