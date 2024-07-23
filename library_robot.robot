*** Settings ***
Library    library_keywords.py
Library    BuiltIn

*** Variables ***
${NAME}      War of the worlds
${AUTHOR}         Wells
${NUMBER_OF_PAGES}      290
${ISBN}           3124123324
${RESERVED}           False


* Test Cases *
Reserve Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Reserve Book    ${reader}    ${book}
    Should Be True  ${book.is_reserved()}
    Should Be True  ${reader.resereved_books}

Take Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Take Book    ${reader}    ${book}
    Should Be True  ${book.is_taken()}
    Should Be True  ${reader.taken_books}

Return Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Take Book    ${reader}    ${book}
    Return Book  ${reader}    ${book}
    Should Not Be True  ${book.is_taken()}
    Should Not Be True  ${reader.taken_books}


Reserve Already Reserved Book
    ${reader1}=  Create Reader  Ivan Ivanov
    ${reader2}=  Create Reader  Sergei Petrov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Reserve Book    ${reader1}    ${book}
    Reserve Book    ${reader2}    ${book}
    Should Be True  ${book.is_reserved()}
    Should Be True  ${reader1.resereved_books}
    Should Not Be True  ${reader2.resereved_books}


Take Already Reserved Book
    ${reader1}=  Create Reader  Ivan Ivanov
    ${reader2}=  Create Reader  Sergei Petrov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Reserve Book    ${reader1}    ${book}
    Take Book    ${reader2}    ${book}
    Should Be True  ${book.is_reserved()}
    Should Be True  ${reader1.resereved_books}
    Should Not Be True  ${reader2.taken_books}


Take Reserved Book By The Same Reader
    ${reader1}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Reserve Book    ${reader1}    ${book}
    Take Book    ${reader1}    ${book}
    Should Not Be True  ${book.is_reserved()}
    Should Not Be True  ${reader1.resereved_books}
    Should Be True  ${book.is_taken()}
    Should Be True  ${reader1.taken_books}


Take Already Taken Book
    ${reader1}=  Create Reader  Ivan Ivanov
    ${reader2}=  Create Reader  Sergei Petrov
    ${book}=  Create Book  ${NAME}    ${AUTHOR}    ${NUMBER_OF_PAGES}  ${ISBN}    ${RESERVED}
    Take Book    ${reader1}    ${book}
    Take Book    ${reader2}    ${book}
    Should Be True  ${book.is_taken()}
    Should Be True  ${reader1.taken_books}
    Should Not Be True  ${reader2.taken_books}


Return Non Taken Book
    ${reader}=  Create Reader  Ivan Ivanov
    ${book}=  Create Book  War_of_the_worlds  Wells  290  True  False
    Return Book    ${reader}    ${book}
    Should Not Be True  ${book.is_reserved()}
    Should Not Be True  ${book.is_taken()}
    Should Not Be True  ${reader.resereved_books}
    Should Not Be True  ${reader.taken_books}



