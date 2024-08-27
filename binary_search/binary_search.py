#!/usr/bin/env python3

# a function that takes a list and target parameter
def binary_search(list, element):
    # multiple variables : middle, start, end, steps
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # start of while loop
    while start <= end:
        print("Step", steps, ":", list[start:end+1])
        # increase steps each time a split is done
        steps += 1
        middle = (start + end) // 2

        # conditions to track target position
        if element == list[middle]:
            return middle

        elif element < list[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 12

binary_search(my_list, target)
