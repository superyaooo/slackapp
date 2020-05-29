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
        team_a_vanguard = Vanguard('team_a.json')
        team_b_vanguard = Vanguard('team_b.json')
        greeting = Greetings().get_greeting()
        client = WebClient(token=bot_token)
        client.chat_postMessage(
            channel=channel_id,
            link_names='true',
            text=f"<!here|here> {greeting} Today's vanguard for team a is:  {team_a_vanguard.name}. And the vanguard for team b is: {team_b_vanguard.name}. Please direct all team related questions to <@{team_a_vanguard.slack_id}> and <@{team_b_vanguard.slack_id}>"
        )
        team_a_vanguard.update_member()
        team_b_vanguard.update_member()
    else:
        print("not a week day")


post_message()
