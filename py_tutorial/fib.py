#!/usr/bin/python3

def fib(n):
	"""print a fibonacci series up to n."""
	a, b = 0, 1

	result = []
	
	while a < n:

		result.append(a)
		a, b = b, a+b

	return result

n = int(input("Enter a number: "))
fr = fib(n)
print(fr)
