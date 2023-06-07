#!/usr/bin/python3

a = 0
for line in open("oob1.py"):
    for char in line:
        a += 1
    print(line, end='')
    print('Printed {} character'.format(a))
    a = 0
print()
