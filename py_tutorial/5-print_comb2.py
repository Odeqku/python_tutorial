#!/usr/bin/python3

# iterate over a range of 100
for i in range(100):
    # Filter out 99 from the values of i using if
    if i < 99:
        # print the result of the iteration with a minimum of two digit
        print("{:02d}".format(i), end=', ')

    else:
        print("{:02d}".format(i))
