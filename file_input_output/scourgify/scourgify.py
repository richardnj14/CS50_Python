#Richard Janssen <richardnjanssen@gmail.com>
#27/07/2023
#CS50 Introduction to Programming with Python
#File Input/Output
#This program takes two command-line arguments, the first one is a csv file to "clean" and the second
#is also the output file name. This program converts data from csv file in a cleaned data
#the save it like a new file
#For instance:
#"Potter,Harry", gryffindor --> Potter, Harry, gryffindor
#You can use "before.csv" as command-line argument to test this script
# ------------------------------------------------
import sys
import csv

def main():
    with open(sys.argv[1], "r", newline='') as input_file:
        reader = csv.DictReader(input_file)
        with open(sys.argv[2], "w", newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for line in reader:
                writer.writerow(convert(line))

def convert(row):
    merged_name, house = row["name"], row["house"]
    last_name, first_name = merged_name.split(",")
    last_name = last_name.strip()
    first_name = first_name.strip()
    return {"first": first_name, "last": last_name, "house": house}



def argv_check(argv):
    if len(argv) > 3:
        sys.exit("Too many command-line arguments.")
    elif len(argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif argv[1][-4:] != ".csv":
        sys.exit("Not a .csv file.")
    try:
        open(sys.argv[1],"r")
    except FileNotFoundError:
        sys.exit("Can't find the file.")

if __name__ == "__main__":
    main()