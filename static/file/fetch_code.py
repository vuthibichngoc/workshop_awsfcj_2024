import json
import requests
import boto3
from decimal import Decimal
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("<< your table name in dynamodb >>")

def get_stock_data(symbol):
    api_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,  
        "apikey": "demo"  
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data

def lambda_handler(event, context):
    symbols = ["MSFT"]  
    processed_symbols = []

    for symbol in symbols:
        data = get_stock_data(symbol)
        time_series = data.get("Time Series (Daily)", {})  # Đã sửa lỗi

        for time_stamp, metrics in time_series.items():
            item = {
                'symbol': symbol,
                'timestamp': time_stamp,
                'open': metrics['1. open'],
                'high': metrics['2. high'],
                'low': metrics['3. low'],
                'close': metrics['4. close'],
                'volume': metrics['6. volume']  
            }

           
            item = json.loads(json.dumps(item), parse_float=Decimal)

            table.put_item(Item=item)

        processed_symbols.append(symbol)

    return {
        "statusCode": 200,
        "body": json.dumps({"processed_symbols": processed_symbols})
    }
