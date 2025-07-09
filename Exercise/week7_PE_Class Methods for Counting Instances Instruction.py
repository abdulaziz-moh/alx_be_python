class Book:
    total_books = 0
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages
        Book.total_books += 1
    @classmethod
    def display_total_books(cls):
        print(f"Their are {cls.total_books} books created in the library")

b1 = Book("good","az",200)
b2 = Book("bad","az",200)
b3 = Book("middle","az",200)
Book.display_total_books()