# This is the main file to start your project
# You may add any additional modules and other files you wish
class books:

    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
        
    def return_book(self):
        self.is_available = True



class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, title ,author):
        book = Book(title, author)
        self.book.appednd(book)
        return f'Book {title} by {author} added'

    def display(self):
        for book in self.books:
            if book.is_available: #nie tak
                print(book)


    def borrow(self):
        for book in self.books:
            if book.title == title and book.is_available: