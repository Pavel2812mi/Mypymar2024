*** Settings ***
Library    bank_deposit_keywords.py
Library    BuiltIn
Library    OperatingSystem
Library    DateTime
Suite Setup    Setup Logging

*** Variables ***
${LOG_FILE}    ${CURDIR}${/}bank_deposit_robot_log_folder${/}bank_deposit_robot.log

*** Keywords ***
Setup Logging
    Create Directory    ${CURDIR}${/}bank_deposit_robot_log_folder
    Create File    ${LOG_FILE}
    Set Log Level    INFO

Get Current Timestamp
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
    [Return]    ${timestamp}


* Test Cases *
Create Deposit
    ${bank}=  Create Bank  Pavel_Danilov  ${True}
    Should Be True  ${bank.is_registred}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Create bank client: ${bank.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    ${result}=  Create Deposit  ${bank}  deposit_name=Deposit_1  initial_deposit_amount=1000  deposit_term=1  percentage_per_annum=10
    Should Be Equal As Strings  ${result}  You have successfully created a deposit Deposit_1
    Should Be True  ${bank.deposits}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Create deposit for bank client: ${bank.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}

Withdraw Deposit
    ${bank}=  Create Bank  Pavel_Danilov  ${True}
    Create Deposit  ${bank}  deposit_name=Deposit_1  initial_deposit_amount=1000  deposit_term=1  percentage_per_annum=10
    ${result}=  Withdraw Deposit  ${bank}  deposit_name=Deposit_1
    Should Be Equal As Strings  ${result}  Итоговая сумма депозита Deposit_1: 1104.71
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Withdraw Deposit1 by bank client: ${bank.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}

Withdraw Nonexistent Deposit
    ${bank}=  Create Bank  Pavel_Danilov  ${True}
    ${result}=  Withdraw Deposit  ${bank}  deposit_name=Nonexistent_Deposit
    Should Be Equal As Strings  ${result}  Депозит с именем Nonexistent_Deposit не найден.
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Withdraw nonexistent deposit by bank client: ${bank.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}

Create Deposit For Unregistered Client
    ${bank}=  Create Bank  Anton_Danilov  ${False}
    Should Not Be True  ${bank.is_registred}
    ${result}=  Create Deposit  ${bank}  deposit_name=Deposit_2  initial_deposit_amount=1000  deposit_term=1  percentage_per_annum=10
    Should Be Equal As Strings  ${result}  Sorry, you need to be a client of the bank to create a deposit
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Create deposit for unregistered Client: ${bank.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}
