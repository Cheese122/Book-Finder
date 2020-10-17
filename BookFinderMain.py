import isbnlib
import webbrowser
import random


def lookup_ISBN(book_isbn):
    if isbnlib.is_isbn13(book_isbn):
        trimmed_id = isbnlib.canonical(book_isbn)
        webbrowser.open(f"https://isbnsearch.org/isbn/{trimmed_id}")
    else:
        if isbnlib.is_isbn10(book_isbn):
            trimmed_id_isbn10 = isbnlib.canonical(book_isbn)
            webbrowser.open(f"https://isbnsearch.org/isbn/{trimmed_id_isbn10}")
        else:
            print("Invalid input. Please check to see if it is in either ISBN13 or ISBN10.")


def randomBook_lookup():
    while True:
        random_id = random.randint(1000000000000, 9999999999999)
        random_id = str(random_id)
        if isbnlib.is_isbn13(random_id):
            print("Book found! {}".format(random_id))
            webbrowser.open(f"https://isbnsearch.org/isbn/{random_id}")
            return
        else:
            print(f"No book found on ISBN13 {random_id}. Looping.")


while True:
    print("\n")
    print("1) Lookup a ISBN (International Standard Book Number)")
    print("2) Get a random book by ID")
    choice = input("Please make a selection:\n")
    if choice == "1":
        isbn_id = input("Please input your ISBN:\n")
        lookup_ISBN(isbn_id)


    elif choice == "2":
        randomBook_lookup()

    else:
        # print("Invalid input. This terminal will close.")  Why close? Was this an assignment with oddly specific instructions?
        print("Invalid input. Please make sure you've inputted a proper ISBN10 or ISBN13.")


