from art import logo
from resources_data import resources
from menu_data import MENU

is_machine_on = True

print(logo)

# TODO-1: print report.
def print_report():
    """ Generate resources report """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# TODO-2: set resources info.
def set_resources_info(water, milk, coffee, money):
    """ set resources data"""
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    resources['money'] += money


# TODO-3: check resources quantity.
def is_resources_sufficient(resource):
    """ check resources quantity """
    if resources['water'] >= MENU[f"{resource}"]["ingredients"]["water"]:
        if resources['coffee'] >= MENU[f"{resource}"]["ingredients"]["coffee"]:
            if resources['milk'] >= MENU[f"{resource}"]["ingredients"]["milk"]:
                return True
            else:
                return "milk"
        else:
            return "coffee"
    else:
        return "water"
    

# TODO-4: process coins.    
def process_coin(choice):
    """ process coins """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    refund = total - MENU[f"{choice}"]["cost"]
    if refund > 0:
        print(f"Here is ${round(refund, 2)} in change.")
    return (total >= MENU[f"{choice}"]["cost"])



while is_machine_on:
    choice = input("What do you like? (espresso/ latte/ cappuccino): ")
    if choice == "off":
        is_machine_on = False    
    elif choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resource = is_resources_sufficient(choice)
        if resource == True:
            if process_coin(choice):  
                set_resources_info(MENU[f"{choice}"]["ingredients"]["water"], MENU[f"{choice}"]["ingredients"]["milk"], MENU[f"{choice}"]["ingredients"]["coffee"], MENU[f"{choice}"]["cost"])            
                print(f"Here is your {choice} enjoy!\n")
            else:
                print(f"Sorry that's not enough money. Money refunded.\n")             
        else:
            print(f"Sorry there is not enough {resource}.\n")
    else:
        print("Please enter correct choice!\n")