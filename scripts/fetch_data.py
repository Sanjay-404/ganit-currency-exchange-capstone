import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import sqlite3
import time

def fetch_historical_rates(start_date, end_date, base='EUR', quotes=None):
    """
    Fetch historical currency rates from Frankfurter API.
    """
    base_url = "https://api.frankfurter.dev/v2/rates"
    params = {
        'from': start_date,
        'to': end_date,
        'base': base
    }
    if quotes:
        params['quotes'] = ','.join(quotes)
    
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.text}")
    
    data = response.json()
    # Process data into flat structure
    records = []
    for date, rates in data.get('rates', {}).items():  # Adjust based on actual response
        for quote, rate in rates.items():
            records.append({
                'date': date,
                'base': data.get('base'),
                'quote': quote,
                'rate': rate
            })
    return pd.DataFrame(records)

# Example usage for 1 year
if __name__ == "__main__":
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    
    print(f"Fetching data from {start_date} to {end_date}")
    
    # Fetch data (in real env)
    # df = fetch_historical_rates(start_date, end_date)
    
    # For demo, create mock data
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    currencies = ['USD', 'GBP', 'JPY', 'INR']
    records = []
    for date in dates:
        for curr in currencies:
            rate = round(1 + (hash(str(date) + curr) % 100)/100, 4)  # mock
            records.append({'date': date.date(), 'base': 'EUR', 'quote': curr, 'rate': rate})
    
    df = pd.DataFrame(records)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/currency_rates.csv', index=False)
    print("Data saved to data/currency_rates.csv")
    
    # Save to SQLite
    conn = sqlite3.connect('data/currency.db')
    df.to_sql('exchange_rates', conn, if_exists='replace', index=False)
    conn.close()
    print("Data saved to SQLite")
