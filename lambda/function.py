import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'API Guardrails Lambda working'})
    }

import json

def lambda_handler(event, context):
    x = 1 / 0   # force error
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'This will fail'})
    }
