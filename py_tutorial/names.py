#!/usr/bin/python3
names = []

for _ in range(3):
	names.append(input("What's your name? "))

with open("names.txt", "a") as file:
	for name in names:
		file.write(f"{name}\n")
