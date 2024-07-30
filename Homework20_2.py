"""Тестирование модуля Банковский вклад"""

import unittest
from homework21.source.Homework11_2 import Bank


class TestBankDeposit(unittest.TestCase):
    """Класс для тестирования работы банковского вклада"""

    def setUp(self):
        """Настраиваем данные для тестов"""
        self.client1 = Bank("Pavel_Danilov", True)
        self.client2 = Bank("Ivan_Ivanov", False)

    def test_create_deposit_registered_client(self):
        """Тест создания депозита для зарегистрированного клиента"""
        deposit_name = "Deposit_1"
        initial_amount = 1000
        term = 1
        percentage = 10

        (self.client1.create_deposit
         (deposit_name, initial_amount, term, percentage))

        self.assertIn(deposit_name, self.client1.deposits)
        deposit = self.client1.deposits[deposit_name]
        self.assertEqual(deposit.name, deposit_name)
        self.assertEqual(deposit.initial_deposit_amount, initial_amount)
        self.assertEqual(deposit.deposit_term, term)
        self.assertEqual(deposit.percentage_per_annum, percentage)

    def test_create_deposit_unregistered_client(self):
        """Тест создания депозита для незарегистрированного клиента"""
        deposit_name = "Deposit_1"
        self.client2.create_deposit(deposit_name, 1000, 1, 10)
        self.assertNotIn(deposit_name, self.client2.deposits)

    def test_withdraw_deposit_existing_deposit(self):
        """Тест возврата существующего депозита"""
        deposit_name = "Deposit_1"
        self.client1.create_deposit(deposit_name, 1000, 1, 10)
        result = self.client1.withdraw_deposit(deposit_name)
        self.assertEqual(result, "Итоговая сумма депозита Deposit_1: 1104.71")

    def test_withdraw_deposit_nonexistent_deposit(self):
        """Тест возврата несуществующего депозита"""
        result = (self.client1.withdraw_deposit
                  ("Nonexistent_Deposit"))
        (self.assertEqual
         (result, "Депозит с именем Nonexistent_Deposit не найден."))


if __name__ == '__main__':
    unittest.main()
