import json


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "V2 , This is Arun, Welcome to the AWS learning centre program",
            }
        ),
    }
