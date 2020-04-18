import os
from slack import WebClient
from slack.errors import SlackApiError
from datetime import datetime
from bottoken import bot_token
from settings import channel_id
from tinydb import TinyDB, Query
# from vanguard import Vanguard

db = TinyDB('members.json')

def get_member():
    members = Query()
    if db.count(members.vanguarded == False) == 0:
        db.update({'vanguarded':False})
    member = db.search(members.vanguarded == False)[0]
    return member

def post_message():
    vanguard = get_member()
    client = WebClient(token=bot_token)
    weekday = datetime.now().isoweekday()
    if 0 < weekday < 6:
        client.chat_postMessage(
            channel=channel_id,
            link_names='true',
            text=f"<!here|here> Good morning, everyone. Today's vanguard for team #001 is:  {vanguard['name']}. Please direct all team related questions to <@{vanguard['id']}>"
        )
        eid = vanguard.eid
        db.update({'vanguarded':True},eids=[eid])
    else:
        print("not a week day")


post_message()