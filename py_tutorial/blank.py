#!/usr/bin/python3

import math

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return f'Point({self.x}, {self.y})'

blank = Point(3.0, 4.0)
print(blank)


def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def main():
    p = Point(3.0, 4.0)
    p1 = Point(4.0, 5.0)

    d = distance_between_points(p, p1)

    print('{:.4f}'.format(d))
main()
