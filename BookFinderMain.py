import time
import isbnlib
import webbrowser
import random


def LookupISBN(ID):
        if isbnlib.is_isbn13(ID):
                trimmedID = isbnlib.canonical(ID)
                webbrowser.open("https://isbnsearch.org/isbn/{}".format(trimmedID)) 
        else:
                if isbnlib.is_isbn10(ID):
                        trimmedIdISBN10 = isbnlib.canonical(ID)
                        webbrowser.open("https://isbnsearch.org/isbn/{}".format(trimmedIdISBN10))
                else: 
                        print("Invalid input. Please check to see if it is in either ISBN13 or ISBN10.")
                        input()
                        exit()



def RandomBookLookup():
        while True:
                randomID = random.randint(1000000000000, 9999999999999)
                randomID = str(randomID)
                if isbnlib.is_isbn13(randomID):
                        print("Book found! {}".format(randomID))
                        webbrowser.open("https://isbnsearch.org/isbn/{}".format(randomID))
                        return
                else:
                        print("Not no book found. Looping. {}".format(randomID))


print("1) Lookup a ISBN (International Standard Book Number)")
print("2) Get a random book by ID")
choice = input("Please make a selection\n")
if choice == "1": 
        isbnId = input("Please input your ISBN:\n")
        LookupISBN(isbnId)
        input()


elif choice == "2":
        RandomBookLookup()
        input()
        
else:
        print("Invalid input. This terminal will close.")
        input()
        exit()



