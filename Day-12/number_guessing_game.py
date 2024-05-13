import random

print("Welcome to the Number Guessing Game!\n")
 
guessed_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100")

difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
if difficulty_level == "easy":
    life_lines = 10
else:
    life_lines = 5

while life_lines > 0:
    print(f"You have {life_lines} attempts remaining to guess the number.") 
    guess = int(input("Make a guess: "))

    if guess == guessed_number:
        print(f"You got it! The answer was {guessed_number}.")
        life_lines = 0
    elif guess > guessed_number:
        print("Too high.")
        print("Guess again.")
    elif guess < guessed_number:
        print("Too low.")
        print("Guess again.")    

    life_lines -= 1     