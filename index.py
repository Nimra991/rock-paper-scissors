import random


def get_choices():
  player_choice = input("Enter a choice(rock, paper, scissors):")
  #input function is used to get input from user
  options = ["rock","paper","scissors"]
  # use list to use multipule choices in single variable
  computer_choice = random.choice(options)
  #use ramdon libaray to choose random optiom by computer
  choices = {"player": player_choice, "computer": computer_choice}
  # Use dict here {pair of key and value, so player is a key and player choice is a value}
  return choices

def check_win(player, computer):
  # creat function arguments(data)
  print(f"you chose {player}, computer choice {computer}")
  # use f-strings use to connect variable with strings
  if player == computer:
    return "its a tie!"
    # use if statment to check if player and computer choice the same.
  elif player == "rock":
   if computer == "scissors":
     return "rock samashes scissors, you win!"
   else:
     return "paper covers rock, you lose."
    # use elif and nestec if here.

  elif player == "paper":
   if computer == "rock":
     return "paper covers rock, you win!"
   else:
     return "scissors cuts paper, you lose."

  elif player =="scissors":
   if computer == "paper":
     return "scissors cuts paper, you win!"
   else:
     return "rock samashes scissors, you lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)     