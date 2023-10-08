#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst = abs(number) % 10
if number < 0:
    lst = -lst
print(f"Last digit of {number} is {lst} and is", end=" ")
if lst > 5:
    print(f"greater than 5")
elif lst == 0:
    print(f"0")
else:
    print(f"less than 6 and not 0")
