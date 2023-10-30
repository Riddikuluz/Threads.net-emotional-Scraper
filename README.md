# Scraper de Threads.net

## Descripción
Este repositorio contiene un script en Python que muestra cómo utilizar el scraper de Threads.net para recopilar datos de productos e información de búsqueda de productos. El script utiliza la API de Threads.net a través del servicio Scrapfly. Los resultados se guardan en el directorio `./results/`.

## Prerrequisitos
Antes de ejecutar el script, asegúrate de tener la clave de API de Scrapfly. Configura la variable de entorno `$SCRAPFLY_KEY` con tu clave de API de Scrapfly:

### Linux/Mac
```bash
export SCRAPFLY_KEY="tu clave desde https://scrapfly.io/dashboard"
```

### Windows
```powershell
$env:SCRAPFLY_KEY="tu clave desde https://scrapfly.io/dashboard"
```

## Uso
1. Clona el repositorio en tu máquina local.
2. Configura la clave de API de Scrapfly según se describe en los prerrequisitos.
3. Ejecuta el script:
   ```bash
   python scraper.py
   ```

## Detalles del Script
### `scraper.py`
Este script inicia el scraper de Threads.net y guarda los resultados en el directorio `./results/`. Incluye una lista de URLs de ejemplo para hacer scraping. Puedes agregar más URLs según sea necesario.

### `addons/main.py`
Este script procesa archivos JSON, realiza extracción de datos, transformación, análisis de sentimientos y almacena los datos finales en formato Excel.

### `data_extraction.py`
Este módulo proporciona funciones para extraer datos de archivos JSON.

### `data_transformation.py`
Este módulo transforma datos, agregando columnas adicionales con valores predeterminados.

### `sentiment_analysis.py`
Este módulo analiza el sentimiento del texto utilizando la biblioteca PySentimiento.

### `data_storage.py`
Este módulo maneja el almacenamiento de los datos finales en formato Excel.

## Instrucciones
1. Ejecuta `scraper.py` para recopilar datos de Threads.net.
2. Ejecuta `addons/main.py` para procesar y analizar los datos recopilados.
3. Encuentra los resultados finales en el archivo `xlsx/Final.xlsx`.