#Richard Janssen <richardnjanssen@gmail.com>
#CS50 Introduction to Programming with Python
#Conditionals
#This program prompts the user for a time and retunrs the corresponding meal time 
#time format accepteds : 
# hh:mm
# hh:mm a.m.
# hh:mma.m
#-------------------------------------------------

def main():
    t = input("What time is it?\n").strip()
    if convert(t) >= 7 and convert(t) <= 8:
        print("breakfast time")
    elif convert(t) >= 12 and convert(t) <= 13:
        print("lunch time")
    elif convert(t) >= 18 and convert(t) <= 19:
        print("dinner time")
    else:
        None

def convert(time):
    time = time.strip()
    hh_mm = (
        time.replace(" a.m.", "")
        .replace(" p.m.", "")
        .replace("a.m.", "")
        .replace("p.m.", "")
        .split(":")
    )
    hh = int(hh_mm[0])
    mm = int(hh_mm[1]) / 60 #converts minutes to hour
    am_pm = time[-4:] #I need to use the ":" to indicates that I want the last four characters
    return hh + mm + 12 if am_pm == "p.m." else hh + mm


if __name__ == "__main__": #The main function will be called just when I execute this function from here
    main()