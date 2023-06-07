#!/usr/bin/python3

class Person:
    def say_hi(self):
        print("Hello, how are you?")

p = Person()
p.say_hi()
print(isinstance(p, int))
print(p.__dict__)
print(dir(p))
