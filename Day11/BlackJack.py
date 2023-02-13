import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def add_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You loose!"
    if player_score == computer_score:
        return "Draw!"
    elif player_score > 21:
        return "You Loose!"
    elif computer_score > 21:
        return "You Won!"
    elif computer_score == 0:
        return "You Loose!"
    elif player_score == 0:
        return "You Won!"
    elif player_score > computer_score:
        return "You Won!"


def play_game():
    print(logo)
    player_cards = []
    computer_cards = []

    for i in range(2):
        player_cards.append(add_card())
        computer_cards.append(add_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {player_cards} and the score is {player_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            player_should_add = input("Type 'y' to get another card...Type 'n' to pass... ")
            if player_should_add == "y":
                player_cards.append(add_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(add_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards are {player_cards} and your final score is {player_score}")
    print(f"Computer's final cards are {computer_cards} and the final score is {computer_score}")
    print(compare(player_score, computer_score))


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play == 'y':
    os.system('cls')
    play_game()
