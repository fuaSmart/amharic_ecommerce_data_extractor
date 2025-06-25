# Amharic E-commerce Data Extractor

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview

This project aims to build a robust **Amharic E-commerce Data Extractor**. The core objective is to transform unstructured and multimodal data (text and images) from various Ethiopian Telegram e-commerce channels into structured, machine-readable information. This extracted data will then be leveraged to populate EthioMart's centralized database, ultimately aiding in identifying promising vendors for micro-lending by providing insights into their activity and product offerings.

Key focus areas include:
* **Data Ingestion:** Programmatically collecting data from Telegram channels.
* **Named Entity Recognition (NER):** Fine-tuning LLMs to extract Product Names, Prices, and Locations from Amharic text.
* **Vendor Analytics:** Developing a scorecard to assess vendor potential for micro-lending based on extracted data and Telegram metadata.

## 📁 Project Structure

This repository follows a standard data science project structure for clarity and maintainability:

* `data/`: Stores raw (`raw/`) and processed (`processed/`) datasets.
* `notebooks/`: Contains Jupyter notebooks for exploratory data analysis (EDA), prototyping, and interactive development.
* `scripts/`: Houses standalone Python scripts for automated tasks (e.g., Telegram data scraping).
* `src/`: Contains core Python modules for reusable functions and project logic.
* `models/`: Stores trained machine learning models.
* `reports/`: For generated reports and figures (`figures/`).
* `tests/`: Unit and integration tests for code quality.
* `config/`: Configuration files for project parameters.
* `utils/`: General utility functions.
* `.github/workflows/`: GitHub Actions for CI/CD pipeline.
* `.vscode/`: VS Code specific settings.

## ⚙️ Setup and Installation

To set up and run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/fuaSmart/amharic_ecommerce_data_extractor.git](https://github.com/fuaSmart/amharic_ecommerce_data_extractor.git)
    cd amharic_ecommerce_data_extractor
    ```


2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows (Command Prompt):
    .\venv\Scripts\activate
    
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Telegram API Credentials:**
    Create a `.env` file in the project's root directory and add your Telegram API credentials (obtained from [my.telegram.org](https://my.telegram.org/)):
    ```
    TG_API_ID=your_api_id_here
    TG_API_HASH=your_api_hash_here
    phone=+251XXXXXXXXX # Your Telegram phone number with country code
    ```


## ▶ Getting Started / Usage

### Task 1: Data Ingestion & Preprocessing 

This phase involved collecting raw Telegram data and preparing it for analysis and model training.

1.  **Run the Telegram Scraper:**
    ```bash
    python scripts/telegram_scraper.py
    ```
    * *First run will prompt for Telegram authentication code.*
    * This script populates `data/raw/telegram_data.csv` with message content and `data/raw/telegram_photos/` with associated images.

2.  **Perform Data Preprocessing:**
    * Launch Jupyter Notebook from the project root: `jupyter notebook`
    * Open and run the notebook: `notebooks/01_Data_Preprocessing.ipynb`
    * This notebook cleans the raw text data and saves it to `data/processed/cleaned_telegram_data.csv`. It also parses the initial provided labeled data (`labeled_telegram_product_price_location.txt`) into a usable format for model training.

### Task 2: Label a Subset of Dataset in CoNLL Format (In Progress)

This crucial task involves manually annotating additional messages to expand the NER training dataset.

* **Process:** Messages are selected from `data/processed/cleaned_telegram_data.csv` and manually labeled in the CoNLL format. Each token is assigned a `B-`, `I-`, or `O` tag for `Product`, `Price`, and `Location` entities.
* **Output:** The manually labeled data is saved in `data/processed/manual_labeled_data.txt`.

## Next Steps

* **Task 3: Fine Tune NER Model:** Combine existing and newly labeled data to fine-tune a transformer-based model for Amharic NER.
* **Task 4: Model Comparison & Selection:** Evaluate and compare different NER models based on performance metrics (F1-score, speed) to select the best one.
* **Task 5: Model Interpretability:** Utilize SHAP/LIME to understand model predictions and identify areas for improvement.
* **Task 6: FinTech Vendor Scorecard:** Develop an analytics engine to calculate key vendor performance metrics and create a "Lending Score" based on extracted entities and Telegram metadata.
