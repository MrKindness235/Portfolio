#!/usr/bin/env python3


import random


choices = ['rock', 'paper', 'scissors']

player_points = 0
comp_points = 0

print("Welcome to the Rock, Paper and Scissors arcade game!\n\
My name is Elias, let's have fun!")
while True:
    comp_choice = random.choice(choices)
    player_choice = input("Enter rock, paper, or scissors. \
Type exit to finish the game: ").lower()

    if player_choice == "rock" and comp_choice == "paper":
        comp_points += 1
        print(f"I choose {comp_choice}")
        print("I win!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == "paper" and comp_choice == "scissors":
        comp_points += 1
        print(f"I choose {comp_choice}")
        print("I win!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == "scissors" and comp_choice == "rock":
        comp_points += 1
        print(f"I choose {comp_choice}")
        print("I win!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == "scissors" and comp_choice == "paper":
        player_points += 1
        print(f"I choose {comp_choice}")
        print("You win!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == "rock" and comp_choice == "scissors":
        player_points += 1
        print(f"I choose {comp_choice}")
        print("You win!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == "paper" and comp_choice == "rock":
        player_points += 1
        print(f"I choose {comp_choice}")
        print("You win!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == comp_choice:
        print(f"I choose {comp_choice}")
        print("Stalemate!")
        print(f"Score: You: {player_points} - Me: {comp_points}")

    elif player_choice == "exit":
        print("Thank you for playing")
        break

    else:
        print("Couldn't get that. Try again.")
