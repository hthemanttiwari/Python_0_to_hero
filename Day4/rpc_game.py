# Rock, Paper, and Scesiors game with computer.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print ("Welcome to my Rock, Paper and Scessor Game. \n")

list = [rock, paper, scissors]

# User Selections
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n")
user_choice = int(user_input)

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 

else:
  print (list[user_choice] + "\n")
  # Computer Selection
  print ("Computer choose: \n")
  computer_choice = random.randint(0, 2)
  print (list[computer_choice] + "\n")
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw") 


# End!