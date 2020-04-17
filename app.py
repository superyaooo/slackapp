import os
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime
from bottoken import bottoken

client = WebClient(token=bottoken)

def postMessage():
    today = datetime.now().date()
    weekday = datetime.now().isoweekday()
    currentTime = datetime.now().time()

    if(0 < weekday < 6):
        print("sending msg to slack")
        response = client.chat_postMessage(
            channel='#vanguard-flagger',
            text=f"test test 1 2 3, today's date: {today}, it's {weekday}, current time: {currentTime}"
        )
        print("msg sent")
        print(response)
    else:
        print("not a week day")

if __name__ == "__main__":
    postMessage()
