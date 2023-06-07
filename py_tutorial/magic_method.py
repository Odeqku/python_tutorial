#!/usr/bin/python3

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other):
        new_time = Time()

        # Add seconds of both objects and correct if offshoot
        if (self.second + other.second) >= 60:
            new_time.minute += 1
            new_time.second = (self.second + other.second) - 60
        else:
            new_time.second = self.second + other.second

        # Add minutes of both objects and correct if offshoot
        if (self.minute + other.minute) >= 60:
            new_time.hour += 1
            new_time.minute += (self.minute + other.minute) - 60
        else:
            new_time.minute += self.minute + other.minute

        # Add hours of both objects and correct if offshoot
        if (self.hour + other.hour) > 24:
            new_time.hour += 1
        else:
            new_time.hour += self.hour + other.hour


        return new_time


time1 = Time(9,50,30)
time2 = Time(13, 10, 20)


print(time1 + time2)
