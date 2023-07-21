alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_lenght = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    if (cipher_direction == "decode"):
        shift_amount *= -1

    for char in start_text:

        if char not in alphabet:
            end_text += char
        
        else:
            index = alphabet.index(char)
            shift_value = index + shift_amount

            if (shift_value < alphabet_lenght and shift_value >= alphabet_lenght):
                end_text += alphabet[shift_value]

            elif (shift_value < 0):
                end_text += alphabet[shift_value + alphabet_lenght]

            else:
                end_text += alphabet[shift_value - alphabet_lenght]
                  
    print (f"The {cipher_direction}d text is {end_text}")

# Importing Caesar Cipher Logo
from art import logo
print(logo)

# Continuously run the code till user want to End
should_end = False

while not should_end:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Triming the Shift if it goes beyond 26 (no. of alphabets).
    while shift > alphabet_lenght:
        shift -= alphabet_lenght
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # restarting/ending the caser cipher as per user input. 
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    if restart == "no":
        should_end = True
        print("Goodbye")





# Encoding and decoding code seperately
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# encryption
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    alphabet_lenght = len(alphabet)
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
        else:
            index = alphabet.index(char)
            shift_value = index + shift
            if (shift_value < alphabet_lenght):
                cipher_text += alphabet[shift_value]
            else:
                cipher_text += alphabet[shift_value - alphabet_lenght]
    print (f"The encoded text is {cipher_text}")

# decryption
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    alphabet_lenght = len(alphabet)
    for char in cipher_text:
        if char not in alphabet:
            plain_text += char
        else:
            index = alphabet.index(char)
            shift_value = index - shift
            if (shift_value < 0):
                plain_text += alphabet[shift_value + alphabet_lenght]
            else:
                plain_text += alphabet[shift_value]
                
    print (f"The encoded text is {plain_text}")



# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' variable.

if (direction == "encode"):
    encrypt(plain_text=text, shift_amount=shift)
elif(direction == "decode"):
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Please enter correct value")

'''