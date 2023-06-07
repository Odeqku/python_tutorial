#!/usr/bin/python3
import csv

students = []

with open("names.csv") as file:
	for line in file:
		name, address = line.rstrip().split(",")
		student = {"name": name, "address": address}
		students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
	print(f'{student["name"]} is in {student["address"]}')


"""
		name, address = line.split(",")
		names.append(f"{name} is at {address}")
for name in sorted(names):
	print(name)
"""
