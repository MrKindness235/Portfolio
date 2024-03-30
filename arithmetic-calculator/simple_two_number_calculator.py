#!/usr/bin/python3
"""This is an Arithmatic Calculator intended for my portfolio"""

# Input two values
num1, num2 = input('Enter 2 numbers: ').split

# Convert string values into integers
num1 = int(num1)
num2 = int(num2)

# Add values entered and store in sum
sum = num1 + num2

# Substract values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Use modulus on the values to find the reminder
reminder = num1 % num2

# Print the result
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, reminder))
