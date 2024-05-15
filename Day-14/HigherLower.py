from art import logo, vs
from game_data import data
from random import randint
import os

def choose_record():
    position = randint(0, len(data))
    followers = data[position]["follower_count"]
    return position, followers


def game():
    score = 0
    lost = False  
    
    playerA_position, playerA_followers = choose_record()
    playerB_position, playerB_followers = choose_record()

    while not lost:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")

        print(f"Compare A: {data[playerA_position]["name"]}, a {data[playerA_position]["description"]}, from {data[playerA_position]["country"]}")

        print(vs)

        print(f"Against B: {data[playerB_position]["name"]}, a {data[playerB_position]["description"]}, from {data[playerB_position]["country"]}")

        option = input("Who has more followers? Type 'A' or 'B': ").capitalize()

        if option == "A" and playerA_followers > playerB_followers:
            score += 1
            playerA_position = playerB_position
            playerA_followers = playerB_followers
            playerB_position, playerB_followers = choose_record()
        elif option == "B" and playerA_followers < playerB_followers:
            score += 1 
            playerA_position = playerB_position
            playerA_followers = playerB_followers
            playerB_position, playerB_followers = choose_record()
        elif playerA_followers == playerB_followers:
            score += 1 
            playerA_position = playerB_position
            playerA_followers = playerB_followers
            playerB_position, playerB_followers = choose_record()
        else:
            lost = True    

        os.system("cls || clear")

    if lost:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}") 

game()    