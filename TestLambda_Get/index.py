import requests
import json

def lambda_handler(event, context):
    # The API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # A GET request to the API
    response = requests.get(url)

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