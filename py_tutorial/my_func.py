#!/usr/bin/python3

def my_func(a=[]):
	a.append(1)
	return a

def main():
	print(my_func(), my_func())


if __name__ == "__main__":
	main()
