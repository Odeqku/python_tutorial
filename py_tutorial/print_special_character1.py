#!/usr/bin/python3

def print_special_pattern_pt2(rows, my_input):
	space = 40 
	for i in range(1, rows + 1):
		print(" " * (rows - i) + my_input * i, end="")
		print(my_input * i, end="")

		print(" " * space + my_input * i, end="")	
		print(my_input * i)
		space = space - 2 
		#print(my_input * (i * 2))

def main():
	my_input = input("Enter the special character : ")

	new_rows = int(input("Enter the number of rows : "))
	print_special_pattern_pt2(new_rows, my_input)

if __name__ == "__main__":
	main()
