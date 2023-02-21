from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = True

while coffee:
    choice = input(f"What would you like? ({Menu().get_items()}): ").lower()
    if choice == "off":
        coffee = False

    elif choice == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        if CoffeeMaker().is_resource_sufficient(Menu().find_drink(choice)):
            if MoneyMachine().make_payment(Menu().find_drink(choice)):
                CoffeeMaker().make_coffee(Menu().find_drink(choice))
