#!/usr/bin/python3
from rectangle import Point

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.centre.x = centre.x
        self.centre.y = centre.y
        self.radius = radius

centre = Point(150, 100)
acircle = Circle(centre, 75)

