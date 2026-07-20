import boto3
from botocore.exceptions import ClientError
import os

BUCKET_NAME = 'your-bucket-name-here'   # <<< CHANGE THIS
REGION = 'us-east-1'

s3 = boto3.client('s3', region_name=REGION)

def upload_file(file_path, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, BUCKET_NAME, f"data/{object_name}")
        print(f"✅ Uploaded: {file_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Uploading to S3...")
    upload_file('data/currency_rates.csv')
    upload_file('data/currency.db')
    print("Done!")