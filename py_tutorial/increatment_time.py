#!/usr/bin/python3

from class_time import Time
import copy

def increment(time, seconds):
    ''' Make a deep copy of time and store in time
    
    '''
    time = copy.deepcopy(time)
    ''' update the second of time object by adding seconds
    '''
    time.second += seconds

    ''' checking second in excess of 60
    '''
    d = time.second//60
    if d >= 1:
       time.second -= (60 * d)
       time.minute += (1 * d)

    d1 = time.minute//60
    if d1 >= 1:
        time.minute -= (60 * d1)
        time.hour += (1 * d1)

    return time


time = Time(12, 60, 60)

def main():
    new_time = increment(time, 60)
    print(new_time)
main()
