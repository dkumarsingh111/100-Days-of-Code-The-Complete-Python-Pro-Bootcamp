alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Encrypt Function
def encrypt(text, shift):
    encrypedText = ''
    for char in text:
        if char in alphabets:
           index = alphabets.index(char)
           position = index + shift
           while position > 25:
              position -= 26

           encrypedText += alphabets[position]
        else:
           encrypedText += char  
                             
    print(f"Encoded message: {encrypedText}")

#Decrypt Function
def decrypt(text, shift):
    decryptedText = ''
    for char in text:
        if char in alphabets:
          index = alphabets.index(char)
          position = index - shift
          while position < 0:
            position += 26

          decryptedText += alphabets[position]
        else:
           decryptedText += char

    print(f"Decoded secret message: {decryptedText}")   

is_continue = "yes"

while is_continue == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  text = input("Enter your message: ").lower()
  shift = int(input("Type the shift number: "))

  if(direction == "encode"):
    encrypt(text, shift) 
  elif(direction == "decode"):
    decrypt(text, shift)
  else:
    print("Enter correct direction!")
    
  is_continue = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()  

  if(is_continue == 'no'):
     print("Good Bye!")