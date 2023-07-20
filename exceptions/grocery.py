#Richard Janssen <richardnjanssen@gmail.com>
#20/07/2023
#CS50 Introduction to Programming with Python
#Exceptions
#This code allows a user to enter items for a grocery list and when stopped by user 
#return the list items and the quantity of each one
#-------------------------------------------------
def main(): #define the main fonction
    grocery_list = dict() #create a new empty dictionary
    while True: #prompt the user until a ctrl+d
        try: #try to get a new input
            new_item = input().upper() #get a input and coverts to uppercase
            if new_item in grocery_list: #if the input already exist in dictionary
                grocery_list[new_item] += 1 #add 1 in the quantity
            else: #if the input doesn't exist in the dictionary:
                grocery_list[new_item] = 1 #create a new dict key with the user string and add 1 to the associated value
        except EOFError: #if ctrl+d, sort alphabetically the list and prints it
            grocery_list = dict(sorted(grocery_list.items())) #sorted() alows to get a list alphabetically sorted .items do the sort with the items (keys and values)
            for item in grocery_list: #alows to print every item of a dictionnary
                print(grocery_list[item],item)
            break
main()