import random

rock ='''
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

game = [rock, paper, scissors]
user = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer = random.choice(game)
print("Your : ", game[user])
print("Computer :", computer)

if user == 0:
    if computer == rock:
        print("Draw")
    elif computer == paper:
        print("You lose")
    elif computer == scissors:
        print("You win")

    
elif user == 1:
    if computer == rock:
        print("You Win")
    elif computer == paper:
        print("Draw")
    elif computer == scissors:
        print("You lose")        
    

elif user == 2:
    if computer == rock:
        print("You lose")
    elif computer == paper:
        print("You win")
    elif computer == scissors:
        print("Draw")   

else:
    print("Wrong input")         

    


    

