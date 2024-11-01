import requests
import time

def main():
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter the message to send: ")
    delay = float(input("Enter the delay between each message (in seconds): "))
    count = int(input("How many : "))

    for i in range(count):
        response = requests.post(webhook_url, json={"content": message})
        
        if response.status_code == 204:
            print(f"Message sent ({i+1}/10)")
        else:
            print(f"Error sending message ({response.status_code})")
        
        time.sleep(delay)

    print("Messages sent successfully.")

main()