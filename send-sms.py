import logging
import json
import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    logger = logging.getLogger();
    logger.setLevel(logging.INFO)
    sns_client = boto3.client("sns")
    
    message = json.loads(event["Records"][0]["Sns"]["Message"])
    
    response = sns_client.publish(
        PhoneNumber=message["phone"], 
        Message="Olá seu cadastro foi realizado com Sucesso!",
    )
    
    return {'statusCode': 200}
