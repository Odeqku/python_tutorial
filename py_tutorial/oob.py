#!/usr/bin/python3


class Coordinate(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def distance(self, other):
        x_diff_sq = (self.__x - other.__x)**2
        y_diff_sq = (self.__y - other.__x)**2
        return (x_diff_sq - y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.__x)+","+str(self.__y)+">"

c1 = Coordinate(3, 4)
c2 = Coordinate(0, 0)
dis = c1.distance(c2)
print(c1)
print(type(c1))
#if type(dis) == int:
try:
    print("{:d}".format(dis))

except ValueError:
    print("{:.4f}".format(dis))
