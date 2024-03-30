#!/usr/bin/python3
""" Second part of the Arithmethic Calculator."""

# Last result starts as 0
last = 0
# Constant Loop
while (True):
    # Enter Calculation: 5 * 6
    # 5 * 6 = 30
    # Store the user input of 2 numbers and the operator
    num1, operator, num2 = input('Enter Calculation: ').split()

    # Convert the strings into integers
    if num1 == 'last':
        num1 = last
        num2 = int(num2)

    elif num2 == 'last':
        num1 = int(num1)
        num2 = last

    else:
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
        if num2 == 0:
            raise ValueError('Do not divide by 0')
        
        result = num1 / num2

    elif operator == '%':
        result = num1 % num2

    # print result
    print("{} {} {} = {}".format(num1, operator, num2, result))

    # Keep last result
    last = result
