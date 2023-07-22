#Richard Janssen <richardnjanssen@gmail.com>
#22/07/2023
#CS50 Introduction to Programming with Python
#Libraries
#This code prompts a user for a integer > 0 level and a integer > 0 guess
#After, generates a random number between 1 and level number and compares it to user guess
#If guess = random number the user wins the game
#-------------------------------------------------


import random

def main():
    level = get_integer("Level: ")
    n = get_integer("Guess: ")
    randonint = random.randint(1,level)
    if n == randonint:
        print("Just right!")
    elif n < randonint:
        print("Too small!")
    else:
        print("Too large!")


def get_integer(str): #this function prompts a user and only accepts integer > 0 numbers
    while True:
        try:
            integer = int(input(str))
            if integer > 0:
                return integer
            else:
                None
        except ValueError:
            None

main()