from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))


    # Initial list of available books
    print("\nAvailable books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\n--- Attempting to check out '1984' ---")
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    print("\n--- Attempting to check out 'Moby Dick' (not in library) ---")
    library.check_out_book("Moby Dick")
    print("\nAvailable books after attempting to check out 'Moby Dick':")
    library.list_available_books()

    print("\n--- Attempting to check out '1984' again (already checked out) ---")
    library.check_out_book("1984")
    print("\nAvailable books after attempting to check out '1984' again:")
    library.list_available_books()

    # Simulate returning a book
    print("\n--- Attempting to return '1984' ---")
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

    print("\n--- Attempting to return 'Moby Dick' (not in library) ---")
    library.return_book("Moby Dick")
    print("\nAvailable books after attempting to return 'Moby Dick':")
    library.list_available_books()

    print("\n--- Attempting to return 'The Great Gatsby' (not checked out) ---")
    library.return_book("The Great Gatsby")
    print("\nAvailable books after attempting to return 'The Great Gatsby':")
    library.list_available_books()


if __name__ == "__main__":
    main()