#Richard Janssen <richardnjanssen@gmail.com>
#20/07/2023
#CS50 Introduction to Programming with Python
#Exceptions
#This code converts a date from "dd/mm/aaaa" or "Month dd, aaaa" to a "YYYY-MM-DD"
#-------------------------------------------------
def convert_to_iso():
    while True: #This loop allows to prompt the user for a date untill a valid input
        date = input("Date: ").strip()
        months = {"January":1, #dictionary with month string and month number matching
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12}
        try:
            mm,dd,yyyy = date.split("/")
            mm = int(mm)
            dd = int(dd)
            yyyy = int(yyyy)
            if mm > 0 and mm < 13 and dd >0 and dd < 32:
                return print(f"{yyyy:02d}",f"{mm:02d}",f"{dd:02d}",sep="-")
                #02d is a format specifier that indicates the desired formatting. The 0 means to pad the number with zeros, the 2 sets the minimum width to 2 digits, and the d indicates that the value is an integer.
            else:
                None
        except ValueError:
            try:
                mmdd,yyyy = date.split(",")
                yyyy.strip()
                mm,dd = mmdd.split(" ")
                mm = months[mm]
                dd = int(dd)
                yyyy = int(yyyy)
                if mm > 0 and mm < 13 and dd >0 and dd < 32:
                    return print(f"{yyyy:02d}",f"{mm:02d}",f"{dd:02d}",sep="-")
                else:
                    None
            except KeyError:
                None
            except ValueError:
                None
            except TypeError:
                None

convert_to_iso()