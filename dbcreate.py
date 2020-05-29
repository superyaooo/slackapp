from tinydb import TinyDB, Query
from settings import member_id

team_a_db = TinyDB('team_a_vanguard.json')
team_a_db.insert({'name': 'user1', 'slackid': member_id, 'vanguarded': False})
team_a_db.insert({'name': 'user2', 'slackid': member_id, 'vanguarded': False})
team_a_db.insert({'name': 'user3', 'slackid': member_id, 'vanguarded': False})

team_b_db = TinyDB('team_b_vanguard.json')
team_b_db.insert({'name': 'user1', 'slackid': member_id, 'vanguarded': False})
team_b_db.insert({'name': 'user2', 'slackid': member_id, 'vanguarded': False})
team_b_db.insert({'name': 'user3', 'slackid': member_id, 'vanguarded': False})
