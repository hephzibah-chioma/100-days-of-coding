print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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


first = input("You have come to a junction. It's time to decide. Type in 'left' or 'right': ").lower()

if first != "left":
  print("You fell into a hole. Game over.")
else:
  second = input("You've come to the edge of the island. You have to make another choice. Type in 'swim' or 'wait': ").lower()
  if second != "wait":
    print("You've been attacked by a trout. Game over.")
  else:
    third = input("You're faced with 3 doors. Choose one of them. Type in 'red', 'blue', or 'yellow': ").lower()
    if third == "red":
      print("Burned by fire. Game over.")
    elif third == "blue":
      print("Eaten by beasts. Game over.")
    elif third == "yellow":
      print("You Win!")
    else:
      print("Invalid input. Game over.")
