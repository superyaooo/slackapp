import os
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime
from bottoken import bot_token
from settings import channel_id
from vanguard import Vanguard
from greetings import Greetings

def post_message():
    weekday = datetime.now().isoweekday()
    if 0 < weekday < 6:
        vanguard = Vanguard()
        greeting = Greetings().get_greeting()
        client = WebClient(token=bot_token)
        client.chat_postMessage(
            channel=channel_id,
            link_names='true',
            text=f"<!here|here> {greeting} Today's vanguard for team #001 is:  {vanguard.name}. Please direct all team related questions to <@{vanguard.slack_id}>"
        )
        vanguard.update_member()
    else:
        print("not a week day")


post_message()