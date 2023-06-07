#!/usr/bin/python3

import math

def rect_in_circle(Circle, Rectangle):
    h = Circle.corner.x
    k = Circle.corner.y
    r = Circle.radius
    awidth = Rectangle.width
    aheight = Rectangle.height
    centrex = Rectangle.centre.x
    centrey = Rectangle.centre.y

    d = math.sqrt((centrex - h)**2 + (centrey - k)**2)
    if d <= r:
        return True
    else: False
