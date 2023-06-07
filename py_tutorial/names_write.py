#!/usr/python3

import csv

name = input("What's your name? ")
home = input("What is your home? ")

with open("names.csv", "a") as file:
	writer = csv.writer(file)
	writer.writerow([name, home])
