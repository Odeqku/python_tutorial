#!/usr/bin/python3

from class_time import Time
from int_to_time import int_to_time
def mul_time(time, n):
    new_time = Time()
    minute = time.hour * 60 + time.minute
    second = minute * 60 + time.second
    mul = second * n

    new_time = int_to_time(mul)

    return new_time


time = Time(23, 45, 00)
print(mul_time(time, 10))
