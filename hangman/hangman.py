#!/usr/bin/python3
"""Hangman game"""


import random


words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# Randomly choose a word from the list
chosen_word = random.choice(words)
# Create a list of underscores
word_display = ['_' for _ in chosen_word]
# Number of allowed attempts
attempts = 8

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            # Reveal letter
            if letter == guess:
                word_display[index] = guess

    else:
        print("That letter doesn't appear in the word, try again!")
        attempts -= 1

# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived")
