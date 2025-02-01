print("--- Digital Library ---")
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
    },
    {
        "title": "I don't reed the books",
        "author": "Nevidomyi",
        "year": 2025,
        "available": False
    }
]

def add_book(availability):
    while True:
        try:
            title = input("* Enter book title: ")
            author = input("* Enter book author: ")
            year = input("Enter publication year: ")
            availability = input("* Is this book available? (True/False): ") #Need to be modified
            if title and author and availability:
                sample_lib.append({"title": title, "author": author, "year": year, "availability": availability})
                print(f"The book {title} was successfully added.")
                break
            else:
                print("Please check whether all data were entered. Try it again.a")
                continue
        except KeyboardInterrupt:
            print(f"Entered Data were interrupted. Please try again.")

def find_book():
    search_book = input("* Please enter author or/and year of publication: ").lower()

    for book in sample_lib:
        print(search_book)
        if search_book == book["author"].lower() or search_book == book["author"].lower:
            print(f"Book {book['title']} was found.")
            if book['available']:
                print(f"It is available to buy.")
            else:
                print("The book is not available to buy. Sorian.")
            break
        elif search_book == book["year"] or search_book == book["year"]:
            print(f"Book {book['title']} was found.")
            if book['available']:
                print(f"It is available to buy.")
            else:
                print("The book is not available to buy. Sorian.")
            break


find_book()
# print(sample_lib)