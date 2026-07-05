# Guess the Number Project
# This project helps beginners practice loops, conditions, and the random module.

import random

secret_number = random.randint(1, 10)
attempts = 0

print("Guess the Number Game")
print("I am thinking of a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        print("Number of attempts:", attempts)
        break
