import random

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Track attempts
attempts = 0
guess = 0

# Game loop
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it in", attempts, "attempts.")
