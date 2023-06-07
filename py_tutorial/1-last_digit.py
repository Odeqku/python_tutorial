#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# convert the number from int to str and store it inside str_num
str_num = str(number)

# obtain the length of the string and store it in num_digits
num_digit = len(str_num)

# Obtain the last character of the str_num and store it is last_char
last_char = str_num[num_digit - 1]

# convert the last_char to int and store it in i
i = int(last_char)

# the constructor and its block of codes to filter int_l
if i > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, i))
elif i == 0:
    print("Last digit of {} is {} and is 0".format(number, i))
elif (i < 6) and not(i == 0):
    print(f"Last digit of {number} is {i} and is less than 6 and not 0")
