import random

is_game_over = False

#print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
n = random.randint(1,100)

def compare(user_choice):
  print(n)
  if n > user_choice:
    return "Too low.\nGuess Again."
  elif n < user_choice:
    return "Too high.\nGuess Again."
  else:
    return "same"

#while is_game_over == False:
if level_of_difficulty == "easy":
#  print("You have 10 attempts remaining to guess the number.")
  number_of_tries = 10
else:
#  print("You have 5 attempts remaining to guess the number.")
  number_of_tries = 5
while number_of_tries != 0 or is_game_over == False:
  print(f"You have {number_of_tries} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  guess_result = compare(user_guess)
  if guess_result == "same":
    print(f"You got it! The number was {n}!")
    is_game_over = True
  else:
    print(guess_result)
  number_of_tries -= 1






  




