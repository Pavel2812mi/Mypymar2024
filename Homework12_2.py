"""Конвертер валют"""


class Deposit:
    """A class to represent all created deposits"""
    def __init__(self, name, initial_deposit_amount,
                 deposit_term, percentage_per_annum):
        self.name = name
        self.initial_deposit_amount = initial_deposit_amount
        self.deposit_term = deposit_term
        self.percentage_per_annum = percentage_per_annum


class Currency:
    """A class to represent all currencies and their rates"""
    def __init__(self, currency_name, USD_exchange_rate,
                 EUR_exchange_rate, BYN_exchange_rate):
        self.currency_name = currency_name
        self.USD_exchange_rate = USD_exchange_rate
        self.EUR_exchange_rate = EUR_exchange_rate
        self.BYN_exchange_rate = BYN_exchange_rate


class Bank:

    """A class to represent all available operations
     for bank clients"""
    def __init__(self, client_name, is_registred):
        self.client_name = client_name
        self.is_registred = is_registred
        self.deposits = {}
        self.currencies = {
            "USD": Currency("USD", 1, 0.929, 3.269),
            "EUR": Currency("EUR", 1.076, 1, 3.21),
            "BYN": Currency("BYN", 0.34, 0.31, 1),
        }

    def exchange_currency(self, source_currency, amount, target_currency=None):
        """Method for exchanging currencies"""

        source_currency = self.currencies.get(source_currency)
        target_currency = self.currencies.get(target_currency)

        try:
            if source_currency == target_currency:
                raise (ValueError
                       ("Source currency can't be equal Target currency"))
        except ValueError as e:
            print(f"Ошибка: {e}")
            return None

        try:
            if not source_currency:
                raise ValueError("Invalid currency provided")
        except ValueError as e:
            print(f"Ошибка: {e}")
            return None

        if target_currency is None:
            target_currency = self.currencies["BYN"]

        if target_currency.currency_name == "EUR":
            result_amount = amount * source_currency.EUR_exchange_rate
        elif target_currency.currency_name == "USD":
            result_amount = amount * source_currency.USD_exchange_rate
        elif target_currency.currency_name == "BYN":
            result_amount = amount*source_currency.BYN_exchange_rate
        return (f"Currency exchange succesful."
                f" You received {result_amount:.2f}"
                f" {target_currency.currency_name}")

    def create_deposit(self, deposit_name, initial_deposit_amount,
                       deposit_term, percentage_per_annum):
        """Method for deposit creation"""
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
        """Method for deposit withdraw"""
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

assert (client1.exchange_currency("USD", 10, "EUR")
        == "Currency exchange succesful. You received 9.29 EUR"), \
    "Incorrect Currency exchange calculation"
assert (client1.exchange_currency("EUR", 10, "USD")
        == "Currency exchange succesful. You received 10.76 USD"), \
    "Incorrect Currency exchange calculation"
assert (client1.exchange_currency("USD", 10, "BYN")
        == "Currency exchange succesful. You received 32.69 BYN"), \
    "Incorrect Currency exchange calculation"
assert (client1.exchange_currency("USD", 10)
        == "Currency exchange succesful. You received 32.69 BYN"), \
    "Incorrect Currency exchange calculation"
