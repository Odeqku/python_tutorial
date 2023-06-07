#!/usr/bin/python3
import re
class Student:
	def __init__(self, name, house, patronus):
		self.name = name
		self.house = house
		self.patronus = patronus


	def __str__(self) -> str:
		return f"{self.name} from {self.house}"
	
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		pattern = r" "
		if re.findall(pattern, name) or not name:
			raise ValueError("Missing Name")
		self._name = name.strip()


	@property
	def house(self):
		print("I am called just once")
		return self._house

	@house.setter
	def house(self, house):

		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid house")

		print("You must pass through me, Yeah!")
		self._house = house
"""	
	def charm(self):
		match self.patronus:
			case "stag":
				return "emoji"
			case "Otter":
				return "snail"
			case "Jack Russel teerier":
				return "Dog"
			case _:
				return "Pen"
		 
"""

def main():
	student = get_student()
	print(student)

def get_student():
	name = input("Name: ")
	house = input("House: ")
	patronus = input("Patronus: ")
	return Student(name, house, patronus)

if __name__ == "__main__":
	main()
