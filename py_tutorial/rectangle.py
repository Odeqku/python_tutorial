#!/usr/bin/python3

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, x, y, corner):
        self.x = x
        self.y = y
        self.corner = corner
        self.corner.x = corner.x
        self.corner.y = corner.y

corner = Point(0.0, 0.0)

rec = Rectangle(1, 2, corner)
print(rec.corner.x)
