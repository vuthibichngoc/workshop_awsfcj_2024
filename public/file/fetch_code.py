import json
import requests
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("stock_prices")


def get_stock_data(symbol):
    api_url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": "1day",
        "apikey": "YOUR_TWELVE_DATA_API_KEY",  
        "outputsize": "30",  
        "format": "JSON"
    }
    
    response = requests.get(api_url, params=params)
    data = response.json()
    
    return data


def lambda_handler(event, context):
    symbols = ["MSFT"]  
    processed_symbols = []

    for symbol in symbols:
        data = get_stock_data(symbol)
        time_series = data.get("values", [])  

        for entry in time_series:
            item = {
                "symbol": symbol,
                "timestamp": entry["datetime"],  
                "open": Decimal(entry["open"]),
                "high": Decimal(entry["high"]),
                "low": Decimal(entry["low"]),
                "close": Decimal(entry["close"]),
                "volume": int(entry["volume"])  
            }


            table.put_item(Item=item)

        processed_symbols.append(symbol)

    return {
        "statusCode": 200,
        "body": json.dumps({"processed_symbols": processed_symbols})
    }
