class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"📘 '{self.title}' by {self.author} - {self.pages} pages"
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    def __del__(self):
        print()
        print(f"deleted {self.title} book for MM")

book_a = Book("Rich dad Poor dad","Robert T. Kiyosaki",200)
print(book_a)
print(repr(book_a))