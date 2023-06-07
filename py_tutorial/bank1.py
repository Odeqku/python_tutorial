#!/usr/bin/python3

class Account:
	def __init__(self):
		self._balance = 0

	def __str__(self):
		return f"{self._balance}"

	@property
	def balance(self):
		return self._balance

	def deposit(self, n):
		self._balance += n

	def withdraw(self, n):
		self._balance -= n

def main():
	account = Account()
	print("Balance: ", account)
	account.deposit(100)
	account.withdraw(50)
	print("Balance:", account)

if __name__ == "__main__":
	main()
