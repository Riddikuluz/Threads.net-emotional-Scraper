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

A continuación, se detallan las dependencias que debes instalar utilizando Poetry:

1. **Poetry (Gestor de Dependencias)**
   ```bash
   pip install poetry
   ```

2. **Dependencias del Proyecto (Ejecutar en el directorio del proyecto)**
   ```bash
   poetry install
   ```

3. **Dependencias del Proyecto (Ejecutar en el directorio del proyecto con un entorno virtual creado por Poetry)**
   ```bash
   poetry add aiohttp
   poetry add bs4
   poetry add pandas
   poetry add pysentimiento
   ```

Asegúrate de ejecutar estos comandos en el entorno virtual de Poetry creado para tu proyecto. Si el código utiliza alguna biblioteca personalizada, debes asegurarte de agregarla también utilizando `poetry add`.

Recuerda que también necesitarás tener Python instalado en tu entorno, en mi caso estoy usando python-3.11.6.

## Uso
1. Clona el repositorio en tu máquina local.
2. Configura la clave de API de Scrapfly según se describe en los prerrequisitos.
3. Ejecuta el script:
   ```bash
   poetry run python run.py
   ```

## Detalles del Script
### `run.py`
Este script inicia el scraper de Threads.net y guarda los resultados en el directorio `./results/`. Incluye una lista de URLs de ejemplo para hacer scraping. Puedes agregar más URLs según sea necesario.

### `addons/main.py`
Este script procesa archivos JSON, realiza extracción de datos, transformación, análisis de sentimientos y almacena los datos finales en formato Excel.

### `addons/data_extraction.py`
Este módulo proporciona funciones para extraer datos de archivos JSON.

### `addons/data_transformation.py`
Este módulo transforma datos, agregando columnas adicionales con valores predeterminados.

### `addons/sentiment_analysis.py`
Este módulo analiza el sentimiento del texto utilizando la biblioteca PySentimiento.

### `addons/data_storage.py`
Este módulo maneja el almacenamiento de los datos finales en formato Excel.

## Instrucciones
1. Ejecuta `poetry run python run.py` para recopilar datos de Threads.net. Asegúrate de haber agregado las URLs previamente en la variable `urls` dentro del archivo `run.py`.
2. Encuentra los resultados finales en el archivo `xlsx/Final.xlsx`.
