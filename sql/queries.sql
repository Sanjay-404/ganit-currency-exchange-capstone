-- SQL Queries for EDA

-- 1. Total records
SELECT COUNT(*) as total_records FROM exchange_rates;

-- 2. Average rate per currency
SELECT 
    quote,
    AVG(rate) as avg_rate,
    MIN(rate) as min_rate,
    MAX(rate) as max_rate,
    COUNT(*) as days
FROM exchange_rates
GROUP BY quote
ORDER BY avg_rate DESC;

-- 3. Rate on specific date
SELECT * FROM exchange_rates 
WHERE date = '2026-01-01';

-- 4. Highest rate day for each currency
SELECT quote, date, rate
FROM exchange_rates
WHERE (quote, rate) IN (
    SELECT quote, MAX(rate)
    FROM exchange_rates
    GROUP BY quote
);