"""Module containing test for sign in functionality."""


from casino_test.conftest import driver
from casino_test.test_data.constants import URL, u_nickname, u_email, u_password, u_confirm_password
from casino_test.pages.main_page import MainPage


def test_01_sign_in_with_correct_creds(driver):
    """
    Test for sign in functionality
    """
    mp = MainPage(driver, URL)
    mp.complete_signup(u_nickname, u_email, u_password, u_confirm_password)

    expected_url = "https://poker.evenbetpoker.com/html5-evenbetpoker/d/?tables/all"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"
