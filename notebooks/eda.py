import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Load data
df = pd.read_csv('data/currency_rates.csv')
df['date'] = pd.to_datetime(df['date'])

print("Data Shape:", df.shape)
print(df.head())
print(df.describe())

# Group by quote
pivot = df.pivot_table(index='date', columns='quote', values='rate')
print(pivot.head())

# Plot trends
plt.figure(figsize=(12,6))
for col in pivot.columns:
    plt.plot(pivot.index, pivot[col], label=col)
plt.title('Currency Exchange Rates vs EUR')
plt.legend()
plt.savefig('dashboard/rates_trend.png')
plt.show()

# Insights
print("Average rates:")
print(df.groupby('quote')['rate'].mean())

# SQL example
conn = sqlite3.connect('data/currency.db')
query = """
SELECT quote, AVG(rate) as avg_rate, MIN(rate) as min_rate, MAX(rate) as max_rate
FROM exchange_rates
GROUP BY quote
"""
print(pd.read_sql(query, conn))
conn.close()
