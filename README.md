# Ganit Capstone Project: Currency Exchange Rates

## Overview
This project fetches 1+ year of historical currency exchange data from Frankfurter API, stores it, performs EDA, and builds a Tableau dashboard. AWS is used for storage and processing.

## Project Structure
- `scripts/`: Python scripts for data fetching and processing
- `data/`: Stored CSV/SQLite data
- `notebooks/`: Jupyter notebooks for EDA
- `sql/`: SQL queries for analysis
- `aws/`: Terraform or CloudFormation for AWS setup
- `dashboard/`: Tableau workbook description and screenshots

## Usage
1. Set up AWS resources
2. Run fetch script
3. Perform EDA
4. Build dashboard in Tableau

## AWS Integration
- Data stored in S3
- Optional Lambda for scheduled fetches
- Athena for querying

