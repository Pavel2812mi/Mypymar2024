"""Тестирование банковского вклада (pytest)"""

import os
from loguru import logger
from ..source.Homework11_2 import Bank


def setup_logging(test_name, log_level="INFO"):
    """
    Logger setup.
    """
    logger.remove()
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{test_name}.log")
    logger.add(log_file, level=log_level, enqueue=True)


class TestBank:
    """Class for bank deposit testing"""

    def setup_method(self, method):
        """Setting up logging """
        self.client = Bank("Pavel_Danilov", True)
        setup_logging(method.__name__)

    def test_create_deposit(self):
        """Test the creation of the deposit."""
        logger.info("Starting test_create_deposit")
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert "Deposit_1" in self.client.deposits, \
            logger.error("The created deposit "
                         "was not added to the list of client deposits.")
        logger.info("test_create_deposit successful")

    def test_create_deposit_as_unregistered_client(self):
        """Test the creation of the deposit for unregistered client."""
        setup_logging("test_create_deposit_as_unregistered_client")
        logger.info("Starting test_create_deposit_as_unregistered_client")
        self.client.is_registred = False
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert "Deposit_1" not in self.client.deposits, \
            logger.error("Deposit was created by the unregistered client")
        logger.info("test_create_deposit_unregistered successful")

    def test_withdraw_deposit(self):
        """Test deposit withdraw."""
        setup_logging("test_withdraw_deposit")
        logger.info("Starting test_withdraw_deposit")
        self.client.create_deposit("Deposit_1", 1000, 1, 10)
        assert (self.client.withdraw_deposit("Deposit_1") ==
                "Итоговая сумма депозита Deposit_1: 1104.71"), \
            logger.error("Incorrect final deposit amount calculation")
        logger.info("test_withdraw_deposit successful")

    def test_withdraw_nonexistent_deposit(self):
        """Test nonexistent deposit withdraw."""
        setup_logging("test_withdraw_nonexistent_deposit")
        logger.info("Starting test_withdraw_nonexistent_deposit")
        assert (self.client.withdraw_deposit("Nonexistent_Deposit") ==
                "Депозит с именем Nonexistent_Deposit не найден."), \
            logger.error("Expected deposit withdrawal to"
                         " fail with 'Deposit not found' error,"
                         " but received different response.")
        logger.info("test_withdraw_nonexistent_deposit successful")
