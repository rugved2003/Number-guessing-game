from random import randint
import random
EASY = 10
HARD = 5

def check_answer(guess, answer, turns):
  """Checks the answer against guess.retuen the number of returns remaing"""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("choose a difficulty.Type 'easy' or 'hard: '")
  if level == "easy":
    return EASY
  else:
    return HARD

def game():
  print("Welcome to the Number Guessig Game!")
  print("I'm thinking of number between 1 and 100")
  answer = random.randrange(1, 100)
  print(f"psst, teh correct answer is {answer} ")
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number. ")
    guess = int(input("Make a Guess:"))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of chances")
      return
    elif guess != answer:
      print("Guess again")
game()
