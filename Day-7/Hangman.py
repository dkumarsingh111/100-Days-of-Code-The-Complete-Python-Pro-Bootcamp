import random

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

""")


stages = ['''
   +-----+
   |     |
   o     |
  /|\    |
  / \    |
         |
============
          
''','''
   +-----+
   |     |
   o     |
  /|\    |
  /      |
         |
============
          
''','''
   +-----+
   |     |
   o     |
  /|\    |
         |
         |
============
          
''','''
   +-----+
   |     |
   o     |
  /|     |
         |
         |
============
          
''','''
   +-----+
   |     |
   o     |
   |     |
         |
         |
============
          
''','''
   +-----+
   |     |
   o     |
         |
         |
         |
============
          
''','''
   +-----+
   |     |
         |
         |
         |
         |
============
          
''']

end_of_game = False
lives = len(stages)

word_list = ['ardvark', 'baboon', 'camel', 'abortion', 'about', 'above', 'abroad', 'absence', 'absolute', 'absolutely', 'absorb', 'abuse', 'academic', 'accept', 'access', 'accident', 
             'accompany', 'accomplish', 'according', 'account', 'accurate', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquire', 'across']

chosen_word = random.choice(word_list)
word = []

for _ in chosen_word:
    word += "_"

print(f"\n Guess word: {word} \n \n")

while not end_of_game and lives > 0:
    guess = input("Guess a Letter: ").lower()
    if guess in word:
        print(f"You've already guessed {guess}.")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if(letter == guess):
                word[position] = letter
                

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life. Available live(s) is/are {lives}.")
            print(stages[lives])
            if lives == 0:
                print("You Loss!\n")

        if guess in chosen_word:
            print(f"{' '.join(word)}\n") 

        if "_" not in word:
            end_of_game = True
            print("\nYou Win!\n")   
               