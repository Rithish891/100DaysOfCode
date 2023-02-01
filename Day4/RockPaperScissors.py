import random

options = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''',
    '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''
]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer = random.randint(0, 2)

print("Player Choice: \n")
print(options[you])
print("\n Computer Choice: \n")
print(options[computer])

# if you == 0 and computer == 0:
#     print("It's a Draw!")
#
# elif you == 0 and computer == 1:
#     print("You Loose!")
#
# elif you == 0 and computer == 2:
#     print("You Win!")
#
# elif you == 1 and computer == 0:
#     print("You Win!")
#
# elif you == 1 and computer == 1:
#     print("It's a Draw!")
#
# elif you == 1 and computer == 2:
#     print("You Loose!")
#
# elif you == 2 and computer == 0:
#     print("You Loose!")
#
# elif you == 2 and computer == 1:
#     print("You Win!")
#
# elif you == 2 and computer == 2:
#     print("It's a Draw!")

if you > computer:
    print("You Win!")

elif you == computer:
    print("Its a Draw!")

elif computer > you:
    print("You Loose!")

elif you == 2 and computer == 0:
    print("You Loose!")

elif you == 0 and computer == 2:
    print("You Win!")

