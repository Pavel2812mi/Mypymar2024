"""Банковский вклад"""


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
            print(f"You have successfully created "
                  f"a deposit {deposit_name}")
        else:
            print("Sorry, you need to be a client of the bank "
                  "to create a deposit")

    def withdraw_deposit(self, deposit_name):
        """Возвращает депозит для клиента."""
        deposit = self.deposits.get(deposit_name)
        if deposit:
            end_deposit_amount = int(deposit.initial_deposit_amount
                                     * (1 + deposit.percentage_per_annum / 100)
                                     ** deposit.deposit_term)
            print(f"Итоговая сумма депозита "
                  f"{deposit_name}: {end_deposit_amount}")
        else:
            print(f"Депозит с именем {deposit_name} не найден.")


client1 = Bank("Pavel_Danilov", True)
client1.create_deposit("Deposit_1", 1000, 2, 10)
client1.withdraw_deposit("Deposit_1")
