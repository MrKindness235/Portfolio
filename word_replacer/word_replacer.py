#!/usr/bin/env python3

def replace_word():
    string = "hi, it is me, the coder and avatar"
    word_to_replace = input("Enter which word to replace: ")
    word_replacement = input("Enter which word replacement: ")
    print(string.replace(word_to_replace, word_replacement))


replace_word()
