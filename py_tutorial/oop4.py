#!/usr/bin/python3

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def distance_between_points(self, other): 
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

def main():
    p1 = Point(2, 3)
    p2 = Point(4, 5)
    d = distance_between_points(p1, p2)
    print(d)

main()
