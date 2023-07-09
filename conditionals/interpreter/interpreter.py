#Richard Janssen <richardnjanssen@gmail.com>
#CS50 Introduction to Programming with Python
#Conditionals
#This program prompts the user for a simple equation like "x + y" and returns its results
#This calculator supports all basics operations (+,-,* and /)
#-------------------------------------------------

def main():
    equation = input("Equation: ").strip().split(" ")
    x = int(equation[0])
    y = equation[1]
    z = int(equation[2])
    print(calculator(x,y,z))

def calculator(x,y,z):
    match y:
        case "+":
            return float(x + z)
        case "-":
            return float(x - z)
        case "*":
            return float(x * z)
        case "/":
            if z==0:
                return "Math Error"
            else:
                return float(x / z)

main()