#!/usr/bin/python3

def incr(n=0):
    v = n
    m = 1
    if n <= 1:
        return 1
    m = incr(n - 1)
    m = m * 2
    print(m)
    return m

n = incr(30)
print(n)
