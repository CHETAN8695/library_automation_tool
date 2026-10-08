# Library Automation Tool

books = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "available": True},
    {"id": 2, "title": "Data Structures", "author": "Robert Brown", "available": True},
    {"id": 3, "title": "Computer Networks", "author": "David Lee", "available": True}
]


def display_books():
    print("\n--- LIBRARY BOOKS ---")

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print("Book ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)
        print("----------------------")


def add_book():
    print("\n--- ADD BOOK ---")

    try:
        book_id = int(input("Enter book ID: "))

        for book in books:
            if book["id"] == book_id:
                print("Error: Book ID already exists.")
                return

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        if title == "" or author == "":
            print("Error: Title and author cannot be empty.")
            return

        books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        })

        print("Book added successfully.")

    except ValueError:
        print("Error: Book ID must be a number.")


def search_book():
    print("\n--- SEARCH BOOK ---")

    keyword = input("Enter book title or author: ").strip().lower()

    if keyword == "":
        print("Please enter a search keyword.")
        return

    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print("\nBook ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"])
            found = True

    if not found:
        print("No matching book found.")


def issue_book():
    print("\n--- ISSUE BOOK ---")

    try:
        book_id = int(input("Enter book ID to issue: "))

        for book in books:
            if book["id"] == book_id:

                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

                return

        print("Book not found.")

    except ValueError:
        print("Error: Book ID must be a number.")


def return_book():
    print("\n--- RETURN BOOK ---")

    try:
        book_id = int(input("Enter book ID to return: "))

        for book in books:
            if book["id"] == book_id:

                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully.")
                else:
                    print("This book was not issued.")

                return

        print("Book not found.")

    except ValueError:
        print("Error: Book ID must be a number.")


def main():
    while True:

        print("\n==============================")
        print("     LIBRARY AUTOMATION TOOL")
        print("==============================")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_books()

        elif choice == "2":
            add_book()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            print("Thank you for using Library Automation Tool.")
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()