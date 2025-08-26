import boto3
import json

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

