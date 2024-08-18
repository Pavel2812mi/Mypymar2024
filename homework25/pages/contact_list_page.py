"""Module representing the Contact List page object."""


from selenium.webdriver.common.by import By
from homework25.pages.base_page import BasePage


class ContactListPage(BasePage):
    """
    Represents the Contact List page of the web application.

    Provides methods for interacting with the list of contacts, such as:
        - Navigating to Add Contact page
        - Accessing contact details
        - Retrieving table data
    """

    def __init__(self, driver):
        """
        Initializes ContactListPage with driver and locators.

        Args:
            driver (webdriver): WebDriver instance.
        """
        super().__init__(
            driver,
            "https://thinking-tester-contact-list.herokuapp.com/contactList")
        self.add_contact_button = (By.ID, 'add-contact')
        self.contact_details = (By.CSS_SELECTOR,
                                '.contactTableBodyRow td:not([hidden])')
        self.main_content = (By.CLASS_NAME, 'main-content')
        self.contact_table = (By.CLASS_NAME, 'contactTable')

    def go_to_add_contact_page(self):
        """Navigates to the Add Contact page
         by clicking the "Add Contact" button."""
        self.find_element(self.add_contact_button).click()

    def go_to_contact_details_page(self):
        """Navigates to the Contact Details page
         by clicking on a contact row."""
        self.find_element(self.contact_details).click()

    def get_table_text(self):
        """
        Retrieves the text content of the contact table.

        Returns:
            str: The text within the contact table.
        """
        table_text = self.find_element(self.contact_table).text
        return table_text
