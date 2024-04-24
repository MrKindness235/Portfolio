#!/usr/bin/env python3
""" A random number guessing game"""

import random

print("Welcome to the Number Guessing Game!")
number_range = input("Enter a number range such as 0 to 50: ").split()

number = random.randrange(int(number_range[0]), int(number_range[2]))
print("Let's start the game.")
while True:
    guess = int(input("Enter number guess: "))
    if guess == number:
        print(f"Congratulations! The number was {number}")
        break

    elif guess > number:
        print("Think smaller.")

    elif guess < number:
        print("Think bigger.")
