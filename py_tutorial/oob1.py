#!/usr/bin/python3


class Coordinate(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self._difference = None

    @property
    def difference(self):
        return self._difference

    @difference.setter
    def difference(self, other):
        x_diff_sq = (self.__x - other.__x)**2
        y_diff_sq = (self.__y - other.__x)**2
        self._difference = (x_diff_sq - y_diff_sq)**0.5

c1 = Coordinate(3, 4)
c2 = Coordinate(5, 6)
c1.difference = c2
dis = c1.difference

try:
    print("{:d}".format(dis))

except ValueError:
    print("{:.4f}".format(dis))
