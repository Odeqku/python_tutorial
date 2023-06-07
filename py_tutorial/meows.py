#!/usr/bin/python3

def meow(n: int) -> str:
    return "meows\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
