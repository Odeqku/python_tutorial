#!/usr/bin/python3
from class_time import Time

def int_to_time(inte):
    time = Time()
    minutes, time.second = divmod(inte, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
