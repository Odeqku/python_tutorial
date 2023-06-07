#!/usr/bin/python3

class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        ''' Returns a float value of the fraction '''
        return self.num / self.denom
    def inverse(self):
        ''' Returns a new fraction representing '''
        return Fraction(self.denom, self.num)

a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b # c is a Fraction object
print(a)
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
