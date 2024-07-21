"""Тестирование банковского вклада (pytest)"""

import os
from loguru import logger
from ..source.Homework11_2 import Bank


log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                       "bank_deposit_log_folder")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "bank_deposit_log")
logger.remove()
logger.add(log_file, level="DEBUG", enqueue=True)


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
        logger.info("Test for deposit creation"
                    " for unregistered client successfully passed")

    def test_withdraw_deposit(self):
        """Test-case for deposit withdraw."""
        logger.info("Starting a test for deposit withdraw")
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert (self.client.withdraw_deposit("Deposit_1") ==
                "Итоговая сумма депозита Deposit_1: 1104.71"), \
            logger.error("Incorrect final deposit amount calculation")
        logger.info("Test for deposit withdraw successfully passed")

    def test_withdraw_nonexistent_deposit(self):
        """Test-case for nonexistent deposit withdraw."""
        logger.info("Starting a test for withdraw of a nonexistent deposit")
        assert (self.client.withdraw_deposit("Nonexistent_Deposit") ==
                "Депозит с именем Nonexistent_Deposit не найден."), \
            logger.error("Expected deposit withdrawal to"
                         " fail with 'Deposit not found' error,"
                         " but received different response.")
        logger.info("Test for withdraw of a nonexistent deposit"
                    " successfully passed")
