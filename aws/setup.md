# AWS Setup

1. Create S3 bucket: `ganit-currency-data`
2. Upload CSV to S3 using boto3.
3. Use AWS Glue or Athena for querying.
4. Optional: Lambda function triggered by EventBridge for daily updates.

Example boto3 upload:
```python
import boto3
s3 = boto3.client('s3')
s3.upload_file('data/currency_rates.csv', 'ganit-currency-data', 'historical_rates.csv')
```
