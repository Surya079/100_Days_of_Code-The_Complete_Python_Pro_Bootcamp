print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
firstChoice = input("You have cross road. Where you want to go? \n \t type 'left' or 'right' ")

if firstChoice == "left" or "LEFT":
    secondChoice = input("You have cross river. What is your decision? \n \t type 'swim' or 'wait' ")
    if secondChoice == "wait" or "WAIT":
        thirdChoice = input("You have three doors. Which one you chose to open? \n \t type 'blue' or 'red' or 'yellow' ")
        if thirdChoice == "yellow" or "YELLOW":
            print("You Win!")
        elif thirdChoice == "blue" or "BLUE":
            print("Eaten by beasts. \nGame over!")
        elif thirdChoice == "red" or "RED":
            print("Burned by fire. \n Game over!")
        else:
            print("Game over!")
    else:
        print("Attacked by trout. \n Game over!")
elif firstChoice == "right" or "RIGHT":
    print("Fall into Hole. \n Game over!")