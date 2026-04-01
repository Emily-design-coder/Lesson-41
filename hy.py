import random

number = random.randint(1, 100)

guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("Correct! You guessed it!")