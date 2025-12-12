# This is the main file to start your project
# You may add any additional modules and other files you wish
class books:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
        return self.is_available
        
    def return_book(self):
        self.is_available = True
        return self.is_available

    def retur (self):
        if self.is_available == True:
            state = "Available"
        else:
            state = "not Available"
            return f'{self.title} is {state}'

class User:

    def __init__(self, name, ):
        self.name = name 
        self.borrowed = []

    def borrowed_book(self, book):
        self.borrowed.append(book)

    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
        else:
            return f'u havent borowed this book'

    def retur (self):
        return f'{self.name} borowed {self.borrowed}'


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    
    def add_book(self, title ,author):
        new_book = books(title, author)
        self.books.append(new_book)
        print("new added")
        return new_book

    def display(self):
        for book in self.books:
            if book.is_available: #nie tak
                print(book)


    