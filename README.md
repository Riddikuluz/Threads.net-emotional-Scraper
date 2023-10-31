# Threads.net Scraper

## Description
This repository contains a Python script that demonstrates how to use the Threads.net scraper to collect product data and product search information. The script utilizes the Threads.net API through the Scrapfly service. The results are saved in the `./results/` directory.

## Prerequisites
Before running the script, make sure you have the Scrapfly API key. Set the environment variable `$SCRAPFLY_KEY` with your Scrapfly API key:

### Linux/Mac
```bash
export SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
```

### Windows
```powershell
$env:SCRAPFLY_KEY="your key from https://scrapfly.io/dashboard"
```

Next, here are the dependencies you need to install using Poetry:

1. **Poetry (Dependency Manager)**
   ```bash
   pip install poetry
   ```

2. **Project Dependencies (Run in the project directory)**
   ```bash
   poetry install
   ```

3. **Project Dependencies (Run in the project directory with a virtual environment created by Poetry)**
   ```bash
   poetry add aiohttp
   poetry add bs4
   poetry add pandas
   poetry add pysentimiento
   ```

Make sure to run these commands in the Poetry-created virtual environment for your project. If the code uses any custom library, make sure to add it using `poetry add`.

Also, ensure that you have Python installed in your environment; in my case, I am using python-3.11.6.

## Usage
1. Clone the repository to your local machine.
2. Set the Scrapfly API key as described in the prerequisites.
3. Run the script:
   ```bash
   poetry run python run.py
   ```

## Script Details
### `run.py`
This script initiates the Threads.net scraper and saves the results in the `./results/` directory. It includes a list of example URLs for scraping. You can add more URLs as needed.

### `addons/main.py`
This script processes JSON files, performs data extraction, transformation, sentiment analysis, and stores the final data in Excel format.

### `addons/data_extraction.py`
This module provides functions to extract data from JSON files.

### `addons/data_transformation.py`
This module transforms data, adding additional columns with default values.

### `addons/sentiment_analysis.py`
This module analyzes the sentiment of the text using the PySentimiento library.

### `addons/data_storage.py`
This module handles the storage of the final data in Excel format in the `./xlsx/` directory.


## Script Details
### `run.py`
This script initiates the Threads.net scraper and saves the results in the `./results/` directory. It includes a list of example URLs for scraping. You can add more URLs as needed.

### `addons/main.py`
This script processes JSON files, performs data extraction, transformation, sentiment analysis, and stores the final data in Excel format.

### `addons/data_extraction.py`
This module provides functions to extract data from JSON files.

### `addons/data_transformation.py`
This module transforms data, adding additional columns with default values.

### `addons/sentiment_analysis.py`
This module analyzes the sentiment of the text using the PySentimiento library.

### `addons/data_storage.py`
This module handles the storage of the final data in Excel format in the `./xlsx/` directory.

## Instructions
1. Run `poetry run python run.py` to collect data from Threads.net. Make sure you have added the URLs previously in the `urls` variable within the `run.py` file.
2. Find the final results in the `xlsx/Final.xlsx` file.
   
### `GPT/gpy.py`
This Python script leverages the OpenAI GPT-3.5 Turbo model for sentiment analysis. It takes a CSV file containing text data, processes each entry through the OpenAI API, and appends the predicted sentiment to the dataset. This step is optional since the emotion analysis is already done by the PySentimiento library.

#### Prerequisites
Before running the script, ensure you have the necessary environment variables set in a `.env` file:

```plaintext
OPENAI_API_KEY=your_openai_api_key
```

Also, make sure you have the required Python packages installed:

```bash
pip install pandas requests python-dotenv openai
```

#### Usage
1. Add your OpenAI API key to the `.env` file.
2. Prepare a CSV file (`Final.csv`) with a column named 'Texto' containing the text data.
3. Run the script:

```bash
python gpy.py
```

#### Notes
- The script assumes the input CSV file has a 'Texto' column for sentiment analysis.
- Predicted sentiments are appended to the 'Concepto asociado' column.

