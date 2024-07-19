"""Тестирование библиотеки (pytest)"""


from loguru import logger
from ..source.Homework11_1 import Reader, Book


def setup_logging(test_name, log_level="DEBUG"):
    """
    Logger setup.
    """
    logger.remove()
    logger.add(f"{test_name}.log", level=log_level, enqueue=True)


def test_book_reservation():
    """
    Test the reservation of a book.
    """
    setup_logging("test_book_reservation")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader2 = Reader("Sergei Petrov")

    logger.info(f"Starting test book {book1.name} reservation")
    reader2.reserve_book(book1)
    assert book1.is_reserved(), \
        (logger.error(f"book {book1.name} is not marked as reserved"))
    assert book1 in Book.reserved_books, \
        logger.error(f"book {book1.name} is not in reserved books list")
    assert book1 in reader2.resereved_books, \
        logger.error(f"book {book1.name}"
                     f" is not in {reader2.name} reserved books list")
    logger.info(f"Book {book1.name} reservation successful")


def test_book_taking():
    """
    Test the taking of a book.
    """
    setup_logging("test_book_taking")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting test book {book1.name} taking")
    reader1.take_book(book1)
    assert book1.is_taken(), \
        logger.error(f"book {book1.name} is not marked as taken")
    assert book1 in Book.taken_books, \
        logger.error(f"book {book1.name} is not in taken books list")
    assert book1 in reader1.taken_books, \
        logger.error(f"book {book1.name} "
                     f"is not in {reader1.name} taken books list")
    logger.info(f"Book {book1.name} taking successful")


def test_taken_book_return():
    """
    Test the returning of a taken book.
    """
    setup_logging("test_taken_book_return")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting test taken book {book1.name} return")
    reader1.take_book(book1)
    reader1.return_book(book1)
    assert book1 not in reader1.taken_books, \
        logger.error(f"book {book1.name} "
                     f"remains in {reader1.name} taken books list")
    assert book1 not in Book.taken_books, \
        logger.error(f"book {book1.name} remains in taken books list")
    logger.info(f"Book {book1.name} return successful")


def test_non_taken_book_return():
    """
    Test the returning of a non-taken book.
    """
    setup_logging("test_non_taken_book_return")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting test returning a non-taken book {book1.name}")
    try:
        reader1.return_book(book1)
    except RuntimeError as e:
        logger.error(f"Expected exception: {e}")
    logger.info(f"Returning a non-taken book {book1.name} failed as expected")


def test_reserved_book_taking_by_another_reader():
    """
    Test the taking of a reserved book by another reader.
    """
    setup_logging("test_reserved_book_taking_by_another_reader")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")
    reader2 = Reader("Sergei Petrov")

    logger.info(f"Starting test taking of a reserved book {book1.name}"
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
    logger.info(f"Taking a reserved book {book1.name} failed as expected")


def test_reserved_book_taking_by_the_same_reader():
    """
    Test the taking of a reserved book by the same reader.
    """
    setup_logging("test_reserved_book_taking_by_the_same_reader")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")

    logger.info(f"Starting test taking of a reserved book"
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
    logger.info(f"Reserved book {book1.name}"
                f" taking by the same reader successful")


def test_taken_book_reservation():
    """
    Test the reservation of a taken book.
    """
    setup_logging("test_taken_book_reservation")

    book1 = Book("War_of_the_worlds", "Wells", 290, True, False)
    reader1 = Reader("Ivan Ivanov")
    reader2 = Reader("Sergei Petrov")

    logger.info("Starting test reservation of a taken book")
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
    logger.info(f"Reservation of a taken book {book1.name} failed as expected")
