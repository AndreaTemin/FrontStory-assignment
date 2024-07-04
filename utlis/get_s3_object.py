import boto3
import urllib.parse
import pandas as pd
from io import StringIO

def get_object(s3_url):
    # Parse the S3 URL
    parsed_url = urllib.parse.urlparse(s3_url)
    bucket_name = parsed_url.netloc
    object_key = parsed_url.path.lstrip('/')

    # Initialize the S3 client
    s3 = boto3.client('s3')

    try:
        # Get the object
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        # Read the content of the object
        content = response['Body'].read().decode('utf-8')

        # Convert the CSV content to a pandas DataFrame
        df = pd.read_csv(StringIO(content))
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None