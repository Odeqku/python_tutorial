#!/usr/bin/python3

for number in range(20):
    try:
        assert number % 3 == 0
        print("Multiple of 3:", number)

    except AssertionError:
        print("Non multiple:",number)
