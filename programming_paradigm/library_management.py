class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """Marks the book as available if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Not checked out

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """
    Manages a collection of Book instances.
    """
    def __init__(self):
        """Initializes a new Library instance with an empty list of books."""
        self._books = [] # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: '{title}'.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: '{title}'.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Prints the titles and authors of all currently available books.
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book) # Uses the __str__ method of the Book class
                available_found = True
        if not available_found:
            print("No books currently available.")