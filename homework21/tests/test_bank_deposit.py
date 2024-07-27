"""Тестирование банковского вклада (pytest)"""

import logging
from homework21.source.Homework11_2 import Bank
from homework21.tests.logger_config import setup_logging

logger = setup_logging("bank_deposit_test.log", log_level=logging.INFO)


class TestBank:
    """Class for bank deposit testing"""

    def setup_method(self):
        """Setting up the client for testing"""
        self.client = Bank("Pavel_Danilov", True)

    def test_create_deposit(self):
        """Test-case for the creation of the deposit."""
        logger.info("Starting a test for deposit creation")
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert "Deposit_1" in self.client.deposits, \
            logger.error("The created deposit "
                         "was not added to the list of client deposits.")
        if "Deposit_1" in self.client.deposits:
            logger.info("Test for deposit creation successfully passed")

    def test_create_deposit_for_unregistered_client(self):
        """Test-case for the creation of the deposit
         for unregistered client."""
        logger.info("Starting a test for deposit creation"
                    " for unregistered client")
        self.client.is_registred = False
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert "Deposit_1" not in self.client.deposits, \
            logger.error("Deposit was created by the unregistered client")
        if "Deposit_1" not in self.client.deposits:
            logger.info("Test for deposit creation"
                        " for unregistered client successfully passed")

    def test_withdraw_deposit(self):
        """Test-case for deposit withdraw."""
        logger.info("Starting a test for deposit withdraw")
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert (self.client.withdraw_deposit("Deposit_1") ==
                "Итоговая сумма депозита Deposit_1: 1104.71"), \
            logger.error("Incorrect final deposit amount calculation")
        if (self.client.withdraw_deposit("Deposit_1")
                == "Итоговая сумма депозита Deposit_1: 1104.71"):
            logger.info("Test for deposit withdraw successfully passed")

    def test_withdraw_nonexistent_deposit(self):
        """Test-case for nonexistent deposit withdraw."""
        logger.info("Starting a test for withdraw of a nonexistent deposit")
        assert (self.client.withdraw_deposit("Nonexistent_Deposit") ==
                "Депозит с именем Nonexistent_Deposit не найден."), \
            logger.error("Expected deposit withdrawal to"
                         " fail with 'Deposit not found' error,"
                         " but received different response.")
        if (self.client.withdraw_deposit("Nonexistent_Deposit")
                == "Депозит с именем Nonexistent_Deposit не найден."):
            logger.info("Test for withdraw of a nonexistent deposit"
                        " successfully passed")
