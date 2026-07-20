# Ganit Capstone Project: Currency Exchange Rate Analysis

## Project Overview
This project demonstrates end-to-end data engineering and analysis using the Frankfurter API, Python, AWS, and Tableau.

## Major Objectives Achieved
- Fetched 1-year historical currency exchange data from Frankfurter API
- Stored data in CSV and SQLite
- Performed thorough EDA using Python, SQL, and visualizations
- Uploaded data to AWS S3
- Built interactive dashboard in Tableau Public
- Made the asset reusable through modular scripts

## Technologies Used
- **API**: Frankfurter API (European Central Bank)
- **Python**: pandas, matplotlib, seaborn, sqlite3, boto3
- **Database**: SQLite
- **Cloud**: AWS S3 (us-east-1)
- **Visualization**: Tableau Public
- **Version Control**: Git & GitHub

## Project Structure
- `scripts/` → Data fetching and AWS upload
- `data/` → CSV + SQLite database
- `notebooks/` → EDA scripts
- `sql/` → SQL queries and analysis
- `screenshots/` → All supporting images
- `dashboard/` → Tableau related

## How to Run
```bash
pip install -r requirements.txt

python scripts/fetch_data.py
python notebooks/eda.py
python sql/run_queries.py
python scripts/upload_to_s3.py