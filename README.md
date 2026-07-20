# Ganit Capstone Project: Currency Exchange Rate Analysis

## Project Overview
This project fetches 1-year historical currency exchange rates from the **Frankfurter API**, performs Exploratory Data Analysis (EDA), stores data using AWS S3, and visualizes insights using Tableau Public.

## Objectives Achieved
- Fetched 1+ year of historical currency data
- Stored data in structured format (CSV + SQLite)
- Performed EDA using Python (Pandas, Matplotlib, Seaborn)
- Uploaded data to AWS S3 (us-east-1)
- Created interactive dashboard in Tableau Public
- Derived actionable insights

## Technologies Used
- **API**: Frankfurter API (ECB rates)
- **Language**: Python
- **Libraries**: pandas, matplotlib, seaborn, boto3
- **Cloud**: AWS S3
- **Visualization**: Tableau Public
- **Storage**: CSV + SQLite

## How to Run the Project

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Fetch data
python scripts/fetch_data.py

# 3. Run EDA
python notebooks/eda.py

# 4. Upload to AWS S3
python scripts/upload_to_s3.py