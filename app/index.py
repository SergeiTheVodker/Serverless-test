import json

import boto3
import requests

_actual_endpoints = {'get' : '/get/api-test', 'post' : '/post/api-test'}

def get_api_config():

    #Declare the S3 client
    s3_client = boto3.client('s3')

    #Declare necessary variables for s3 object
    bucket = 'my-test-bucket-for-mini-serverless-project'
    file = 'apiconfig.json'

    #Declare the s3 object
    s3_object = s3_client.get_object(Bucket=bucket, Key=file)

    #Read the contents of the s3 file apiconfig.json
    body = s3_object["Body"].read().decode("utf-8")

    return(json.loads(body))

def is_api_endpoint_valid(method, path) -> bool:
    
    api_config = get_api_config()

    for endpoint in api_config:
        if endpoint.get('allowed') == True:
            if method == endpoint.get('method') and path == endpoint.get('path'):
                return True
    
    return False

def generate_response(response):
    result = {
        "reason": response.reason,
        "object": response.json()
    }

    return {
        "statusCode": response.status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(result)  # convert dict → string
    }

def common_handler(event, context):

    # The API endpoints
    get_url = "https://jsonplaceholder.typicode.com/posts/1"
    post_url = "https://jsonplaceholder.typicode.com/posts"

    #Body of API Requests
    post_payload = {
        "title" : "Foo2",
        "body"  : "bar2",
        "userId" : 6
    }

    put_payload = {
        "id" : 1,
        "title" : "foo",
        "body"  : "b3r3",
        "userId" : 1
    }
    
    # check if allowed
    if is_api_endpoint_valid(event.get('httpMethod'), event.get('path')):
        print(f"success")
        print(f"method: {event.get('httpMethod')}")
        match event.get('httpMethod'):
            case 'GET':
                return generate_response(requests.get(get_url))
            case 'PUT':
                return generate_response(requests.put(get_url, put_payload))
            case 'POST':
                return generate_response(requests.post(post_url, post_payload))
            case _:
                raise Exception('Unknown method')
    print(event.get('httpMethod'))
    print(event.get('path'))
    print(is_api_endpoint_valid(event.get('httpMethod'), event.get('path')))

    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": 'Error'  # convert dict → string
    }