#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_n = number % 10
if last_n < 0:
    last_n = number % -10
else:
    last_n = number % 10
print("Last digit of {} is {} and is".format(number, last_n), end=" ")
if last_n > 5:
    print("greater than 5")
elif last_n == 0:
    print("0")
else:
    print("less than 6 and not 0")
