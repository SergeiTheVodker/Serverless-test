import requests

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

    # Print the response
    print(response.json())