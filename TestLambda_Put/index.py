import requests
import json

def lambda_handler(event, context):
    #REST URI
    url = "https://jsonplaceholder.typicode.com/posts/1"

    #Body of API request
    payload = {
        "id" : 1,
        "title" : "foo",
        "body"  : "b3r3",
        "userId" : 1
    }

    response = requests.put(url, payload)

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