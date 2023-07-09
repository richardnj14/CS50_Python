#Richard Janssen <richardnjanssen@gmail.com>
#CS50 Introduction to Programming with Python
#Functions and variables
#This program prompts the user for a meal price and for a tip percentage and returns tip value in dollar
#-------------------------------------------------

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$",""))


def percent_to_float(p):
    return float(p.replace("%",""))/100


main()