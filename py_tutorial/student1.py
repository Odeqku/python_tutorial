#!/usr/bin/python3

class Student:

	def __init__(self, name, house):
		self.name = name
		self.house = house


	def __str__(self) -> str:
		return f"{self.name} from {self.house}"

	@classmethod
	def get(cls):
		name = input("Name: ")
		house = input("House: ")
		return cls(name, house)
