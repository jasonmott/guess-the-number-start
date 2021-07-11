import random
from art import logo
print(logo)
is_game_over = False

#print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = random.randint(1,100)

def compare(user_choice):
  print(n)
  if n > user_choice:
    return "Too low."
  elif n < user_choice:
    return "Too high."
  else:
    return "same"

if level_of_difficulty == "easy":
  number_of_tries = 10
else:
  number_of_tries = 5
while is_game_over == False and number_of_tries != 0:
  print(f"You have {number_of_tries} attempts remaining to guess the number.")
  number_of_tries -= 1
  user_guess = int(input("Make a guess: "))
  guess_result = compare(user_guess)
  if guess_result != "same" and number_of_tries !=0:
    print(guess_result)
    print("Guess Again.")
  elif guess_result == "same":
    print(f"You got it! The number was {n}!")
    is_game_over = True
  elif number_of_tries == 0:
    print(guess_result)
    print("You've run out of guesses, you lose.")






  




