# Number Guessing Game

import random

number = random.randint(1, 10)

while True:
    guees = int(input("Enter the number: "))

    if guees == number:
        print("The number is correct")
        break

    elif guees > number:
        print("The number is high, guess again")

    else:
        print("The number is low, guess again")