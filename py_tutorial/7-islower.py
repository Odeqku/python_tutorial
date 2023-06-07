#!/usr/bin/python3
# the function prototype, followed by its definition
def islower(c):
    # store the unicode of the character in unc using ord()
    unc = ord(c)

    # iterate over a range of 97 to 123: unicodes for lowercase letters
    for i in range(97, 123):
    # compare unc to the range using if statement
        if unc == i:
            return True
    else:
        return False
