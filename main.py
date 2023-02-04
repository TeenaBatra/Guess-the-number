import random
from replit import clear

print('''
   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                        
''')
game_end=False

def check_number(num):
  if num>choosed_number:
    print("Too High")
  elif num<choosed_number:
    print("Too Low")
  elif num==choosed_number:
    return True
    
while not game_end:
  print("Welcome to the number guessing game.")
  print("I am thinking of a number between 1 and 100")
  choosed_number=random.randint(1,101)
  #print(choosed_number)
  level=input("Choose the level of the game: Easy or Difficult\n").lower()
  if level=="easy":
    number_of_attempts=10
    print("You've 10 attempts to guess the number.")
    while number_of_attempts>0:
      guessed_number=int(input("Guess the number: "))
      output=check_number(guessed_number)
      if output==True:
        print(f"You guessed it! The answer was {guessed_number}")
        break
      number_of_attempts-=1
      print(f"You still have {number_of_attempts} attempts remaining.")
    if number_of_attempts==0:
      print("You've run out of guesses, You lose!")
  elif level=="difficult":
    number_of_attempts=5
    print("You've 5 attempts to guess the number.")
    while number_of_attempts>0:
      guessed_number=int(input("Guess the number: "))
      output=check_number(guessed_number)
      if output==True:
        print(f"You guessed it! The answer was {guessed_number}")
        break
      number_of_attempts-=1
      print(f"You still have {number_of_attempts} attempts remaining.")
    if number_of_attempts==0:
      print("You've run out of guesses, You lose!")
  else:
    print("There is no such level!")
  
  run_again=input("Do you want to play again? Yes or No\n").lower()
  if run_again=="no":
    game_end=True
    print("Thank you!")
