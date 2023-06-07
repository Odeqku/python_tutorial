#!/usr/bin/python3

from collections import namedtuple
from operator import attrgetter
from bisect import bisect, insort, bisect_left
from pprint import pprint

Movie = namedtuple("Movie", ("name", "released", "director"))

movies = [
	Movie("Jaws", 1975, "Spielberg"),
	Movie("Titanic", 1997, "Cameron"),
	Movie("The Birds", 1963, "Hitechcock"),
	Movie("Aliens", 1986, "Cameron")
]

# Find the first movie released after 1960
by_year = attrgetter("released")
movies.sort(key=by_year)
#print(movies[bisect(movies, 1960, key=by_year)])

# Insert a table while maintaining sort order
romance = Movie("Love Story", 1970, "Hiller")
insort(movies, romance, key=by_year)
#pprint(movies)

data = [("red", 5), ("blue", 1), ("yellow", 8), ("black", 0)]
data.sort(key=lambda r:r[1])
#print(data)
keys = [r[1] for r in data]
print(data[bisect_left(keys, 0)])
print(data[bisect_left(keys, 1)])
print(data[bisect_left(keys, 5)])
print(data[bisect_left(keys, 8)])
