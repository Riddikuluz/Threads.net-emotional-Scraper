import pandas as pd
import csv  # Importa la biblioteca csv

# Nombre de tu archivo CSV
csv_file = "Formatiado.csv"

try:
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        is_valid = True  # Suponemos que el archivo es válido hasta que encontremos un problema
        line_number = 1

        for row in reader:
            # Verificamos si el número de campos en la fila es impar
            if len(row) % 2 != 0:
                print(f"La fila {line_number} tiene un número impar de campos.")
                is_valid = False

            line_number += 1

        if is_valid:
            print("El archivo CSV parece estar bien formateado y no tiene filas con un número impar de campos.")

except Exception as e:
    print("Error al abrir el archivo CSV:", str(e))
