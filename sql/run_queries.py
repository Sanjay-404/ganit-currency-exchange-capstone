import sqlite3
import pandas as pd

conn = sqlite3.connect('data/currency.db')

queries = [
    "SELECT COUNT(*) as total_records FROM exchange_rates;",
    """
    SELECT quote, AVG(rate) as avg_rate, MIN(rate) as min_rate, 
           MAX(rate) as max_rate 
    FROM exchange_rates 
    GROUP BY quote 
    ORDER BY avg_rate DESC;
    """
]

for i, q in enumerate(queries, 1):
    print(f"\n--- Query {i} ---")
    result = pd.read_sql(q, conn)
    print(result)

conn.close()