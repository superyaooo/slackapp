from random import randint

class Greetings(object):
    greetings = ["Good morning, everyone.", "Oh hello, you.", "Well well well, it's a new day again.", "What a lovely day, isn't it!"]

    def get_greeting(self):
        max = len(self.greetings) - 1
        value = randint(0,max)
        greeting = self.greetings[value]
        return greeting