#Richard Janssen <richardnjanssen@gmail.com>
#08/07/2023
#CS50 Introduction to Programming with Python
#Unit test : twitter code : converts a user string to the same string without vowels
#-------------------------------------------------
def main():
    user_str=input("Input:")
    print(shorten(user_str))


def shorten(word):
    for s in word:
        if s.lower() == "a" or s.lower() == "e" or s.lower() == "i" or s.lower() == "o" or s.lower() == "u":
            word = word.replace(s,"")
        while "  " in word: #remove double spaces in strings like "This is a code"
            word = word.replace("  "," ")
    return word


if __name__ == "__main__":
    main()