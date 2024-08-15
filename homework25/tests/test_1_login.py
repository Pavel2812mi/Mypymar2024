"""Module containing tests for login functionality."""


import pytest
from homework25.test_data.constants import u_email, u_password
from homework25.test_data.constants import URL
from homework25.pages.login_page import LoginPage


@pytest.mark.login
def test_01_login_with_correct_creds(driver):
    """
    Test login with correct email and password.

    Verifies that a user can successfully log in with valid credentials
    and is redirected to the Contact List page.
    """
    lp = LoginPage(driver, URL)
    contact_list_page = lp.complete_login(u_email, u_password)
    assert "Contact List" in contact_list_page.driver.title, \
        "Login failed or incorrect page loaded"
