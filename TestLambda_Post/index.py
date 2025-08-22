import requests
import json

def lambda_handler(event, context):
    # The API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    #Body of API Request
    payload = {
        "title" : "Foo2",
        "body"  : "bar2",
        "userId" : 6
    }

    # A post request to the API
    response = requests.post(url, payload)

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