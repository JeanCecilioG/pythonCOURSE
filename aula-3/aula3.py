print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"-._      `"=.                     |
 _________|_____________________`"=._o`"-._          `"=._o`"-._ _________|_______
|                   |    |    |      `"=._o`"-._          `"=._o`"-._  |
|___________________|____|____|__________|`"=._o`"-._          `"=._o`"-._|_______
          |                |    |    |          `"=._o`"-._          `"=._o`"-._
 _________|________________|____|____|________________`"=._o`"-._          `"=._o`"-._
|                   |    |    |      |                | `"=._o`"-._          `"=._o`"-._
|___________________|____|____|______|________________|_______`"=._o`"-._          `"=.
          |                |    |    |          |                | `"=._o`"-._
 _________|________________|____|____|__________|________________|______`"=._o`"-._
|                   |    |    |      |                |    |    |        `"=._o`"-._
|___________________|____|____|______|________________|____|____|__________`"=._o`"-._
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Write your code below:
# Tip: Use if/elif/else statements

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
