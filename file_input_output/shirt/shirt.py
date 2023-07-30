#Richard Janssen <richardnjanssen@gmail.com>
#28/07/2023
#CS50 Introduction to Programming with Python
#File Input/Output
#This program expect for two command-line arguments, the first one is a image file input and the second
#is the output file name or path. This program overlay a "shirt image" on the given input file
#input and output are expected to have same format (.jpeg, .jpg, or .png)
# ------------------------------------------------
import sys
import PIL
from PIL import Image

def main():
    check_argv(sys.argv)
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as input:
        resized = PIL.ImageOps.fit(input, shirt.size)
        resized.paste(shirt,shirt)
        resized.save(sys.argv[2])

def check_argv(argv):
    if len(argv) > 3:
        sys.exit("Too many command-line arguments.")
    elif len(argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif get_extension(argv[1]) not in ["jpg", "jpeg", "png"]:
        sys.exit("Not a valid format file.")
    elif get_extension(argv[1]) != get_extension(argv[2]):
        sys.exit("Input and output must have the same format")
    try:
        open(sys.argv[1],"r")
    except FileNotFoundError:
        sys.exit("Can't find the file.")

def get_extension(str):
    return str.rsplit(".",1)[1]

if __name__ == "__main__":
    main()