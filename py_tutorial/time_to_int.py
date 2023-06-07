#!/usr/bin/python3

from class_time import Time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    new_time = Time()
    new_time.second = t1.second + t2.second
    new_time.minute = t1.minute + t2.minute
    new_time.hour = t1.hour + t2.hour
 
    d = new_time.second//60
    d1 = new_time.minute//60

    if d >= 1:
        new_time.minute += d
        new_time.second -= (60 * d)

    if d1 >= 1:
        new_time.hour += d
        new_time.minute -= (60 * d)

    return new_time

def main():
    
    time = Time(14, 17, 56)
    seconds = time_to_int(time)
    time = int_to_time(seconds)
    sum_time = add_time(time, time)
    print(seconds)
    print(time)
    print(sum_time)
    print(time_to_int(sum_time))

main()
