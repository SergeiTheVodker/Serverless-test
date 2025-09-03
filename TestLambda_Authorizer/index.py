import json

def lambda_handler(event, context):
    # Extract authorization token (e.g., from 'authorizationToken' header)
    token = event['authorizationToken']
    method_arn = event['methodArn']
    print(token)

    # Implement your authorization logic here (e.g., validate token against a database, JWT validation)
    # For a basic example, let's assume a hardcoded valid token
    if token == "Bearer pass":
        # Construct a policy document allowing access
        policy = {
            "principalId": "user123",  # A unique identifier for the authorized user
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "execute-api:Invoke",
                        "Effect": "Allow",
                        "Resource": method_arn
                    }
                ]
            }
        }
    else:
        # Construct a policy document denying access
        policy = {
            "principalId": "anonymous",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "execute-api:Invoke",
                        "Effect": "Deny",
                        "Resource": method_arn
                    }
                ]
            }
        }
    return policy