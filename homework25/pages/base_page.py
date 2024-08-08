"""Module for defining the BasePage class"""


class BasePage:
    """
    Base class for page objects.

    Provides common functionality for interacting with web pages, such as:
        - Initializing page objects with a driver and URL
        - Opening URLs
        - Finding elements
    """

    def __init__(self, driver, url, timeout=10):
        """
        Initializes a BasePage object.

        Args:
            driver (webdriver): WebDriver instance.
            url (str): Base URL of the page.
            timeout (int, optional): Implicit wait timeout in seconds.
            Defaults to 10.
        """
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self, url):
        """
        Opens the specified URL in the browser.

        Args:
            url (str): The URL to open.
        """
        self.driver.get(url)

    def find_element(self, selector):
        """
        Finds a single element on the page using the provided selector.

        Args:
            selector (tuple): A tuple containing the By strategy
            and locator value.

        Returns:
            WebElement: The found element.
        """
        return self.driver.find_element(*selector)

    def find_elements(self, selector):
        """
        Finds all elements on the page matching the provided selector.

        Args:
            selector (tuple): A tuple containing the By strategy
            and locator value.

        Returns:
            list: A list of found WebElements.
        """
        return self.driver.find_elements(*selector)
