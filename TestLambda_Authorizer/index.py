import json
import boto3

def get_api_config() -> any:

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

def is_api_endpoint_valid() -> bool:
    api_config = get_api_config()

    for endpoint in api_config:
        return endpoint["allowed"] == False

def lambda_handler(event, context):
    api_config_list = get_api_config()
    whole_auth_token = "event.get['authorizationToken']"
    if not whole_auth_token:
        whole_auth_token = "Some Token This should fail."

    print(f"Auth Token is: {whole_auth_token}")
    print(f"Method ARN: Authorizer")

    principal_id = ""
    resource = ""
    effect = ""
    
    for endpoint in api_config_list:
        if endpoint["allowed"] == True:
            if event.get("httpApiMethod") == endpoint["method"] and event.get("httpApiPath") == endpoint["path"]:
                raise Exception("Unauthorized")
    return {
        "principalId" : principal_id,
        "policyDocument" :{
            'Version' : '2012-10-17',
            'Statement' : [
                {
                    "Action" : "execute-api:Invoke",
                    "Effect" : effect,
                    "Resource" : resource
                }
            ]
        }
    }