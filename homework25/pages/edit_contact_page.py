"""Module representing the Edit Contact page object."""


from selenium.webdriver.common.by import By
from homework25.pages.base_page import BasePage


class EditContactPage(BasePage):
    """
    Represents the Edit Contact page of the web application.

    Provides methods for modifying existing contact details.
    """
    def __init__(self, driver):
        """
        Initializes EditContactPage with driver and locators.

        Args:
            driver (webdriver): WebDriver instance.
        """
        super().__init__(
            driver,
            "https://thinking-tester-contact-list.herokuapp.com/editContact")
        self.firstname_input = (By.XPATH, '//input[@id="firstName"]')
        self.lastname_input = (By.XPATH, '//input[@id="lastName"]')
        self.submit_button = (By.XPATH, '//button[@id="submit"]')

    def edit_contact(self, firstname, lastname):
        """
        Edits the contact's first and last names and submits the changes.

        Args:
            firstname (str): The new first name of the contact.
            lastname (str): The new last name of the contact.
        """
        self.find_element(self.firstname_input).send_keys(firstname)
        self.find_element(self.lastname_input).send_keys(lastname)
        self.find_element(self.submit_button).click()
