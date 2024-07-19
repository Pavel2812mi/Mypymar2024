"""Библиотека"""


from typing import List
from loguru import logger


class Book:
    """A class to represent all available books in the library"""
    reserved_books: List[str] = []
    taken_books: List[str] = []

    def __init__(self, name, author, number_of_pages, ISBN, reserved):
        self.name = name
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved = reserved

    def is_reserved(self):
        """checks if the book is reserved"""
        return self in Book.reserved_books

    def is_taken(self):
        """checks if the book is taken"""
        return self in Book.taken_books


book1 = Book("War_of_the_worlds", "Wells", 290, True, "False")
book2 = Book("Time_machine", "Wells", 314, True, "False")
book3 = Book("Island of doctor Morrow", "Wells", 325, True, "False")


class Reader:
    """A class to represent all library readers"""

    def __init__(self, name):
        self.name = name
        self.resereved_books = []
        self.taken_books = []

    def reserve_book(self, book):
        """Method for book reservation"""
        if book.is_reserved():
            logger.warning(f"{self.name}: Sorry, {book.name}"
                           f" is already reserved")
        elif book.is_taken():
            logger.warning(f"{self.name}: Sorry, {book.name} is already taken")
        else:
            book.reserved = True
            book.reserved_books.append(book)
            self.resereved_books.append(book)
            logger.info(f"{self.name}: Successfully reserved {book.name}")

    def take_book(self, book):
        """Method for book taking"""
        if book.is_reserved() and book in self.resereved_books:
            book.reserved = False
            book.taken_books.append(book)
            self.taken_books.append(book)
            book.reserved_books.remove(book)
            self.resereved_books.remove(book)
            logger.info(f"{self.name}: Successfully taken {book.name}")
        elif book.is_reserved():
            logger.warning(f"{self.name}: Sorry, {book.name}"
                           f" is already reserved")
        elif book.is_taken():
            logger.warning(f"{self.name}: Sorry, {book.name} is already taken")
        else:
            book.reserved = False
            book.taken_books.append(book)
            self.taken_books.append(book)
            logger.info(f"{self.name}: Successfully taken {book.name}")

    def return_book(self, book):
        """Method for book returning"""
        if book in self.taken_books:
            self.taken_books.remove(book)
            book.taken_books.remove(book)
            logger.info(f"{self.name}: Successfully returned {book.name}")
        else:
            logger.warning(f"{self.name}: Sorry, "
                           f"but you do not have {book.name}")


reader1 = Reader("Ivan Ivanov")
reader2 = Reader("Sergei Petrov")

reader1.reserve_book(book1)
reader2.take_book(book1)
reader1.take_book(book1)
reader2.return_book(book1)
reader1.return_book(book1)
