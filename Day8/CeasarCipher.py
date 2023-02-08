alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(encode_message, shift_number):
    encode = ""
    for letter in encode_message:
        pos = alphabet.index(letter)
        new_pos = shift_number + pos
        encode += alphabet[new_pos]
    return encode


def decrypt(decode_message, shift_number):
    decode = ""
    for letter in decode_message:
        pos = alphabet.index(letter)
        new_pos = pos - shift_number
        decode += alphabet[new_pos]
    return decode


option = input("Type 'encode' to encode your message...Type 'decode' to decode your message...")
message = input("Enter your message here...\n").lower()
shift = int(input("Type the shift number..."))

if option == "encode":
    final_encrypt = encrypt(message, shift)
    print(f"Your encrypted message is {final_encrypt}")

elif option == "decode":
    final_decrypt = decrypt(message, shift)
    print(f"Your encrypted message is {final_decrypt}")
