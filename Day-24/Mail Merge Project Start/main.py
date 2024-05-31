#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as file:
    letter_content = file.read()


#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as file:
    names = file.read()   


#Replace the [name] placeholder with the actual name. 
for name in names.split("\n"):   
    new_letters = letter_content.replace("[name]", name)   

    #Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as data:
        data.write(f"{new_letters}")  


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


