import requests
import json

# Replace with your Teams webhook URL
WEBHOOK_URL = "https://ssinfis.webhook.office.com/webhookb2/a8572049-47a6-47fe-b78b-289bfb1adff4@1543f07f-30f9-407a-9eb5-8a7aec418fff/IncomingWebhook/3ae869ebb0ab4c18aa1e670e20b95715/d9e51cd3-930f-4499-abd3-9d567315f17f/V2HLylhZBnOUWCX4lesciuLRkZBpxUq94EYDrhRC9Oqbc1"

# Define the message payload
message_payload = {
    "text": "Hello, Teams! This message was sent via a webhook."
}

# Send the request
response = requests.post(WEBHOOK_URL, headers={"Content-Type": "application/json"}, data=json.dumps(message_payload))

# Check response status
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
