"""Module containing test for signin functionality."""


from casino_test.conftest import driver
from casino_test.test_data.constants import URL
from casino_test.pages.main_page import MainPage


def test_01_open_game(signin, driver):
    """
    Test for signin functionality
    """
    mp = MainPage(driver, URL)
    mp.navigate_to_casino_first_game()


