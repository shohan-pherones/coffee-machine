MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def get_user_choice():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many coins?: "))
    return total

def is_transaction_successful(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that’s not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def coffee_machine():
    is_on = True

    while is_on:
        choice = get_user_choice()

        if choice == "off":
            is_on = False
            print("Turning off the coffee machine.")
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif choice == "refill":
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
            print("Resources refilled successfully.")
        else:
            drink = MENU.get(choice)
            if drink:
                if is_resource_sufficient(drink["ingredients"]):
                    payment = process_coins()
                    if is_transaction_successful(payment, drink["cost"]):
                        make_coffee(choice, drink["ingredients"])

coffee_machine()