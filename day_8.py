# Caesar Cipher

# import the logo
from art import logo

# Defining the encryption and decryption process for letters only
def caesar(text, shift, direction):
    if direction == "decode":
        shift = -shift
    new_text = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_letter = alphabet[letter_index+shift]
            new_text += new_letter
        else:
            new_text+=letter
    print(new_text)

# Print the logo
print(logo)

# Setting the variables required and the data base of letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2
go_on = True
# Continue until user stops us
while go_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

# Dealing with shifts larger than the length of the alphabet
    if shift > 26:
        shift = shift % 26


    caesar(text, shift, direction)
    keep = input("Do you want to keep going?\n")
    if keep.lower()!= "yes":
        go_on = False