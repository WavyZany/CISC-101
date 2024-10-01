"""

This program calculates the distance between two points
Author: Z. Al-Hamwy
Student Number: 20453474
Date: 13 September 2024

"""
import math

# First coordinate
x1 = int(input("Please enter the x coordinate of the first point: "))
y1 = int(input("Please enter the y coordinate of the first point: "))

# Second coordinate
x2 = int(input("Please enter the x coordinate of the second point: "))
y2 = int(input("Please enter the y coordinate of the second point: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("The distance between the two points is", distance)
