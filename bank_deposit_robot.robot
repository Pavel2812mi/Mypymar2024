*** Settings ***
Library    bank_deposit_keywords.py
Library    BuiltIn


* Test Cases *
Create Deposit
    ${bank}=  Create Bank  Pavel_Danilov  ${True}
    Should Be True  ${bank.is_registred}
    ${result}=  Create Deposit  ${bank}  deposit_name=Deposit_1  initial_deposit_amount=1000  deposit_term=1  percentage_per_annum=10
    Should Be Equal As Strings  ${result}  You have successfully created a deposit Deposit_1
    Should Be True  ${bank.deposits}

Withdraw Deposit
    ${bank}=  Create Bank  Pavel_Danilov  ${True}
    Create Deposit  ${bank}  deposit_name=Deposit_1  initial_deposit_amount=1000  deposit_term=1  percentage_per_annum=10
    ${result}=  Withdraw Deposit  ${bank}  deposit_name=Deposit_1
    Should Be Equal As Strings  ${result}  Итоговая сумма депозита Deposit_1: 1104.71

Withdraw Nonexistent Deposit
    ${bank}=  Create Bank  Pavel_Danilov  ${True}
    ${result}=  Withdraw Deposit  ${bank}  deposit_name=Nonexistent_Deposit
    Should Be Equal As Strings  ${result}  Депозит с именем Nonexistent_Deposit не найден.

Create Deposit For Unregistered Client
    ${bank}=  Create Bank  Pavel_Danilov  ${False}
    Should Not Be True  ${bank.is_registred}
    ${result}=  Create Deposit  ${bank}  deposit_name=Deposit_2  initial_deposit_amount=1000  deposit_term=1  percentage_per_annum=10
    Should Be Equal As Strings  ${result}  Sorry, you need to be a client of the bank to create a deposit
