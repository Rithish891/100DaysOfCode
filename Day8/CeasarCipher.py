print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(encode_message, shift_number):
#     encode = ""
#     for letter in encode_message:
#         pos = alphabet.index(letter)
#         new_pos = shift_number + pos
#         encode += alphabet[new_pos]
#     return encode
#
#
# def decrypt(decode_message, shift_number):
#     decode = ""
#     for letter in decode_message:
#         pos = alphabet.index(letter)
#         new_pos = pos - shift_number
#         decode += alphabet[new_pos]
#     return decode

def cipher(cipher_message, shift_number, direction):
    final_message = ""
    if direction == "decode":
        shift_number *= -1
    for letter in cipher_message:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = pos + shift_number
            final_message += alphabet[new_pos]
        else:
            final_message += letter
    return final_message


again = True

while again:
    option = input("Type 'encode' to encode your message...Type 'decode' to decode your message...")
    message = input("Enter your message here...\n").lower()
    shift = int(input("Type the shift number..."))

    print(f"Your {option}d message is {cipher(message, shift, option)}")

    loop = input("Do you want to go again?...Yes/No??").lower()
    if loop == "yes":
        again = True
    else:
        again = False

    # if option == "encode":
    #     final_encrypt = encrypt(message, shift)
    #     print(f"Your encrypted message is {final_encrypt}\n")
    #
    #     loop = input("Do you want to go again?...Yes/No??").lower()
    #     if loop == "yes":
    #         again = True
    #     else:
    #         again = False
    #
    # elif option == "decode":
    #     final_decrypt = decrypt(message, shift)
    #     print(f"Your encrypted message is {final_decrypt}")
    #
    #     loop = input("Do you want to go again?...Yes/No??").lower()
    #     if loop == "yes":
    #         again = True
    #     else:
    #         again = False
