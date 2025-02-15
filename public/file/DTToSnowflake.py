import json
import boto3
import pandas as pd
from io import StringIO
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

dynamodb_table = dynamodb.Table("<< Your table name in DynamoDB >>")
bucket_name = "<< Your S3 bucket name >>"

def get_dynamo_data():
    response = dynamodb_table.scan()
    return response['Items']


def convert_to_dataframe(items):
    df = pd.DataFrame(items)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def save_to_s3(df, table_name):
    df['date'] = df['timestamp'].dt.date

    for date, group in df.groupby('date'):
        key = f"snowflake/{table_name}_{date}.csv"

        csv_buffer = StringIO()
        group.to_csv(csv_buffer, index=False)

        s3.put_object(Bucket=bucket_name, Key=key, Body=csv_buffer.getvalue())
        print(f"Data saved to S3 at {key}")

def lambda_handler(event, context):
    items = get_dynamo_data()

    if not items:
        print("No data found in DynamoDB")
        return

    df = convert_to_dataframe(items)

    save_to_s3(df, "stock_prices")

    print(f"Successfully processed and saved {len(items)} records.")
