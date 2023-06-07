#!/usr/bin/python3

# Iterate over a range of 50 using for loop
for i in range(50):
    # filter out multiple of 10 and 11 in the range
    if (i % 10 != 0) and (i % 11 != 0):
        # filter out 21, 31, and 32
        if (i != 21) and (i != 31) and (i != 32):
            # filter out 41, 42 and 43
            if (i != 41) and (i != 42) and i != 43:
                # print out the filtered and formatted result
                print("{:02d}".format(i), end=', ')

# Iterate over a range from 56 to 79 using for loop
for n in range(56, 80):
    # filter out multiple of 10 and 11 in the range
    if (n % 10 != 0) and (n % 11 != 0):
        if (n != 61) and (n != 62) and (n != 63) and (n != 64) and (n != 65):
            if (n != 71) and (n != 72) and (n != 73) and (n != 74):
                if (n != 76) and (n != 75):
                    print("{:02d}".format(n), end=', ')

print("{:02d}".format(89))
