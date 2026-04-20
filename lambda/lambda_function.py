import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    user_message = body.get('message', '')
    
    client = boto3.client('bedrock-agent-runtime', region_name='us-east-2')
    
    response = client.invoke_agent(
        agentId='ZFCHZU4BFP',
        agentAliasId='U99QTSMJLX',
        sessionId='session-001',
        inputText=user_message
    )
    
    completion = ''
    for event in response['completion']:
        if 'chunk' in event:
            completion += event['chunk']['bytes'].decode('utf-8')
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': json.dumps({'response': completion})
    }
