import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_count = int(input("How many letters do you need in your password? "))
numbers_count = int(input("How many numbers do you need in your password? "))
symbols_count = int(input("How many symbols do you need in your password? "))

password = []

for i in range(letters_count):
    password.append(random.choice(letters))

for i in range(numbers_count):
    password.append(random.choice(numbers))

for i in range(symbols_count):
    password.append(random.choice(symbols))

random.shuffle(password)

pswd = ""

for i in password:
    pswd += i

print(pswd)