#Richard Janssen <richardnjanssen@gmail.com>
#CS50 Introduction to Programming with Python
#Functions and variables
#This program prompts the user for a mass value and converts it into a energy value by the Einstein formule E = mc²
#-------------------------------------------------

def main():
    mass = int(input("Enter the mass in kg?\n"))
    print(einstein_equation(mass),"J")

def einstein_equation(m):
    return int(m*pow(3e8,2))

main()