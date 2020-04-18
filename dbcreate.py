from tinydb import TinyDB, Query
from settings import member_id

db = TinyDB('members.json')
db.insert({'name': 'user1', 'id': member_id, 'vanguarded': False})
db.insert({'name': 'user2', 'id': member_id, 'vanguarded': False})
db.insert({'name': 'user3', 'id': member_id, 'vanguarded': False})
