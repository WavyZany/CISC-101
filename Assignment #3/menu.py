"""
This program creates a menu of unrelated items
Author: Z. Al-Hamwy
Student Number: 20453474
Date: 5 October 2024
"""
def main():
    userInput = menu()

    if userInput == 1:
        name = input("What is your name?")
        poem(name)
    elif userInput == 2:
        mealPrice = float(input("What was the price of your meal?"))
        tipPercentage = float(input("What percent tip do you want to give?"))
        overallTip = tip(mealPrice, tipPercentage)
        print("Your tip for the meal is", overallTip)
    elif userInput == 3:
        americanDollar = float(input("Enter Amercian Dollars"))
        print("Your total in Canadian Dollars is", exchange(americanDollar))
    else:
        print("Invalid option")


def menu():
    print("1. Print a poem")
    print("2. Calculate a tip given a meal price and tip percentage")
    print("3. Translate US dollars to Canadian")
    print("\nEnter the number corresponding to the item that you want to run:")

    userInput = int(input())
    return userInput

def poem(Name):
    print("Rose are red")
    print("Violets are blue")
    print(Name + ",", "this poem")
    print("Was written for you")

def tip(mealPrice, tipPercent):
    tip = mealPrice * (tipPercent / 100)
    return tip

def exchange(americanDollar):
    canadianDollar = americanDollar * 1.30
    return canadianDollar
    
main()