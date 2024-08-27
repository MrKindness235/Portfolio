#!/usr/bin/env python3

import random

# This list must be expanded for a greater array of answers
names = [
    'James', 'Michael', 'Robert', 'Jhon', 'David', 'William', 'Richard',
    'Joseph', 'Thomas', 'Christopher']

# This list must be expanded for a greater array of answers
surnames = [
    'Smith', 'Jones', 'Williams', 'Taylor', 'Brown', 'Davies',
    'Evans', 'Thomas', 'Wilson', 'Johnson']

# Random choice being generated
name = random.choice(names)
surname = random.choice(surnames)

# Output
print(f"{name} {surname}")
