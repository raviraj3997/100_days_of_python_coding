from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_collector = MoneyMachine()

is_on = True

while is_on:
    drink = input(f"What would you like? {menu.get_items()}:")
    if drink == 'report':
        coffee_machine.report()
        money_collector.report()
    elif drink == 'off':
        is_on = False
    else:
        ordered_drink = menu.find_drink(drink)
        if coffee_machine.is_resource_sufficient(ordered_drink):
            if money_collector.make_payment(ordered_drink.cost):
                coffee_machine.make_coffee(ordered_drink)

print('powering off the machine. Thanks!')
