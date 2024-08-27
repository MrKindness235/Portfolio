#!/usr/bin/env python3


import random


choices = ['piedra', 'papel', 'tijera']

player_points = 0
comp_points = 0

print("Bienvenido al juego Arcade de Piedra, Papel y Tijera!\n\
Mi nombre es Elías, vamos a divertirnos!")

while True:
    comp_choice = random.choice(choices)
    player_choice = input("Escribe piedra, papel o tijera. \
Escribe salir para terminar el juego: ").lower()

    if player_choice == "piedra" and comp_choice == "papel":
        comp_points += 1
        print(f"Yo elijo {comp_choice}")
        print("Yo gano!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == "papel" and comp_choice == "tijera":
        comp_points += 1
        print(f"Yo elijo {comp_choice}")
        print("Yo gano!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == "tijera" and comp_choice == "piedra":
        comp_points += 1
        print(f"Yo elijo {comp_choice}")
        print("Yo gano!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == "tijera" and comp_choice == "papel":
        player_points += 1
        print(f"Yo elijo {comp_choice}")
        print("Tu ganas!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == "piedra" and comp_choice == "tijera":
        player_points += 1
        print(f"Yo elijo {comp_choice}")
        print("Tu ganas!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == "papel" and comp_choice == "piedra":
        player_points += 1
        print(f"Yo elijo {comp_choice}")
        print("Tu ganas!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == comp_choice:
        print(f"Yo elijo {comp_choice}")
        print("Empate!")
        print(f"Puntaje: Tú: {player_points} - Yo: {comp_points}")

    elif player_choice == "salir":
        print("Gracias por jugar.")
        break

    else:
        print("No entiendo eso, intenta devuelta.")
