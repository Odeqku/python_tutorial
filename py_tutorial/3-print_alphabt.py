#!/usr/bin/python3

# insert ascii values (+1) of lowercase alphabet in range()

for i in range(97, 122):
    # Use an if statement to filter out e and q respectively
    if not(i == 101) and not(i == 113):
        # Print the letters of the alphabets and format it with c (character)
        print("{:c}".format(i), end=' ')
