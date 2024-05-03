print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to treasure island.")
print("Your mission is to find the treasure.")

decision1 = input("You are at crossroad, where do you want to go? Type 'left' or 'right'? ").lower()

if(decision1 == "right"):
    print("You fell into a hole. Game Over!")
else:
    decision2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim a cross.").lower()
    if(decision2 == "swim"):    
        print("You got attacked by an angry trout. Game Over!")
    else:
        decision3 = input("You arrive at the island unhamed. There is a house with 3 doors. One Red, One Yellow, and one Blue. Which color do you choose? ").lower()
        if(decision3 == "red"):
            print("It's a room full of Fire. Game Over!")
        elif(decision3 == "blue"):
            print("You enter a room of beasts. Game Over!")
        elif(decision3 == "yellow"):
            print("You found the treasure! You Win!")
        else:
            print("You choose a door that doesn't exist. Game Over!")
    

