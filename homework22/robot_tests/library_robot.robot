*** Settings ***
Library    ../resources/library_keywords.py
Library    BuiltIn
Library    OperatingSystem
Library    DateTime
Suite Setup    Setup Logging


*** Variables ***
${LOG_FILE}    ${CURDIR}${/}..${/}robot_library_log_folder${/}library_robot.log
${NAME}      War of the worlds
${AUTHOR}         Wells
${NUMBER_OF_PAGES}      290
${ISBN}           3124123324
${RESERVED}           False


*** Keywords ***
Setup Logging
    Create Directory    ${CURDIR}${/}..${/}robot_library_log_folder
    Create File    ${LOG_FILE}
    Set Log Level    INFO

Get Current Timestamp
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d %H:%M:%S
    [Return]    ${timestamp}

* Test Cases *
Reserve Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Reserve book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Reserve Book    ${reader}    ${book}
    Should Be True  ${book.is_reserved()}
    Should Be True  ${reader.resereved_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Reserve book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}

Take Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Take Book    ${reader}    ${book}
    Should Be True  ${book.is_taken()}
    Should Be True  ${reader.taken_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}

Return Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Return book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Take Book    ${reader}    ${book}
    Return Book  ${reader}    ${book}
    Should Not Be True  ${book.is_taken()}
    Should Not Be True  ${reader.taken_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Return book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}


Reserve Already Reserved Book
    ${reader1}=  Create Reader  Ivan Ivanov
    ${reader2}=  Create Reader  Sergei Petrov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Reserve already reserved book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Reserve Book    ${reader1}    ${book}
    Reserve Book    ${reader2}    ${book}
    Should Be True  ${book.is_reserved()}
    Should Be True  ${reader1.resereved_books}
    Should Not Be True  ${reader2.resereved_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Reserve already reserved book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}


Take Already Reserved Book
    ${reader1}=  Create Reader  Ivan Ivanov
    ${reader2}=  Create Reader  Sergei Petrov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take already reserved book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Reserve Book    ${reader1}    ${book}
    Take Book    ${reader2}    ${book}
    Should Be True  ${book.is_reserved()}
    Should Be True  ${reader1.resereved_books}
    Should Not Be True  ${reader2.taken_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take already reserved book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}


Take Reserved Book By The Same Reader
    ${reader1}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take reserved book: ${book.name} by the same reader\n
    Append To File    ${LOG_FILE}    ${log_message}
    Reserve Book    ${reader1}    ${book}
    Take Book    ${reader1}    ${book}
    Should Not Be True  ${book.is_reserved()}
    Should Not Be True  ${reader1.resereved_books}
    Should Be True  ${book.is_taken()}
    Should Be True  ${reader1.taken_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take reserved book: ${book.name} by the same reader completed\n
    Append To File    ${LOG_FILE}    ${log_message}


Take Already Taken Book
    ${reader1}=  Create Reader  Ivan Ivanov
    ${reader2}=  Create Reader  Sergei Petrov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take already taken book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Take Book    ${reader1}    ${book}
    Take Book    ${reader2}    ${book}
    Should Be True  ${book.is_taken()}
    Should Be True  ${reader1.taken_books}
    Should Not Be True  ${reader2.taken_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Take already taken book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}


Return Non Taken Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  War_of_the_worlds  Wells  290  True  False
    ${timestamp}=  Get Current Timestamp
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Return non taken book: ${book.name}\n
    Append To File    ${LOG_FILE}    ${log_message}
    Return Book    ${reader}    ${book}
    Should Not Be True  ${book.is_reserved()}
    Should Not Be True  ${book.is_taken()}
    Should Not Be True  ${reader.resereved_books}
    Should Not Be True  ${reader.taken_books}
    ${log_message}=  Set Variable  ${timestamp} ${LOG_LEVEL} Return non taken book: ${book.name} completed\n
    Append To File    ${LOG_FILE}    ${log_message}



