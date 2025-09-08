import requests

def lambda_handler(event, context):
    
    # SOAP request URL
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

    # structured XML
    payload = """<?xml version="1.0" encoding="utf-8"?>
                <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                    <soap12:Body>
                        <ListOfCountryNamesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        </ListOfCountryNamesByName>
                    </soap12:Body>
                </soap12:Envelope>"""

    # headers
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }

    # POST request
    response = requests.request("POST", url, headers=headers, data=payload)

    # prints the response
    return {
            "statusCode": str(response.status_code),
            "headers": {
                "Content-Type": "application/json"
            },
            "body": response.text
        }