from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
on = True

choice = ''
while not choice == 'off':
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)) and \
                money_machine.make_payment(menu.find_drink(choice).cost):
            coffee_maker.make_coffee(menu.find_drink(choice))
