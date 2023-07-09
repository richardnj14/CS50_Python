#Richard Janssen <richardnjanssen@gmail.com>
#CS50 Introduction to Programming with Python
#Loops
#This program promps the user for a camel case string and returns the same string snake case converted
#thisIsACamelCase
#this_is_a_snake_case
#-------------------------------------------------
def main():
    camelCase=input("camelCase: ")
    print("snake_case: ",convert_to_snake(camelCase))

def convert_to_snake(user_str):
    j=0
    str_matrix=[""]
    for s in user_str:
        if s.islower():
            str_matrix[j] = str_matrix[j] + s.lower()
        elif s.isupper():
            str_matrix.append(s.lower())
            j+=1
    return "_".join(str_matrix) #"_".join() allows to add all itens of a list in the same string "_" separated

main()