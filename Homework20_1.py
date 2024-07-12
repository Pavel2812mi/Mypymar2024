"""Тестирование модуля Библиотека"""


import unittest
from Homework11_1 import Book, Reader


class TestLibrary(unittest.TestCase):
    """Класс для тестирования работы библиотеки"""

    def setUp(self):
        """Настраиваем данные для тестов"""
        self.book1 = Book("Война миров", "Уэллс", 290, True, False)
        self.book2 = Book("Машина времени", "Уэллс", 314, True, False)
        self.reader1 = Reader("Иван Иванов")
        self.reader2 = Reader("Сергей Петров")

    def test_reserve_book(self):
        """Тест бронирования книги"""
        self.reader1.reserve_book(self.book1)
        self.assertTrue(self.book1.is_reserved())
        self.assertIn(self.book1, self.reader1.resereved_books)

    def test_take_book(self):
        """Тест взятия книги"""
        self.reader1.take_book(self.book1)
        self.assertTrue(self.book1.is_taken())
        self.assertIn(self.book1, self.reader1.taken_books)

    def test_reserve_already_reserved_book_by_different_reader(self):
        """Тест бронирования уже забронированной книги другим читателем"""
        self.reader1.reserve_book(self.book1)
        self.reader2.reserve_book(self.book1)
        self.assertNotIn(self.book1, self.reader2.resereved_books)

    def test_take_already_reserved_book_by_different_reader(self):
        """Тест попытки взять забронированную другим читателем книгу"""
        self.reader1.reserve_book(self.book1)
        self.reader2.take_book(self.book1)
        self.assertNotIn(self.book1, self.reader2.taken_books)

    def test_take_reserved_book_by_same_reader(self):
        """Тест взятия забронированной книги тем же читателем"""
        self.reader1.reserve_book(self.book1)
        self.reader1.take_book(self.book1)
        self.assertTrue(self.book1.is_taken())
        self.assertFalse(self.book1.is_reserved())
        self.assertIn(self.book1, self.reader1.taken_books)
        self.assertNotIn(self.book1, self.reader1.resereved_books)

    def test_take_already_taken_book_by_different_reader(self):
        """Тест взятия уже взятой книги"""
        self.reader1.take_book(self.book1)
        self.reader2.take_book(self.book1)
        self.assertNotIn(self.book1, self.reader2.taken_books)

    def test_return_taken_book(self):
        """Тест возврата взятой книги"""
        self.reader1.take_book(self.book1)
        self.reader1.return_book(self.book1)
        self.assertFalse(self.book1.is_taken())
        self.assertNotIn(self.book1, self.reader1.taken_books)

    def test_return_reserved_book(self):
        """Тест возврата зарезервированной книги"""
        self.reader1.reserve_book(self.book1)
        self.reader1.return_book(self.book1)
        self.assertTrue(self.book1.is_reserved())
        self.assertIn(self.book1, self.reader1.resereved_books)

    def test_return_not_taken_book(self):
        """Тест возврата книги читателем, который ее не брал"""
        self.reader1.take_book(self.book1)
        self.reader2.return_book(self.book1)
        self.assertTrue(self.book1.is_taken())
        self.assertIn(self.book1, self.reader1.taken_books)


if __name__ == '__main__':
    unittest.main()
