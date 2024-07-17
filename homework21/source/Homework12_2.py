"""Конвертер валют"""


class Currency:
    """A class to represent all currencies and their rates"""
    def __init__(self, currency_name, USD_rate, EUR_rate, BYN_rate):
        self.currency_name = currency_name
        self.USD_rate = USD_rate
        self.EUR_rate = EUR_rate
        self.BYN_rate = BYN_rate


class Bank:
    """A class to represent all available operations for bank clients"""
    def __init__(self, client_name):
        self.client_name = client_name
        self.deposits = {}

    @staticmethod
    def create_currency(currency_name):
        """Factory method to create Currency objects"""
        if currency_name == "USD":
            return Currency("USD", 1, 0.929, 3.269)
        if currency_name == "EUR":
            return Currency("EUR", 1.076, 1, 3.21)
        if currency_name == "BYN":
            return Currency("BYN", 0.34, 0.31, 1)
        raise ValueError(f"Invalid currency name: {currency_name}")

    def exchange(self, source_currency, amount, target_currency="BYN"):
        """Method for exchanging currencies"""
        source_currency_obj = self.create_currency(source_currency)

        exchange_rate = getattr(source_currency_obj, f"{target_currency}_rate")
        result_amount = amount * exchange_rate
        return (f"{result_amount:.2f} "
                f"{target_currency}")


client1 = Bank("Pavel_Danilov")
assert client1.exchange("USD", 10, "EUR") == "9.29 EUR", \
    "Incorrect Currency exchange calculation"
assert client1.exchange("EUR", 10, "USD") == "10.76 USD", \
    "Incorrect Currency exchange calculation"
assert client1.exchange("USD", 10, "BYN") == "32.69 BYN", \
     "Incorrect Currency exchange calculation"
assert (client1.exchange("USD", 10) == "32.69 BYN"), \
    "Incorrect Currency exchange calculation"
