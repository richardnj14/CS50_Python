#Richard Janssen <richardnjanssen@gmail.com>
#02/07/2023
#CS50 Introduction to Programming with Python
#This program prompts the user for a fraction like "1/3" and converts it to a percentage value
#if >99% it prints F for "Full"
#if <1% it prints E for "Empty"
#-------------------------------------------------

def main():
    while True:
        try:
            user_str = input("Fraction: ")
            print(gauge(convert(user_str)))
            break
        except ValueError:
            None
        except ZeroDivisionError:
            None

def convert(str):
    num,den = str.split("/")
    num = int(num)
    den = int(den)
    frac = round(num/den*100)
    if frac <= 100 and frac >= 0:
        return frac
    else:
        raise ValueError

def gauge(x):
    if x < 99 and x > 1:
        return f"{x}%"
    elif x >= 99 and x <= 100 :
        return "F"
    elif x <= 1 and x >= 0:
        return "E"

if __name__ == "__main__":
    main()