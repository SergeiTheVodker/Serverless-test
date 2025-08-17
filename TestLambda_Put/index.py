import requests

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

print(response.json())