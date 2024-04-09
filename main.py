from menu import MENU, resources

revenue = 0


# Check resources sufficient?
def check_resources(order_ingredients):
    """Returns True when there is sufficient ingredients to make the order."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total from coins inserted"""
    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


# Check transaction successful
def check_transaction_successful(coins_inserted, drink_cost):
    """Returns True when payment is sufficient, or False when money is not sufficient"""
    if coins_inserted >= drink_cost:
        global revenue
        revenue += drink['cost']
        change = coins_inserted - drink_cost
        print(f"Here is {change:.2f} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients used for the drink from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕️ Enjoy!")


finishing_order = False

while not finishing_order:
    # check the user's input to decide what to do next
    user_choice = input("What would you like? (espresso/latte/cappuccino)")

    # Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == 'off':
        finishing_order = True
    elif user_choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {revenue}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
