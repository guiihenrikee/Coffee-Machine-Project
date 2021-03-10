from menu import *


def check_coins():
    """Returns the total calculated from coins inserted"""
    global total
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def check():
    """Returns just the total, without input function"""
    return total


def rss_water(x):
    if x <= resources['water']:
        return True
    else:
        return False


def rss_milk(x):
    if x <= resources['milk']:
        return True
    else:
        return False


def rss_coffee(x):
    if x <= resources['coffee']:
        return True
    else:
        return False
