"""
This example run script shows how to run the Threads.net scraper defined in ./threads.py
It scrapes product data and product search and saves it to ./results/

To run this script set the env variable $SCRAPFLY_KEY with your scrapfly API key:
$ export $SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
 
On windows terminal: 
$env:SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
"""
from pathlib import Path
import asyncio
import json
import threads
import subprocess

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)

# Lista de URLs a leer
urls = [
    "https://www.threads.net/@liberalesargentinaok/post/CyMS-ONuuaU",
    "https://www.threads.net/@lanatappt/post/CyvjalRg-vx",# Ejemplos
    # Agrega más URLs aquí...
]

async def run():
    threads.BASE_CONFIG["debug"] = True

    print("running Threads scrape and saving results to ./results directory")
    
    for i, url in enumerate(urls):
        thread = await threads.scrape_thread(url)
        # Guarda cada hilo en un archivo distinto
        output.joinpath(f"thread_{i}.json").write_text(json.dumps(thread, indent=2, ensure_ascii=False), encoding='utf-8')
        
        # Si también quieres guardar los perfiles:
        #profile = await threads.scrape_profile(url)
        #output.joinpath(f"profile_{i}.json").write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding='utf-8')

if __name__ == "__main__":
    asyncio.run(run())

# Ejecuta el archivo 'json_csv.py'
subprocess.run(["python", "addons/main.py"])