
print("Welcome to the UAlbany Basement. Your mission is to find the treasure.")

answer1 = input('You are lost in the basemant of the University. '
                'You come to the end of a hall and hear frightining scream. '
                'Where do you want to go? Type "left" or "right" \n').lower()

if answer1 == "left":
    answer2 = input('Your are running for your life and come to another dead end '
                    'with only a giant fountain in front of you. '
                    'Type "wait" to wait for security. '
                    'Type "swim" to swim across. \n').lower()

    if answer2 == 'wait':
        answer3 = input("You arrive to the Campus Center unharmed. "
                        "There are 3 doors. One red, one yellow and one blue. "
                        "Which colour do you choose? \n").lower()

        if answer3 == 'red':
            print("The room is full of fire. Game Over")
        elif answer3 == 'yellow':
            print("You found the treasure! You WIN!!!")
        elif answer3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print('You chose a door that doesnt exist. GAME OVER!')

    else: print("You get attacked by an angry trout. Game Over")

else:
    print("You fell into a hole. Game Over.")