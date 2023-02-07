import random
import words
import lives

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/        
''')

word = random.choice(words.words_list)
print("Start guessing the letter in the word!\n")

blank_list = []

for i in range(len(word)):
    blank_list.append('_')
print(blank_list)

in_game = True
life = 6

while in_game:

    letter = input("Take a guess: ").lower()
    print("\n")

    if letter in blank_list:
        print(f"You have already guessed the letter {letter}...Try guessing another letter!")

    if word.__contains__(letter):
        for pos in range(len(word)):
            if word[pos] == letter:
                blank_list[pos] = letter
        print(blank_list)

    else:
        life -= 1
        print("The letter you guessed is not present in the word...Try again!")
        print(lives.stages[life])

        print(blank_list)

        if life == 0:
            print("YOU LOOSE!\n")
            print(f"The word is {word}...Better luck next time!!!")
            in_game = False

    if '_' not in blank_list:
        print("YOU WIN!")
        in_game = False

    else:
        continue
