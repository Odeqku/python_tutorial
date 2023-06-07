#!/usr/bin/python3
'''
from int_to_time import int_to_time
'''
class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '{}:{:02d}:{:02d}'.format(self.hour,self.minute,self.second)

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if hour <= 24:
            self.__hour = hour
        else:
            print("Entre time in 24 hours only")

    def __add__(self, t1):
        second = self.second + t1.second
        minute = self.minute + t1.minute
        hour = self.hour + t1.hour

        d = second//60
        d1 = minute//60

        if d >= 1:
            minute += d
            second -= (60 * d)

        if d1 >= 1:
            hour += d
            minute -= (60 * d)
        
        return '{}:{:02d}:{:02d}'.format(hour,minute,second)

    def __sub__(self, start):
        min2 = self.hour * 60 + self.minute
        sec2 = min2 * 60 + self.second
        sum2 = sec2

        min1 = start.hour * 60 + start.minute
        sec1 = min1 * 60 + start.second
        sum1 = sec1

        sum3 = sum2 - sum1

        return sum3

    def int_to_time(self, inte=0):
        inte = inte
        self.minute, self.second = divmod(inte, 60)
        self.hour, self.minute = divmod(self.minute, 60)
        return '{}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)


end = Time(23, 50, 60)
start = Time(12, 23, 34)
time = Time()
d = end - start
durat = time.int_to_time(d)
print(durat)
