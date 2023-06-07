#!/usr/bin/python3

balance = 0
d = 0
w = 0

def main():
	print("Current Balance: ", balance)
	deposit(100)
	print("Number of Deposit made: ", d)
	withdraw(50)
	print("Number of Withdraw made: ", w)
	print("New Balance: ", balance)

def deposit(dep):
	global balance, d
	d += 1
	balance += dep

def withdraw(withdr):
	global balance, w
	w += 1
	balance -= withdr

if __name__ == "__main__":
	main()
