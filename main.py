from art import logo, vs
from game_data import data
import random
from replit import clear


def randomChoices(data, previous_winner=None):
  """Choose two random dictionaries from the list, with the option to include a previous winner"""
  choice1 = previous_winner if previous_winner else random.choice(data)
  choice2 = random.choice(data)

  while choice2 == choice1:
    choice2 = random.choice(data)

  return choice1, choice2


def compareFollowers(choice1, choice2):
  """Compare the follower counts of two dictionaries and return the winner"""
  if choice1["follower_count"] > choice2["follower_count"]:
    return "A", choice1
  else:
    return "B", choice2


def game(data):
  """Play the higher or lower game"""
  print(logo)
  score = 0
  previous_winner = None
  
  while True:
    choice1, choice2 = randomChoices(data, previous_winner)
    print("Compare A:",choice1["name"],"- a", choice1["description"], "from", choice1["country"])
    print(vs)
    print("Against B:", choice2["name"],"- a", choice2["description"], "from", choice2["country"])
  
    guess = input("Who do you think has more followers? Type 'A' or 'B': ").upper()
    answer, winner = compareFollowers(choice1, choice2)
    
    if guess == answer:
      score = score+1
      previous_winner = winner
      clear()
      print(f"You're right. Current Score: {score}")
      
    else:
      print(f"Sorry, that's wrong. Final Score: {score}")
      print("Game Over!")
      break

game(data)
