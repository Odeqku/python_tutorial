#!/usr/bin/python3

students = [
	{"name": "Hermione", "house": "Gryffindor"},
	{"name": "Harry", "house": "Gryffindor"},
	{"name": "Ron", "house": "Slytherin"},
	{"name": "Padma", "house": "Ravenclaw"}
]
#print(sorted(list(set([dic["house"] for dic in students]))))

houses = set()
for student in students:
	houses.add(student["house"])

for house in sorted(houses):
	print(house)

