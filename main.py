from menu import *
from aux_functions import *
money = 0.0
off = True
while off:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user == 'off':
        off = False
    elif user == 'report':
        print(f"Watter: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user == 'espresso':
        if rss_water(50) and rss_coffee(18):
            print("Please insert the coins.")
            if check_coins() >= 1.50:
                change = check() - 1.50
                print(f"Here is ${round(change, 2)} in change")
                print("Here is your espresso ☕. Enjoy!")
                resources['water'] -= 50
                resources['coffee'] -= 18
                money += 1.50
            elif check() < 1.50:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources to prepare the espresso.")
    elif user == 'latte':
        if rss_water(200) and rss_coffee(24) and rss_milk(150):
            print("Please insert the coins.")
            if check_coins() >= 2.50:
                change = check() - 2.50
                print(f"Here is ${round(change, 2)} in change")
                print("Here is your latte ☕. Enjoy!")
                resources['water'] -= 200
                resources['coffee'] -= 24
                resources['milk'] -= 150
                money += 2.50
            elif check() < 2.50:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources to prepare the espresso.")
    elif user == 'cappuccino':
        if rss_water(250) and rss_coffee(24) and rss_milk(100):
            print("Please insert the coins.")
            if check_coins() >= 3.00:
                change = check() - 3.00
                print(f"Here is ${round(change, 2)} in change")
                print("Here is your cappuccino ☕️.Enjoy!")
                resources['water'] -= 250
                resources['coffee'] -= 24
                resources['milk'] -= 100
                money += 3.00
            elif check() < 3.00:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough resources to prepare the espresso.")
    else:
        print("Wrong order!")
        off = False
