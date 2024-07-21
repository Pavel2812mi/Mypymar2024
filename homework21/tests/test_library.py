"""Тестирование библиотеки (pytest)"""

import os
from loguru import logger
from ..source.Homework11_1 import Reader, Book


log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                       "library_log_folder")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "library_test.log")
logger.remove()
logger.add(log_file, level="DEBUG", enqueue=True)


def test_book_reservation():
    """
    Test-case for the reservation of a book.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader2 = Reader("Sergei Petrov")

    logger.info(f"Starting a test for reserving a book {book1.name}")
    reader2.reserve_book(book1)
    assert book1.is_reserved(), \
        (logger.error(f"book {book1.name} is not marked as reserved"))
    assert book1 in Book.reserved_books, \
        logger.error(f"book {book1.name} is not in reserved books list")
    assert book1 in reader2.resereved_books, \
        logger.error(f"book {book1.name}"
                     f" is not in {reader2.name} reserved books list")
    logger.info(f"Test for reserving a book {book1.name} successfully passed")


def test_book_taking():
    """
    Test-case for the taking of a book.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting a test for taking a book {book1.name}")
    reader1.take_book(book1)
    assert book1.is_taken(), \
        logger.error(f"book {book1.name} is not marked as taken")
    assert book1 in Book.taken_books, \
        logger.error(f"book {book1.name} is not in taken books list")
    assert book1 in reader1.taken_books, \
        logger.error(f"book {book1.name} "
                     f"is not in {reader1.name} taken books list")
    logger.info(f"Test for taking a book {book1.name} successfully passed")


def test_taken_book_return():
    """
    Test-case for the returning of a taken book.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting a test for returning book {book1.name}")
    reader1.take_book(book1)
    reader1.return_book(book1)
    assert book1 not in reader1.taken_books, \
        logger.error(f"book {book1.name} "
                     f"remains in {reader1.name} taken books list")
    assert book1 not in Book.taken_books, \
        logger.error(f"book {book1.name} remains in taken books list")
    logger.info(f"Test for returning a book {book1.name} successfully passed")


def test_non_taken_book_return():
    """
    Test-case for the returning of a non-taken book.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting a test for returning a non-taken book {book1.name}")
    try:
        reader1.return_book(book1)
    except RuntimeError as e:
        logger.error(f"Expected exception: {e}")
    logger.info(f"Test for returning a non-taken book"
                f" {book1.name} failed as expected")


def test_reserved_book_taking_by_another_reader():
    """
    Test-case for the taking of a reserved book by another reader.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")
    reader2 = Reader("Sergei Petrov")

    logger.info(f"Starting a test for taking of a reserved book {book1.name}"
                f" by another reader")
    reader1.reserve_book(book1)
    try:
        reader2.take_book(book1)
    except RuntimeError as e:
        logger.error(f"Expected exception: {e}")
    assert book1 in Book.reserved_books, \
        logger.error(f"book {book1.name} is not in reserved books list")
    assert book1 in reader1.resereved_books, \
        logger.error(f"book {book1.name} "
                     f"is not in {reader1.name} reserved books list")
    logger.info(f"Test for taking a reserved book"
                f" {book1.name} failed as expected")


def test_reserved_book_taking_by_the_same_reader():
    """
    Test-case for the taking of a reserved book by the same reader.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting a test for taking of a reserved book"
                f" {book1.name} by the same reader")
    reader1.reserve_book(book1)
    reader1.take_book(book1)
    assert not book1.is_reserved(), \
        logger.error(f"book {book1.name} is marked as reserved")
    assert book1.is_taken(), \
        logger.error(f"book {book1.name} is not marked as taken")
    assert book1 not in Book.reserved_books, \
        logger.error(f"book {book1.name} remains in reserved books list")
    assert book1 not in reader1.resereved_books, \
        logger.error(f"book {book1.name} "
                     f"remains in {reader1.name} reserved books list")
    assert book1 in Book.taken_books, \
        logger.error(f"book {book1.name} is not in taken books list")
    assert book1 in reader1.taken_books, \
        logger.error(f"book {book1.name} "
                     f"is not in {reader1.name} taken books list")
    logger.info(f"Test for reserved book {book1.name}"
                f" taking by the same reader successful")


def test_taken_book_reservation():
    """
    Test-case for the reservation of a taken book.
    """

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")
    reader2 = Reader("Sergei Petrov")

    logger.info("Starting a test for reservation of a taken book")
    reader1.take_book(book1)
    try:
        reader2.reserve_book(book1)
    except RuntimeError as e:
        logger.error(f"Expected exception: {e}")
    assert book1 in Book.taken_books, \
        logger.error(f"book {book1.name} is not in taken books list")
    assert book1 in reader1.taken_books, \
        logger.error(f"book {book1.name}"
                     f" is not in {reader1.name} taken books list")
    logger.info(f"Test for reservation of a taken book"
                f" {book1.name} failed as expected")
