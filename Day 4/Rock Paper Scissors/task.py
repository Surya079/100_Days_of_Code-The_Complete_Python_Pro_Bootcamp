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
import random
gameLogics = [rock, paper, scissors]

your_choice = int(input("Enter your choice? 0 , 1 or 2"))
if your_choice == 1 or your_choice ==  2 or your_choice ==  0:
    print("Your choice:", gameLogics[your_choice])
    com_choice = random.randint(0,2)
    print("Computer choice:", gameLogics[com_choice])


    if com_choice == 2 and your_choice == 1:
        print("You Lose!")
    elif your_choice == 2 and com_choice == 0:
        print("You Lose!")
    elif com_choice == 1 and your_choice == 0:
        print("You Lose!")
    elif com_choice == your_choice:
        print("Match draw!")
    else:
        print("You win!")
else:
    print("You entered wrong number...")