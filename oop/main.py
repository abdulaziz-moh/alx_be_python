from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)               # Expected: 1984 by George Orwell, published in 1949
    print(repr(my_book))         # Expected: Book('1984', 'George Orwell', 1949)
    del my_book                  # Expected: Deleting 1984

if __name__ == "__main__":
    main()
