# Coffee machine project

# importing the system module for exiting
import sys

# MENU and resources
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

select_drink = True

while select_drink:
    # Get a drink
    drink = input( "What would you like? (espresso/latte/cappuccino): ")

    # setting up a report
    if drink == "report":
        for resource in resources.items():
            print(f"{resource[0].title()}: {resource[1]}ml")
    # turning the machine off
    elif drink == "off":
        sys.exit("The machine is turned off.")

    elif drink in MENU:
        # Check resource sufficiency
        available_resources = "yes"
        for resource in resources.items():
            # checking whether there are enough resources
            if resource[1] < MENU[drink]["ingredients"][resource[0]]:
                available_resources = "no"
                print(f"Sorry there is not enough {resource[0]}")
                break
        if available_resources == "yes":
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01

            # Check if money inserted can cover the costs
            if MENU[drink]["cost"] > money_inserted:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["Money"] = MENU[drink]["cost"]
                if money_inserted > MENU[drink]["cost"]:
                    print(f"Here is ${round(money_inserted-MENU[drink]['cost'],2)} dollars in change.")
                for resource in resources:
                    if resource != "Money":
                        resources[resource] -= MENU[drink]["ingredients"][resource]
                print(f"Here is your {drink}. Enjoy!")        






