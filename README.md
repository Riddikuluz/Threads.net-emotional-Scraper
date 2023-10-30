# Threads.net Scraper

Este raspador utiliza [scrapfly.io](https://scrapfly.io/) y Python para raspar los datos de las publicaciones y perfiles de Threads.net.

El código de raspado se encuentra en el archivo `threads.py`. Está completamente documentado y simplificado con fines educativos y el código de ejemplo del raspador se puede encontrar en el archivo `run.py`.

Este raspador raspa:
- Datos del hilo (también conocido como publicación) de Threads.net
- Datos del perfil de Threads.net

Para ver ejemplos de salida, consulte el directorio `./results`.

Nota: Este raspador solo raspa datos públicos de Threads que no requieren un inicio de sesión para acceder.

## Descargo de responsabilidad de uso justo

Tenga en cuenta que este código se proporciona de forma gratuita tal cual, y Scrapfly __no__ proporciona soporte gratuito para raspado web o consulta. Para cualquier error, consulte el rastreador de problemas.

## Configuración y uso

Este raspador de Threads.net utiliza __Python 3.10__ con el paquete [scrapfly-sdk](https://pypi.org/project/scrapfly-sdk/) que se utiliza para raspar y analizar los datos de Threads.

0. Asegúrese de tener __Python 3.10__ y el [gestor de paquetes Python poetry](https://python-poetry.org/docs/#installation) en su sistema.
1. Recupere su clave API Scrapfly desde <https://scrapfly.io/dashboard> y configure la variable de entorno `SCRAPFLY_KEY`:
    ```shell
    $ export SCRAPFLY_KEY="SU CLAVE SCRAPFLY"
    ```
    o en el PowerShell en el caso de Windows:
   ```shell
    $ export SCRAPFLY_KEY="SU CLAVE SCRAPFLY"
    ```
2. Clone e instale el entorno Python:
    ```shell
    $ git clone https://github.com/scrapfly/scrapfly-scrapers.git
    $ cd scrapfly-scrapers/threads-scraper
    $ poetry install
    $ pip install openpyxl sentiment-analysis-spanish scrapfly-sdk playwright nested_lookup jmespath "scrapfly-sdk[all]"
    ```
3. Ejecute el raspado de ejemplo:
    ```shell
    $ poetry run python run.py
    ```
4. Ejecute las pruebas:
    ```shell
    $ poetry install --with dev
    $ poetry run pytest test.py
    # o áreas específicas de raspado
    $ poetry run pytest test.py -k test_thread_scraping
    $ poetry run pytest test.py -k test_user_scraping
    ```
 5. Ejecute el raspado, agregando urls al archivo run.py:
      ```shell
    urls = [
    "https://www.threads.net/@liberalesargentinaok/post/CyMS-ONuuaU",
    "https://www.threads.net/@lanatappt/post/CyvjalRg-vx",
    "https://www.threads.net/@lanatappt/post/CyuKPeasna5"  # Ejemplos
    # Agrega más URLs aquí...
    ]
    ```
    Para posteriormente, ejecutar el script:
    ```shell
    $ poetry run python run.py
    ```

Además, este proyecto incluye tres scripts adicionales que procesan los datos extraídos por el raspador:

- `run.py`: Este script ejecuta el raspador en una lista predefinida de URLs y guarda los resultados en archivos JSON individuales en el directorio ./results. También ejecuta dos scripts adicionales, 'json_csv.py' y 'emo_excel.py', que están ubicados en el directorio /addons.
Claro, aquí tienes un breve resumen de cada archivo `.py` que se creó:

1. **data_extraction.py**: Este archivo contiene funciones para extraer datos de archivos JSON. Las funciones incluyen `obtener_datos_json` para leer un archivo JSON, `extraer_datos` para extraer datos específicos de los datos JSON, `extraer_respuestas` para extraer respuestas de los datos JSON y `guardar_datos_csv` para guardar los datos extraídos en un archivo CSV. La función `procesar_archivos_json` procesa todos los archivos JSON en el directorio 'results'.

2. **data_transformation.py**: Este archivo contiene funciones para transformar los datos extraídos. La función `transformar_datos` renombra las columnas del DataFrame y añade nuevas columnas. La función `procesar_archivos_csv` procesa todos los archivos CSV en el directorio 'csv' y guarda los datos transformados en 'csv/Formatiado.csv'.

3. **sentiment_analysis.py**: Este archivo contiene funciones para realizar un análisis de sentimientos en los datos transformados. La función `analisis_sentimientos` aplica un análisis de sentimientos a la columna 'Texto' del DataFrame y guarda los resultados en la columna 'Concepto_asociado'. La función `procesar_archivos_formatiado` lee el archivo 'csv/Formatiado.csv', aplica el análisis de sentimientos y guarda los resultados.

4. **data_storage.py**: Este archivo contiene la función `guardar_datos_excel` para guardar el DataFrame final en un archivo Excel.

5. **main.py**: Este es el archivo principal que importa y utiliza las funciones de los otros archivos para realizar todo el proceso desde la extracción de datos hasta el almacenamiento de los resultados.

Espero que esto te ayude a entender mejor la estructura del código. ¡Buena suerte con tu proyecto! 😊