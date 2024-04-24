#!/usr/bin/env python3
""" Second part of the Arithmethic Calculator."""

# Enter Calculation: 5 * 6
# 5 * 6 = 30
# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    result = num1 / num2

elif operator == '%':
    result = num1 % num2

# print result
print("{} {} {} = {}".format(num1, operator, num2, result))
