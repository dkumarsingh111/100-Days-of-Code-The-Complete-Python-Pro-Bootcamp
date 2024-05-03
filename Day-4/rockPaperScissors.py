import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = input("What do you choose? Rock / Paper / Scissor: ").lower()

if(user_choice == "rock"):
    print(rock)
elif(user_choice == "paper"):
    print(paper)
elif(user_choice == "scissor"):
    print(scissor)
else:
    print("Wrong choice!")


computer_choice = random.randint(0,2)

if(computer_choice == 0):
    print(f"Computer Choice: Rock \n {rock}")
    computer_choice = "rock"
elif(computer_choice == 1):
    print(f"Computer Choice: Paper \n {paper}")
    computer_choice = "paper"
elif(computer_choice == 2):
    print(f"Computer Choice: Scissors \n {scissor}")
    computer_choice = "scissor"
  

if(user_choice == computer_choice):
    print("Game Draw")
else:
    if((user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper")):
        print("You won!")
    elif((user_choice == "rock" and computer_choice == "paper") or (user_choice == "scissor" and computer_choice == "rock") or (user_choice == "paper" and computer_choice == "scissor")):
        print("Computer Wins!")
    else:
        print("You Lose the Game!")
       
