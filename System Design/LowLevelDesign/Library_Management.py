import enum

class BookStatus(enum):
    AVAILABLE = 1
    BORROWED = 2
    RESERVED = 3

class Book:
    def __init__(self, title, ISBN, author, subject):
        self. titile = title
        self.ISBN = ISBN
        self.author = author
        self.subject = subject

class BookItem(Book):
    def __init__(self, title, ISBN, author, subject, barcode, status):
        super().__init__(title, ISBN, author, subject)
        self.barcode = barcode
        self.status = status

class User:
    def __init__(self, user_id, name, email):
        self.user_id =user_id
        self.name = name
        self.email = email

class Student(User):
    def __init__(self, user_id, name,email):
        super().__init__(user_id, name, email)
        self.borrowed_books = []

    def borrow_book(self, book_item, borrow_record):
        if book_item.status == BookStatus.AVAILABLE:
            book_item.status = BookStatus.BORROWED
            self.borrowed_books.append(book_item)
        else:
            print("Not Available")

class Librarian(User):
    def __init__(self, user_id, name, email):
        super().__init(user_id, name, email)
    
    def add_book(self, book_item):
        self.book_items[book_item.barcode] = book_item
        self.catalog.add_book_item(book_item)
    
    def remove_book(self, book_item):
        book_item = self.book_items.pop(book_item)

class Catalog:
    def __init__(self):
        self.title_map = {}
    
    def add_book(self, book_item):
        self.title_map.setdefault(book_item.title, []).append(book_item)

    def remove_book(self, book_item):
        if book_item in self.title_map:
            self.title_map[book_item.title].remove(book_item)
    