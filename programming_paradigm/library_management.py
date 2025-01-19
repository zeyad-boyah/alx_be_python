class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_checked_out(self):
        return self.__is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, new_book):
        self._books.append(new_book)

    def check_out_book(self, title):
        book_found = False
        for book in self._books:
            if book.title == title:
                book.check_out()
                print(f"The book '{title}' has been checked out.")
                book_found = True
                break
        if book_found == False:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        book_found = False
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"The book '{title}' has been returned.")
                book_found = True
                break
        if book_found == False:
            print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
