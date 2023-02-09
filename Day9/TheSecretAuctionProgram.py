import os


# clear = lambda: os.system('cls')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

print("Welcome to the secret auction program\n")

bidder = True
auction = {}

while bidder:
    name = input('Enter your name... ')
    price = int(input("Enter your bid price... "))

    auction.update({name: price})

    choice = input("Are there any other bidders?...Yes/No... ").lower()
    if choice == "yes":
        clear()
        bidder = True

    else:
        bidder = False

max_bid = max(auction, key=lambda i: auction[i])
print(f"The winner is {max_bid} with a bid of {auction[max_bid]}")
