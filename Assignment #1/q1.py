"""

This program calculates the number of animals seen from values given by user
Author: Z. Al-Hamwy
Student Number: 20453474
Date: 13 September 2024

"""
# Taking input of animals/nests/holes seen
nests = int(input("Please enter the number of squirrel nests that you saw "))
holes = int(input("Please enter the number of chipmunk holes that you saw "))
deers = int(input("How many deer did you see? "))
    
# Calculating Squirrels/Chipmunks seen in each nest or hole respectively
squirrels = nests * 4
chipmunks = holes * 14

# Total amount of animals
total = squirrels + chipmunks + deers


# Output to let the user know
print("You encountered", squirrels, "squirrels", chipmunks, "chipmunks and", deers, "deer")
print("That is a total of", total, "animals")
