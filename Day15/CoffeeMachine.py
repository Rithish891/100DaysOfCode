import menu 

money = 0
coffee = True

while coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        coffee = False
    elif choice == "report":
        print(f"Water: {menu.resources['water']}ml")
        print(f"Milk: {menu.resources['milk']}ml")
        print(f"Coffee: {menu.resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        for i in menu.items_list[choice]["ingredients"]:
            if menu.items_list[choice]["ingredients"][i] > menu.resources[i]:
                print(f"Not enough {i}.")
                items = False
            else:
                items = True
        if items:
            print("Insert coins.")
            total = int(input("Quarters?: ")) * 0.25
            total += int(input("Dimes?: ")) * 0.1
            total += int(input("Nickles?: ")) * 0.05
            total += int(input("Pennies?: ")) * 0.01
            if total >= menu.items_list[choice]["cost"]:
                change = round(total - menu.items_list[choice]["cost"], 2)
                print(f"Collect your change {change}.")
                money += total
                for item in menu.items_list[choice]["ingredients"]:
                    menu.resources[item] -= menu.items_list[choice]["ingredients"][item]
                print(f"Here is your {choice}!")
            else:
                print("Not enough money...Refund initiated.")
    