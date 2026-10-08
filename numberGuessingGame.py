
# Homework 3: Number Guessing Game

import random

hidden_number = random.randint(1, 20)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 20")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess == hidden_number:
        print("Congratulations! You won!")
        print(f"Attempts: {attempts}")
        break

    elif guess > hidden_number:
        print("Too high! Try again.")

    else:
        print("Too low! Try again.")

print("Game Over!")
