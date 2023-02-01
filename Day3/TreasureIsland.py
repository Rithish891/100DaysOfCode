print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

direction = input("Choose the direction in which you wish to start the game. Right? or Left?")

if direction.lower() == 'left':
    print("You reached the sea of terror")
    action = input("Do you want to wait for the BOAT? or Do you want to SWIM?")
    if action.lower() == 'boat':
        print("Get on to the boat, It will take you the Island of treasure")
        door = input("Choose a door to find the treasure. Red? Blue? Yellow")
        if door.lower() == 'red':
            print("Burned by fire. GAME OVER!")
        elif door.lower() == 'blue':
            print("Eaten by beasts. GAME OVER!")
        elif door.lower() == 'yellow':
            print("Congratulations! The treasure is all yours!!")
        else:
            print("GAME OVER!")

    else:
        print("Attacked by trout. GAME OVER!")
else:
    print("You fell in the hole. GAME OVER!")
