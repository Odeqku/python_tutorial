#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.attribute = name

    def say_hi(self):
        print('Hello, my name is', self.attribute)


p = Person('Swarroop')
p.say_hi()
