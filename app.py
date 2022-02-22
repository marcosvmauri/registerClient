from chalice import Chalice
import boto3
import json

app = Chalice(app_name='registerClient')

@app.route('/', methods=['POST'], content_types=['application/json'])
def index():
    try:
        body = app.current_request.json_body
        callSNS(body)
    except Exception as e:
        return  {'error':  str(e)}
    return 'Cliente cadastrado com Sucesso!';

def callSNS(body):
    client = boto3.client("sns")
    TOPIC_ARN = "arn:aws:sns:us-east-1:146448507854:RegisterTopic"
    sns = boto3.client("sns")
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=json.dumps(body),
    )
    