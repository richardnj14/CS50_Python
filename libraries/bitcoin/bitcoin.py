#Richard Janssen <richardnjanssen@gmail.com>
#22/07/2023
#CS50 Introduction to Programming with Python
#Libraries
#This code get some bitcoin amount on a command-line argument and converts it to dollar cost
#Command-line argument need to be a number
#-------------------------------------------------

import requests #import http library to requests some api
import sys

def main():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json() #request JSON from API
        rate = r["bpi"]["USD"]["rate"] #get the rate to USD currency
        rate = float(rate.replace(",","")) #converts the string rate to a float
        cost = float(sys.argv[1])*rate
        print(f"${cost:,.2f}", sep="")
    except ValueError:
        sys.exit("Command-line argument need to be a number")
    except IndexError:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()