alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Enter your message: ").lower()
shift = int(input("Type the shift number: "))
encodedText = ''
decodedText = ''
 

def encode_function(text, shift):
    for char in text:
        index = alphabets.index(char)
        encodedText += alphabets[index + shift]
                             
    print(f"Encoded secret message: {encodedText}")


def decode_function(text, shift):
    for char in encodedText:
        index = alphabets.index(char)
        decodedText += alphabets[index - shift]

    print(f"Decoded secret message: {decodedText}")   




if(direction == "encode"):
  encode_function(text, shift)
elif(direction == "decode"):
  decode_function(text, shift)
else:
  print("Enter correct direction!")