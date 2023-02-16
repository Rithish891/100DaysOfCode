import os
import random

import art
import game_data

in_game = True
score = 0
print(art.logo)
while in_game:
    if score > 0:
        os.system('cls')
        print(f"You are correct! Current score is {score}")

    compare = random.sample(game_data.data, 2)
    print(compare)
    a_name = compare[0]['name']
    a_des = compare[0]['description']
    a_country = compare[0]['country']
    b_name = compare[1]['name']
    b_des = compare[1]['description']
    b_country = compare[1]['country']
    print(f"Compare A: {a_name} a {a_des}, from {a_country}")
    print(art.vs)
    print(f"Compare B: {b_name} a {b_des}, from {b_country}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == 'b' and compare[1]['follower_count'] > compare[0]['follower_count']:
        score += 1
    elif choice == 'a' and compare[0]['follower_count'] > compare[1]['follower_count']:
        score += 1
    else:
        print(f"You guessed it wrong. Final score is {score}")
        in_game = False
