#!/usr/bin/env python3
""" Second part of the Arithmethic Calculator."""

# Last result starts as 0
last = 0

# Greeting
print("Hello, my name is Larry")
print("Please, enter a simple calculation, such as 2 + 2 (Spaces are needed).")
print("use the 'help' command for more info about my funtionality")
print("----------------------------------------------------------")
# Constant Loop
while (True):
    # Enter Calculation: 5 * 6
    # 5 * 6 = 30
    # Store the user input of 2 numbers and the operator
    # num1, operator, num2
    userinput = input('Enter Calculation: ')

    # Help command
    if userinput == 'help':
        print("----------------------------------------------------------")
        print("Larry Version 1.0")
        print("Addition: +")
        print("Substraction: -")
        print("Multiplication: *")
        print("Division: /")
        print("Modulo: %")
        print("'last' will use the lastest calculated value as its value.")
        print("'exit' will exit the program.")
        print("----------------------------------------------------------")

    # Exit program
    elif userinput == 'exit':
        exit()

    else:
        # Arithmetic input
        num1, operator, num2 = userinput.split()

        # 'Last' value implemetation
        if num1 == 'last':
            num1 = last
            num2 = int(num2)

        elif num2 == 'last':
            num1 = int(num1)
            num2 = last

        # Convert the strings into integers
        else:
            num1 = int(num1)
            num2 = int(num2)

        # if + then we need to provide output based on addition
        if operator == '+':
            result = num1 + num2

        # if - then we need to provide output based on substraction
        elif operator == '-':
            result = num1 - num2

        # if * then we need to provide output based on multiplication
        elif operator == '*':
            result = num1 * num2

        # if / then we need to provide output based on divition
        elif operator == '/':
            if num2 == 0:
                print('Do not divide by 0')

            else:
                result = num1 / num2

        # if % then we need to provide output based on modulo
        elif operator == '%':
            result = num1 % num2

        # print result
        if num2 == 0:
            pass

        else:
            print("{} {} {} = {}".format(num1, operator, num2, result))
            print("----------------------------------------------------------")
        # Keep last result

        if num2 == 0:
            pass

        else:
            last = result
