"""Module representing the Login page object."""


from selenium.webdriver.common.by import By
from homework25.pages.base_page import BasePage
from homework25.pages.contact_list_page import ContactListPage


class LoginPage(BasePage):
    """
    Represents the Login page of the web application.

    Provides methods for interacting with the login form and performing login.
    """

    def __init__(self, driver, URL):
        """
        Initializes LoginPage with driver, URL, and locators.

        Args:
            driver (webdriver): WebDriver instance.
            URL (str): The URL of the login page.
        """
        super().__init__(driver, URL)
        self.email_input = (By.XPATH, '//input[@id="email"]')
        self.password_input = (By.XPATH, '//input[@id="password"]')
        self.submit_button = (By.XPATH, '//button[@id="submit"]')
        self.error_message = (By.ID, "error")
        self.open(self.url)

    def enter_email(self, email):
        """
        Enters the provided email address into the email input field.

        Args:
            email (str): The email address to enter.
        """
        el_in = self.find_element(self.email_input)
        el_in.send_keys(email)

    def enter_password(self, password):
        """
        Enters the provided password into the password input field.

        Args:
            password (str): The password to enter.
        """
        el_in = self.find_element(self.password_input)
        el_in.send_keys(password)

    def click_submit_button(self):
        """Clicks the "Submit" button on the login form."""
        btn = self.find_element(self.submit_button)
        btn.click()

    def complete_login(self, email, password):
        """
        Performs a complete login flow.

        Enters email, password, clicks "Submit," and returns ContactListPage.

        Args:
            email (str): The email address to use for login.
            password (str): The password to use for login.

        Returns:
            ContactListPage: An instance of ContactListPage,
                             assuming successful login.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()
        return ContactListPage(self.driver)
