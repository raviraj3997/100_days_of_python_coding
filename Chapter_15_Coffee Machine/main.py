MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0,
}


def sufficient_resources(drink):
    """
    Functions check if there are sufficient resources.
    :param drink: (string) the drink you ordered
    :return: (Bool) Whether there are sufficient resources.
    """
    drink_ingredients = MENU[drink]['ingredients']
    for resource in drink_ingredients.keys():
        if drink_ingredients[resource] > resources[resource]:
            print(f'Sorry there is not enough {resource}.')
            return False
    return True


def update_resource(drink):
    """
    Functions updates the available resources.
    :param drink: (string) the drink you ordered
    :return: None.
    """
    drink_ingredients = MENU[drink]['ingredients']
    for resource in drink_ingredients.keys():
        resources[resource] = resources[resource] - drink_ingredients[resource]
    resources['money'] = resources['money'] + MENU[drink]['cost']


def process_coins():
    """
    :return: (float) returns the total value of all entered coins
    """
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total


machine_on = True

while machine_on:

    drink_required = input("What would you like? (espresso/latte/cappuccino):")

    if drink_required == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money6: ${resources["money"]}')

    elif drink_required == 'off':
        machine_on = False

    elif drink_required in MENU.keys():
        if not sufficient_resources(drink_required):
            continue
        entered_coins = process_coins()
        if entered_coins >= MENU[drink_required]['cost']:
            change = entered_coins - MENU[drink_required]['cost']
            if change != 0.0:
                print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {drink_required}. Enjoy!!")
            update_resource(drink_required)
        else:
            print("Sorry not enough money. Money refunded.")
    else:
        print("Invalid input")


print("Powering off the coffee machine. Thanks!")
