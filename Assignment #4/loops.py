'''
This program is a series of functions created on one file
Author: Z. Al-Hamwy
Student Number: 20453474
Date: 20 October 2024
'''
import random

def diceRollInput():
    """
    Purpose - This function takes input from the user of the amount of rolls and if out of range repeatedly prompts the user
    Parameters - None
    Return Value - The number of dice rolls the user wants from 1-500
    """

    numRolls = int(input("How many rolls would you like from 1-500? "))
    while numRolls < 1 or numRolls > 500:
        numRolls = int(input("Please enter in a valid range from 1-500: "))
    
    return numRolls

def diceRoll(numRolls):
    total = 0
    for i in range(1, numRolls + 1):
        randomNum1 = random.randint(5,10)
        randomNum2 = random.randint(5,10)
        total = total + randomNum1 + randomNum2
    
    return total


def numSumInput():
    n = int(input("Enter a number, n: "))
    m = int(input("Enter a number, m: "))
    while m <= n:
        print("Please enter numbers such that m > n")
        n = int(input("Enter another number, n:"))
        m = int(input("Enter another number, m:"))
    
    return (n, m)
    
def numSum(n, m):
    sum = 0
    for i in range(n, m + 1):
        sum = sum + i
    
    print("The sum of the range is", sum)
    return sum


def getBaseHeight():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    while base < 0 or height <0:
        print("Please enter valid numbers that are not negative")
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))

    return base, height

def halfAreaTriangle(base, height):
    halfArea = ((base * height) / 2) / 2
    return halfArea


def menu():
    print("1) Dice Roll - Rolls a pair of die and returns the total rolled")
    print("2) Number Sum - Returns the sum from a range of numbers")
    print("3) Half Area Triange - Returns half of the area of a triangle")
    print("4) Quit the program")
    choice = 0

    while choice != 4:
        choice = int(input("Please enter an option: "))

            
        if choice == 1:
            x = diceRollInput()
            print(diceRoll(x))
        elif choice == 2:
            x, y = numSumInput()
            print(numSum(x, y))
        elif choice == 3:
            b, h = getBaseHeight()
            print(halfAreaTriangle(b, h))
        else:
            print("Please enter valid input!")

menu()

    

