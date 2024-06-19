"""Конвертер валют"""


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

        source_currency_obj = self.currencies.get(source_currency)
        target_currency_obj = self.currencies.get(target_currency)

        if source_currency_obj is None:
            print("Error: Invalid source currency")
            return None

        if source_currency_obj == target_currency_obj:
            print("Error: Source currency cannot be equal to target currency")
            return None

        if target_currency_obj is None:
            target_currency_obj = self.currencies["BYN"]

        exchange_rate = getattr(source_currency_obj,
                                f"{target_currency_obj.currency_name}"
                                f"_exchange_rate")
        result_amount = amount * exchange_rate
        return (f"Currency exchange succesful. "
                f"You received {result_amount:.2f} "
                f"{target_currency_obj.currency_name}")


client1 = Bank("Pavel_Danilov", True)
assert ((client1.exchange_currency("USD", 10, "EUR"))
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
