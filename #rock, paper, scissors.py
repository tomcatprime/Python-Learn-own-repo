#rock, paper, scissors
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
#list of choices
data = [rock,paper,scissors]
#player choice
x= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_choice = data[x]

#Computer chose
pc_random = random.randint(0, 2)
computer = data[pc_random]

print(player_choice)
print(computer)

if player_choice == rock and computer == paper:
    print("You lose")
elif player_choice == rock and computer == scissors:
    print("You won")
elif player_choice == paper and computer == rock:
    print("You won")
elif player_choice == paper and computer == scissors:
    print("You lose")
elif player_choice == scissors and computer == paper:
    print("You won")
elif player_choice == scissors and computer == rock:
    print("You lose")
else:
    print("Play again")



