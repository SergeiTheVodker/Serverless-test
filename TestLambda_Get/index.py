import requests

def lambda_handler(event, context):
    # The API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # A GET request to the API
    response = requests.get(url)

    return {
	    'statusCode': str(response.status_code) + " " + response.reason,
        'object': response.json()
    }