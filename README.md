# SNS to Slack Lambda Alerts

A Lambda function to forward AWS SNS notifications to Slack channels. This repository includes the setup guide to integrate AWS SNS notifications with Slack using a Lambda function.

## Features
- AWS SNS notifications are forwarded to a Slack channel via a webhook.
- Supports setting custom Slack usernames and icons.
- Simple deployment and configuration steps.

## Prerequisites
- An AWS account with permissions to create SNS topics and Lambda functions.
- A Slack workspace with permission to add incoming webhooks.

## Setup

### 1. Create an SNS Topic
1. Go to the [Amazon SNS Console](https://console.aws.amazon.com/sns/v3/home).
2. Click **Create topic**.
3. Choose a topic type, such as **Standard**, and name your topic (e.g., `my-sns-alerts`).
4. Click **Create topic**.

### 2. Create an SNS Subscription (Optional)
This step allows you to send the SNS notifications to Lambda:
1. Go to your SNS topic.
2. Under **Subscriptions**, click **Create subscription**.
3. For **Protocol**, select **Lambda**.
4. For **Endpoint**, select the Lambda function to receive the SNS notifications.
5. Click **Create subscription**.

### 3. Set up a Slack Webhook
1. Go to your [Slack Apps Management Page](https://api.slack.com/apps).
2. Click **Create New App**.
3. Select **From Scratch**, then name your app and choose the workspace.
4. Go to **Incoming Webhooks** and activate **Incoming Webhooks**.
5. Click **Add New Webhook to Workspace** and follow the prompts to select a channel.
6. Copy the Webhook URL provided.

### 4. Create the Lambda Function
1. Go to the [AWS Lambda Console](https://console.aws.amazon.com/lambda).
2. Click **Create function**.
3. Choose **Author from scratch** and set a function name (e.g., `sns-to-slack-alerts`).
4. Select **Python 3.8** or higher as the runtime.
5. Under **Execution role**, choose or create a role with **AWSLambdaBasicExecutionRole** and **AmazonSNSFullAccess** permissions.

### 5. Add the Code
1. Copy the provided Python code (above) into the Lambda function editor.
2. Replace the `url` in the code with your Slack webhook URL from Step 3.
3. Save the changes.

### 6. Set up SNS Permissions
1. In your Lambda function configuration, go to **Permissions**.
2. Attach a policy to the role to allow `sns:Publish` permissions if you intend to invoke other SNS topics.

### 7. Configure Lambda as an SNS Topic Subscriber
1. In the SNS Console, go to your topic’s **Subscriptions** tab.
2. Click **Create Subscription** and set the protocol to **Lambda**.
3. Choose the Lambda function as the endpoint.
4. Confirm the subscription by allowing the SNS topic to invoke the Lambda function.

### Testing
1. Publish a test message to your SNS topic to verify the integration.
2. You should see the notification in the designated Slack channel within seconds.

## Notes
- Ensure that your Lambda execution role has the necessary permissions for SNS and logging.
- Customize the Slack message as needed for your alerting needs.
  
