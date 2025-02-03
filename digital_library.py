import json
import os

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
            availability = bool(input("* Is this book available? (True/False): ")) #Need to be modified
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
    year_search = int(input("* Enter publication year: ")) #i didn't make any check. How to do it in easiest way?

    books_found = 0

    if not author_search and not year_search: #when both are empty
        print(f"You didn't gave any valid data. You were returned to the menu.")
    elif not author_search or not year_search: #when one of the inputs is not empty
        for book in sample_lib:
            author = book["author"].lower()
            if author_search == author:
                books_found += 1
                print(f"The book {book['title']} was successfully found.")
            elif year_search == book["year"]:
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
    #it works, but I have an error with "json_file". I think it should be another way to write the same functionality.
    try:
        # Check if file exists first
        with open(books_library, "r", encoding="utf-8") as json_file:
            file_overwrite = input(
                f"* The file {books_library} already exists. Would you like to overwrite it? (y/n): ")
            if file_overwrite.lower() == "y":
                with open(books_library, "w", encoding="utf-8") as json_file:
                    json.dump(sample_lib, json_file, indent="4")
                    print("The file was successfully overwritten. Have a nice day!.")
            else:
                print("Have a nice day!")

    except FileNotFoundError:
        with open(books_library, "w", encoding="utf-8") as json_file:
            json.dump(sample_lib, json_file, indent="4")
            print("The books were successfully saved. Have a nice day!")

    print("\n_______________________________________\n")

def main():
    while True:
        menu_option = input("""Menu:\n1. Add a book manually\n2. Search for books\n3. Update book availability\n4. List all book titles\n5. Load books from a JSON file\n6. Save and exit\nEnter the option you would like to choose: """)
        try:
            if menu_option == "1":
                add_book()
                continue
            elif menu_option == "2":
                find_book()
                continue
            elif menu_option == "3":
                update_availability()
                continue
            elif menu_option == "4":
                get_all_titles()
                continue
            elif menu_option == "5":
                load_books_from_json()
                continue
            elif menu_option == "6":
                save_library_to_json()
                break
            else:
                print("\nYou entered an invalid option. Please try again.\n")
                continue
        except (KeyboardInterrupt, ValueError):
            print(f"\nYou entered smth wrong. Start everything again.")
            print("\n_______________________________________\n")
print("___Digital Library___")
main()