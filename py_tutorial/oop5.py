#!/usr/bin/python3


class Friend:
    def __init__(self, friends):
        self.friends = friends
    def is_friend_of(self, name):
        return name in self.friends

Obidients = Friend(['Nedu', 'Chu', 'Abdul'])
res = Obidients('is_friend_of', 'Chu')
print(res)
