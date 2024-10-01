"""

This program calculates the amount each person should pay for the bill (split evenly)
Author: Z. Al-Hamwy
Student Number: 20453474
Date: 13 September 2024

"""

total = float(input("What is the total bill? "))
tip = total * 0.18

total = total + tip
print("The total amount with tip included is:", total)

people = int(input("How many people are splitting the bill? "))
total = total / people

print("Each person should contribute", total)
