#!/usr/bin/python3
inp = float(input("Please enter a temperature in degree celsius:\n"))
inp1 = (inp * (9/5)) + 32
print("{:.2f} {} celsius".format(inp, ('degrees' if inp > 1 or inp < -1 else 'degree')),end=' ')
print("is {:.2f} {} Fahrenheit".format(inp1, ('degrees' if inp1 > 1 or inp1 < -1 else 'degree')))




