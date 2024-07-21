"""Банковский вклад"""


from loguru import logger


class Deposit:
    """A class to represent all created deposits"""
    def __init__(self, name, initial_deposit_amount,
                 deposit_term, percentage_per_annum):
        self.name = name
        self.initial_deposit_amount = initial_deposit_amount
        self.deposit_term = deposit_term
        self.percentage_per_annum = percentage_per_annum


class Bank:
    """A class to represent all available operations
     for bank clients"""
    def __init__(self, name, is_registred):
        self.name = name
        self.is_registred = is_registred
        self.deposits = {}

    def create_deposit(self, deposit_name, initial_deposit_amount,
                       deposit_term, percentage_per_annum):
        """Создает депозит для клиента."""
        if self.is_registred is True:
            deposit1 = Deposit(deposit_name, initial_deposit_amount,
                               deposit_term, percentage_per_annum)
            self.deposits[deposit_name] = deposit1
            logger.info(f"You have successfully "
                        f"created a deposit {deposit_name}")
        else:
            logger.warning("Sorry, you need to be a client"
                         " of the bank to create a deposit")

    def withdraw_deposit(self, deposit_name):
        """Возвращает депозит для клиента."""
        deposit = self.deposits.get(deposit_name)
        if deposit:
            monthly_interest = deposit.percentage_per_annum / 12 / 100
            months = deposit.deposit_term * 12
            end_deposit_amount = (deposit.initial_deposit_amount
                                  * (1 + monthly_interest) ** months)
            return (f"Итоговая сумма депозита"
                    f" {deposit_name}: {end_deposit_amount:.2f}")
        return f"Депозит с именем {deposit_name} не найден."


client1 = Bank("Pavel_Danilov", True)
client1.create_deposit("Deposit_1", 1000, 1, 10)
assert (client1.withdraw_deposit("Deposit_1")
        == "Итоговая сумма депозита Deposit_1: 1104.71"), \
    "Incorrect final deposit amount calculation"
