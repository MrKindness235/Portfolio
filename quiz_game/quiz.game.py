#!/usr/bin/env python3
"""A small quiz game"""

# Questions:

questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },

    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },

    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },

    {
        "prompt": "Who wrote 'To Kill a Mockingbird?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J. K. Rowling",
                    "D. Ernest Hemingway"],
        "answer": "A"
    },
]

# Start of question function:


def runquiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct, hooray!!")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"])

    print(f"You got {score} out of {len(questions)} quesstions correct.")


runquiz(questions)
