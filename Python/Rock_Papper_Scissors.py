import random

def get_choices():
  player_choice = input("Input a choice(rock,paper,scissors):")
  option = ["rock", "paper","scissors"]
  computer_choice = random.choice(option)
  choices = {"player": player_choice,"computer": computer_choice}
  return choices

def check_win(player,computer):
  print(f"You chose: {player}\nComputer chose:{computer}")
  if player == computer:
    return print("Its a Tie")
  elif player == "rock":
    if computer == "scissors":
      print("rock beats scissors: you win!")
    else: print("paper covers rock: you lose.")  
  elif player == "paper":
    if computer == "scissors":
      print("scissors cut paper: you lose.")
    else: print("paper covers rock: you win!")  
  elif player == "scissors":
    if computer == "rock":
      print("rock beats scissors: you lose.")
    else: print("scissors cut paper: you win!")  


choices = get_choices()
result = check_win(choices["player"],choices["computer"])