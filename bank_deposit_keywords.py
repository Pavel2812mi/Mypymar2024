"""Bank Deposit keywords"""

from robot.api.deco import keyword
from Homework11_2 import Bank


@keyword
def Create_Bank(name, is_registred):
    """Bank object Creation."""
    return Bank(name=name, is_registred=is_registred)


@keyword
def Create_Deposit(bank, deposit_name, initial_deposit_amount,
                   deposit_term, percentage_per_annum):
    """Client deposit creation."""
    if bank.is_registred:
        initial_deposit_amount = float(initial_deposit_amount)
        deposit_term = int(deposit_term)
        percentage_per_annum = float(percentage_per_annum)
        result = bank.create_deposit(deposit_name, initial_deposit_amount,
                                     deposit_term, percentage_per_annum)
        return result
    return "Sorry, you need to be a client of the bank to create a deposit"


@keyword
def Withdraw_Deposit(bank, deposit_name):
    """Client deposit withdraw."""
    result = bank.withdraw_deposit(deposit_name)
    return result
