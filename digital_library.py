import json
import os.path
import time

sample_lib = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "available": True
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "available": False
    }
]

def add_book(): #1
    while True:
        try:
            title = input("* Enter book title: ")
            author = input("* Enter book author: ")
            year = int(input("Enter publication year: "))
            availability_status = int(input("* Is this book currently available? (1/0): "))
            availability = bool(availability_status)
            if title and author and availability:
                sample_lib.append({"title": title, "author": author, "year": year, "availability": availability})
                print(f"The book \"{title}\" was successfully added.")
                break
            else:
                print("Please check whether all data were entered. Try it again.a")
                continue
        except KeyboardInterrupt:
            print(f"Entered Data were interrupted. Please try again.")
    print("\n_______________________________________\n")

def find_book(): #2
    author_search = input("* Enter book author: ").lower()
    while True:
        year_search = input("* Enter publication year: ") #I didn't make any check. How to do it in easier way?
        if year_search.isdigit():
            year_search = int(year_search)
            break
        elif not year_search:
            break
        else:
            print("You entered an invalid year. Please try again.")
            continue

    books_found = 0

    if not author_search and not year_search: #when both are empty
        print(f"You didn't gave any valid data. You were returned to the menu.")
    elif not author_search or not year_search: #when one of the inputs is not empty
        for book in sample_lib:
            author = book["author"].lower()
            if author_search == author or year_search == book["year"]:
                books_found += 1
                print(f"The book {book['title']} was successfully found.")
    else: #when both inputs are not empty
        for book in sample_lib:
            author = book["author"].lower()
            if author_search == author and year_search == book["year"]:
                books_found += 1
                print(f"The book {book['title']} was successfully found.")
    if not books_found:
        print("No books were found.")
    print("\n_______________________________________\n")

def update_availability(): #3
    selected_book = input("* Enter book title: ").lower()
    books_found = 0
    for book in sample_lib:
        if book["title"].lower() == selected_book:
            print(f"The book {book['title']} by {book['author']} was successfully found.")
            availability_status = int(input("* Is this book currently available? (1/0): "))
            book["available"] = bool(availability_status)
            print(f"The availability status for \"{book['title']}\" was successfully updated to \"{book["available"]}\".")
            books_found += 1
    if books_found == 0:
        print("No books were found.")
    elif books_found >= 1:
        print(f"No more books were found.")
    print("\n_______________________________________\n")

def get_all_titles():
    print("Here is a list of all available books:")
    for idx, book in enumerate(sample_lib):
        print(f"{idx + 1}. {book['title']}")
    print("\n_______________________________________\n")

def load_books_from_json():
    books_library = input("* Please, enter the name of the file (books.json): ")
    try:
        with open(books_library) as json_file:
            books = json.load(json_file)
            for book in books:
                sample_lib.append(book)
        print("The books were successfully loaded.")
    except (json.JSONDecodeError , FileNotFoundError) as e:
        print(f"{e}. An error occurred. You were returned to the menu.")
    print("\n_______________________________________\n")

def save_library_to_json():
    books_library = input("* Please, enter the name of the file (without extension): ") + ".json"

    if os.path.isfile(books_library):
        file_overwrite = input(f"* The file {books_library} already exists. Would you like to overwrite it? (y/n): ")
        if file_overwrite.lower() != "y":
            print("You were returned to the menu.")
            return

    with open(books_library, "w") as json_file:
        json.dump(sample_lib, json_file, indent=4) # It writes the file only when program stops :(
        print("The file was successfully saved.")

    print("\n_______________________________________\n")



def main():
    options = {
        "1": ["Add a book manually", add_book],
        "2": ["Search for books", find_book],
        "3": ["Update book availability", update_availability],
        "4": ["List all book titles", get_all_titles],
        "5": ["Load books from a JSON file", load_books_from_json],
        "6": ["Save current library to JSON file", save_library_to_json],
        "7": ["Exit", exit]
    }
    while True:
        print("Menu:")
        for option, function in options.items():
            print(option + '. ' + function[0])
        else:
           menu_option = input(f"Enter the option you would like to choose (1-{option}):")
        try:
            if menu_option in options:
                try:
                    options[menu_option][1]()
                    time.sleep(2)
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif menu_option == "7":
                break
            else:
                print("Invalid option. Please try again.")
        except (KeyboardInterrupt, ValueError) as e:
            print(f"\n{e}. Entered DATA are wrong. Start everything again.")
            print("\n_______________________________________\n")

print("___Digital Library___")
main()