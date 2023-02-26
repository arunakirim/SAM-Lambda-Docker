import json


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "V3 and may be for V4, This is Arun, Welcome to the AWS learning centre program",
            }
        ),
    }
