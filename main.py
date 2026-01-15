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
}

profit = 0


def check_resources(choice, resources_a):
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources_a[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    print("Please insert the coins")
    return True


def check_money(total):
    global profit
    cost = MENU[user_choice]["cost"]

    if total >= cost:
        change = round(total - cost, 2)
        profit += cost
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        print(f"Here is your {user_choice}. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def update_resources():
    ingredients = MENU[user_choice]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]


continue_drink = True

while continue_drink:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        continue_drink = False

    elif user_choice == "report":
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : {profit}")

    elif user_choice in MENU:
        if check_resources(user_choice, resources):

            quarter = int(input("quarters: "))
            dimes = int(input("dimes: "))
            nickels = int(input("nickels: "))
            pennies = int(input("pennies: "))

            total = (
                quarter * 0.25 +
                dimes * 0.10 +
                nickels * 0.05 +
                pennies * 0.01
            )

            if check_money(total):
                update_resources()

    else:
        print("Invalid choice.")
