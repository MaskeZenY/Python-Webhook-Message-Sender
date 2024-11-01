# Python Webhook Message Sender

This Python script sends a message to a specified webhook URL at regular intervals. It uses the `requests` library to make HTTP POST requests.

## Features

- Sends a custom message to a specified webhook URL.
- Allows setting the delay between each message.
- Specifies the total number of messages to be sent.

## Requirements

Make sure you have the `requests` library installed before running the script:

```bash
pip install requests
```

## Usage

1. Clone this repository or download the file.

2. Run the script:

```bash
python webhook_sender.py
```

3. Provide the following information when prompted:
   - **Webhook URL**: The URL to which the message will be sent.
   - **Message**: The content of the message to send.
   - **Delay between each message (in seconds)**: The time interval (in seconds) between each message.
   - **Number of messages**: The total number of messages to send.

The script will send the specified message at regular intervals, displaying a confirmation for each sent message or an error message if it fails.

## Example Run

```
Enter the webhook URL: https://discordapp.com/api/webhooks/12345678910/DGe1Sik_NN4H24-S75-1F3g4re1VGE483feG1
Enter the message to send: Hello, World!
Enter the delay between each message (in seconds): 2
How many: 5

Message sent (1/5)
Message sent (2/5)
...
Messages sent successfully.
```

## Disclaimer

Sending repeated messages to webhooks should comply with the API's usage policies. Use this script responsibly to avoid potential blocks or restrictions.
