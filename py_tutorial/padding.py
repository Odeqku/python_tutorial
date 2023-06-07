#!/usr/bin/python3
import re
pattern = "NULL"
while True:
#	print("{:12} {:d}".format(input("Enter Name: "), input("Enter an integer: ")))
#	print("{:*^15}".format("Taken"))
	#f = open('Data', 'a')
	read = "{:12} {}{}".format(input("Enter Name: "), input("Enter an Age: "), '\n')
	match = re.search(pattern, read)
	if match:
		break
	read1 = "{:*^15} {}".format("Taken", '\n')
	with open('Data', 'a') as f:
		f.write(read)
		f.write(read1)
#	print(read)
#	print(read1)
#f.close()
