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

# random_integer = random.randint(0, 1)
# print(random_integer)

# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")

player1_choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player1_choice == 0:
    print(rock)
elif player1_choice == 1:
    print(paper)
else:
    print(scissors)
    
random_int = random.randint(0, 2)

computer_choice = random_int

print("Computer chose: ")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("Try again")
    
if player1_choice == 0 and computer_choice == 2:
    print("You win")
elif player1_choice == 1 and computer_choice == 0:
    print("You win")
elif player1_choice == 2 and computer_choice == 1:
    print("You win")
elif player1_choice == computer_choice:
    print("Draw") 
    
if computer_choice == 0 and player1_choice == 2:
    print("You lose")
elif computer_choice == 1 and player1_choice == 0:
    print("You lose")
elif computer_choice == 2 and player1_choice == 1:
    print("You lose")
elif computer_choice == player1_choice:
    print("Draw")    
                  
            