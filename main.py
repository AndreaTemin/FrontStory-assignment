import pandas as pd
# Example usage
s3_url = 's3://your-bucket-name/your-file.csv'
df = download_public_s3_object(s3_url)
if df is not None:
    print(df.head())