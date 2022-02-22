import json
import boto3
import uuid
from decimal import Decimal

def lambda_handler(event, context):
    
    body = json.loads(event["Records"][0]["body"])
    message = json.loads(body["Message"], parse_float=Decimal)
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("clients")
    
    table.put_item(
        Item={
            "id": str(uuid.uuid4()),
            "content": message      
        })
    
    return {
        'statusCode': 200,
    }
