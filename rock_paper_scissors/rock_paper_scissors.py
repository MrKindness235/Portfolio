#!/usr/bin/env python3


import random


choices = ['rock', 'paper', 'scissors']

compchoice = random.choice(choices)
pchoice = input("Enter rock, paper, or scissors").lower

if pchoice == "rock" and compchoice == "paper":
    print("I win!")

elif pchoice == "paper" and compchoice == "scissors":
    print("I win!")

elif pchoice == "scissors" and compchoice == "rock":
    print("I win!")
