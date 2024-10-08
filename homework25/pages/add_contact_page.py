"""Module providing page object for the Add Contact page."""


from selenium.webdriver.common.by import By
from homework25.pages.base_page import BasePage


class AddContactPage(BasePage):
    """
    Represents the Add Contact page of the web application.

    Provides methods for interacting with elements on the Add Contact page,
    such as:
        - Filling in contact details
        - Submitting the form
        - Canceling contact creation
    """

    def __init__(self, driver):
        super().__init__(
            driver,
            "https://thinking-tester-contact-list.herokuapp.com/addContact")
        self.firstname_input = (By.XPATH, '//input[@id="firstName"]')
        self.lastname_input = (By.XPATH, '//input[@id="lastName"]')
        self.submit_button = (By.XPATH, '//button[@id="submit"]')

    def add_contact(self, firstname, lastname):
        """
        Adds a new contact with the provided first and last names.

        Fills in the First Name and Last Name fields, then submits the form.

        Args:
            firstname (str): The first name of the contact.
            lastname (str): The last name of the contact.
        """
        self.find_element(self.firstname_input).send_keys(firstname)
        self.find_element(self.lastname_input).send_keys(lastname)
        self.find_element(self.submit_button).click()
