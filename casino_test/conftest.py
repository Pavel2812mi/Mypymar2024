"""Module containing pytest fixtures for UI tests."""


import pytest
from selenium import webdriver
from casino_test.test_data.constants import URL, u_nickname, u_email, u_password, u_confirm_password
from casino_test.pages.main_page import MainPage


@pytest.fixture
def driver():
    """
    Provides a Chrome WebDriver instance.

    Configures the browser window size, sets an implicit wait,
    opens the base URL, yields the driver, and quits the browser
    after the test completes.
    """
    _options = webdriver.ChromeOptions()
    _options.add_argument("window-size=1920,1080")
    chrome = webdriver.Chrome(options=_options)

    yield chrome
    chrome.quit()


@pytest.fixture
def signin(driver):
    """
    Sign in to the application.
    """
    sp = MainPage(driver, URL)
    sp.complete_signup(u_nickname, u_email, u_password, u_confirm_password)
    return sp
