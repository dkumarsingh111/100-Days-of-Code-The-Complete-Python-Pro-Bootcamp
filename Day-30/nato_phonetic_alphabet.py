# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

yes = True

try:
    data = pandas.read_csv("c:/Users/10278018/OneDrive - BD/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/Day-26/nato_phonetic_alphabet.csv")

except FileNotFoundError as err_msg:
    print(f"{err_msg}")

else:
    #TODO 1. Create a dictionary in this format:
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    while yes:
        word = input("Enter a word: ").upper()
        try:
            output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            yes = False
            print(output_list)
