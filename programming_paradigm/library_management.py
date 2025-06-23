
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    def is_available(self):
        return not self.__is_checked_out
    def checked_out(self):
        self.__is_checked_out = True
    def return_book(self):
        self.__is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self,title):
        for bk in self._books :
            if bk.title == title:
                bk.checked_out()
    def return_book(self, title):
        for bk in self._books :
            if bk.title == title:
                bk.return_book()
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"Title: {book.title}, Author: {book.author}")
        #return available_books