"""
This program indicates whether a student is eligible for automatic, pending, or not eligible for admission into a computing plan
Author: Z. Al-Hamwy
Student Number: 20453474
Date: 13 September 2024
"""

# Initializing variables
grade121 = input("Enter your grade for CISC 121: ")
grade124 = "F"

# Making sure a valid option is entered for whether they took CISC 124 
try:
    taken124 = int(input("Have you taken CISC 124? (Enter 1 for yes and 0 for no)"))
except:
     print("Please enter a valid option")
     
if taken124 == 1:
    grade124 = input("Enter your grade for CISC 124: ")
elif taken124 == 0:
    pass


# Converting to upper case
grade121 = grade121.upper()
grade124 = grade124.upper()

# Obtaining GPA
gpa = float(input("Enter your GPA: "))

# Checking if GPA is valid
if gpa < 0 or gpa > 4.3:
    print("Invalid GPA")

# If GPA is greater than 2.0, we need to check if grades in CISC 121/124 are higher than C
elif gpa >= 2.0:
    # Using < because ASCII reads "A" as 65 and "B" as 66
    if grade121 < "C" or grade124 < "C":
        print("Automatically accepted into a Computing plan!")
    elif grade121 < "D" or grade124 < "D":
        print("Pending acceptance into a Computing plan.")
    else:
        print("Not eligible for admission.")
else:
    print("Not eligible for admission.")
    
