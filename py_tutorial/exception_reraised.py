#!/usr/bin/python3

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
