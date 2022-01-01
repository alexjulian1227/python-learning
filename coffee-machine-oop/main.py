from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}):   ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"{drink.name} is ${drink.cost}")
            money_machine.process_coins()
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


