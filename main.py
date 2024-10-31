#!/usr/bin/python3.6
import urllib3
import json

# Initialize an HTTP client for making requests
http = urllib3.PoolManager()

def lambda_handler(event, context):
    # Define the Slack webhook URL where messages will be sent
    url = "slack_webhook_url"
    
    # Create the message payload with desired Slack parameters
    msg = {
        "channel": "#aws_sns_notifications",  # Slack channel where messages are posted
        "username": "AWS Notifications and Alarms",  # Display name of the bot
        "text": event["Records"][0]["Sns"]["Message"],  # Extract the SNS message content
        "icon_emoji": ":aws:",  # Optional icon for the bot
    }

    # Convert message dictionary to JSON format
    encoded_msg = json.dumps(msg).encode("utf-8")

    # Send the JSON payload to the specified Slack webhook URL
    resp = http.request("POST", url, body=encoded_msg)
    
    # Log message status and response for troubleshooting or record-keeping
    print(
        {
            "message": event["Records"][0]["Sns"]["Message"],
            "status_code": resp.status,
            "response": resp.data,
        }
    )
