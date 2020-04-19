from tinydb import TinyDB, Query

class Vanguard(object):
    def __init__(self):
        self.db = TinyDB('members.json')
        member = self.get_member()
        self.name = member['name']
        self.slack_id = member['slackid']
        self.element_id = member.eid

    def get_member(self):
        members = Query()
        if self.db.count(members.vanguarded == False) == 0:
            self.db.update({'vanguarded':False})
        member = self.db.search(members.vanguarded == False)[0]
        return member

    def update_member(self):
        self.db.update({'vanguarded': True}, eids=[self.element_id])
