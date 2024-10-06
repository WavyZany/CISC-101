"""
This program determines whether a student will be admitted to
a computing plan, put on the pending list or rejected based
on their marks in CISC 121/CISC 124 and their gpa.

Author: Zane Al-Hamwy
Date: September 2024
"""

def main():
    grade121, grade124 = getMarks()
    overallGPA = getGPA()
    overallOutcome = determineOutcome(grade121, grade124, overallGPA)
    informOfOutcome(overallOutcome)
    
def getMarks():
    #assume they have taken 121
    cisc121Mark = input("Please enter your mark in CISC 121 (A, B, C, D, E, F) ")
    cisc121Mark = cisc121Mark.upper()

    #check to see if they have taken 124
    taken124 = input("Have you taken CISC 124? (Y/N) ")
    if taken124 == "Y" or taken124 == "y":
        cisc124Mark = input("Please enter your mark in CISC 124 (A, B, C, D, E, F) ")
        cisc124Mark = cisc124Mark.upper()
       

    else:
        #set to F to indicate not taken -- this will not get them into a plan
        cisc124Mark = "F"
        
    return cisc121Mark, cisc124Mark

def getGPA():
    #get gpa
    gpa = float(input("Please enter your gpa(float) "))
    return gpa

def determineOutcome(grade121, grade124, gpa):



    if gpa < 0 or gpa > 4.3:
        print("You have entered an invalid gpa -- no result available")
    else:
        #automatic acceptance?
        #note in string comparison, a "B" is less than an "A"
        if gpa >= 2.6 and (grade121 <= "B" or grade124 <= "B"):
            return "Accepted"

        #pending list
        elif gpa >= 2.0 and (grade121 <= "C" or grade124 <= "C"):
            return "Pending"

        #not eligible
        else:
            return "Not Eligible"

def informOfOutcome(outcome):
        print("Your current acceptance status is:", outcome)

main()

