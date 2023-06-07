#!/usr/bin/python3

from bisect import bisect

def main():
	print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
	return grades[bisect(breakpoints, score)]

if __name__ == "__main__":
	main()
