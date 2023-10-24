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
- `json_csv.py`: Este script procesa los archivos JSON generados por el raspador y los convierte en archivos CSV. Cada archivo JSON se lee, se extraen los datos relevantes del hilo (thread) y las respuestas, y estos datos se guardan en un archivo CSV individual.
- `emo_excel.py`: Este script realiza un análisis de sentimientos en los datos del archivo CSV 'Formatiado.csv'. Utiliza la biblioteca `sentiment_analysis_spanish` para analizar el sentimiento de cada texto en el DataFrame. Los resultados se guardan como un nuevo archivo CSV llamado 'Final.csv'. Luego, este archivo CSV se carga nuevamente en un DataFrame y se guarda como un archivo Excel llamado 'Final.xlsx' en la carpeta 'xlsx'.
