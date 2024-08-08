"""Module representing the Contact Details page object."""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework25.pages.base_page import BasePage


class ContactDetailsPage(BasePage):
    """
    Represents the Contact Details page of the web application.

    Provides methods to interact with contact details, including:
        - Navigating to edit contact page
        - Deleting a contact
        - Returning to the contact list
    """

    def __init__(self, driver):
        """
        Initializes ContactDetailsPage with driver and locators.

        Args:
            driver (webdriver): WebDriver instance.
        """
        super().__init__(
            driver, "https://thinking-tester-contact-list.herokuapp.com/"
                    "contactDetails")
        self.edit_contact_button = (By.ID, 'edit-contact')
        self.delete_contact_button = (By.ID, 'delete')
        self.return_button = (By.ID, 'return')

    def go_to_edit_contact_page(self):
        """Navigates to the Edit Contact page by clicking
         the "Edit Contact" button."""
        self.find_element(self.edit_contact_button).click()

    def delete_contact(self, driver):
        """
        Deletes the contact.

        Clicks the "Delete" button and accepts the confirmation alert.

        Args:
            driver (webdriver): WebDriver instance (needed for alert handling).
        """
        self.find_element(self.delete_contact_button).click()
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.accept()

    def return_to_contact_list(self):
        """Navigates back to the Contact List page by clicking
         the "Return" button."""
        self.find_element(self.return_button).click()
