#!/usr/bin/python3

def point_in_circle(circle, point):

    h = circle.centre.x
    k = circle.centre.y
    r = circle.radius
    p1 = point.x
    p2 = point.y

    d = math.sqrt((p1-h)**2 + (p2-k)**2)
    if (d <= r):
        return True
    else:
        return False
