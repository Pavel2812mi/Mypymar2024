"""Module containing pytest fixtures for UI tests."""


import pytest
from selenium import webdriver
from homework25.test_data.constants import u_email, u_password, URL
from homework25.pages.login_page import LoginPage


@pytest.fixture
def driver():
    """
    Provides a Chrome WebDriver instance.

    Configures the browser window size, sets an implicit wait,
    opens the base URL, yields the driver, and quits the browser
    after the test completes.
    """
    _options = webdriver.ChromeOptions()
    _options.add_argument("windows-size=1920, 1080")
    chrome = webdriver.Chrome(options=_options)
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    """
    Logs in to the application.

    Uses the `driver` fixture to access the browser,
    navigates to the login page, enters credentials,
    and performs login.
    """
    lp = LoginPage(driver, URL)
    lp.complete_login(u_email, u_password)
    return lp
