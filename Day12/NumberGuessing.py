import random
print('''
  
  _   _                 _                  _____                    _             
 | \ | |               | |                / ____|                  (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___ ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ | '__| | | |_ | | | |/ _ / __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __| |    | |__| | |_| |  __\__ \__ | | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___|___|___|_|_| |_|\__, |
                                                                             __/ |
                                                                            |___/ 
''')
print("Welcome to the number Guessing game!")
print("Guess the number ranging from 1 to 100")

random_number = random.randint(1, 100)


def guessing_game(chances):
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too High.")
        print("Guess again!")
        easy_game(chances - 1)
    elif guess < random_number:
        print("Too Low.")
        print("Guess again!")
        easy_game(chances - 1)
    elif guess == random_number:
        print(f"You got it! The number was {random_number}")


def easy_game(chances):
    print(f"You have {chances} attempts to guess the number")

    if chances == 0:
        print("You've ran out of guesses. YOU LOOSE!")

    else:
        guessing_game(chances)


def hard_game(chances):
    print(f"You have {chances} attempts to guess the number")

    if chances == 0:
        print("You've ran out of guesses. YOU LOOSE!")

    else:
        guessing_game(chances)


if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
    easy = 10
    easy_game(easy)
else:
    hard = 5
    hard_game(hard)
