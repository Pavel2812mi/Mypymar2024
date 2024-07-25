"""Library keywords"""

from robot.api.deco import keyword
from Homework11_1 import Book, Reader


@keyword
def create_book(name, author, number_of_pages, ISBN, reserved):
    """Create a new book"""
    return Book(name, author, number_of_pages,
                ISBN, reserved)


@keyword
def create_reader(name):
    """Create a new reader"""
    return Reader(name)


@keyword
def reserve_book(reader, book):
    """Reserve a book for a reader"""
    return reader.reserve_book(book)


@keyword
def take_book(reader, book):
    """Take a book from the library"""
    return reader.take_book(book)


@keyword
def return_book(reader, book):
    """Return a book to the library"""
    return reader.return_book(book)
