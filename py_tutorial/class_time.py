#!/usr/bin/python3

class Time:
    '''Represents the time of day.

    attributes: hour, minute, second
    '''
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

'''
time = Time(11, 59, 30)
print(time)
'''
