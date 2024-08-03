"""add contact test"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

URL = 'https://thinking-tester-contact-list.herokuapp.com/'


@pytest.fixture()
def browser_webdriver():
    """Set up and teardown for a Chrome browser instance."""
    browser = webdriver.Chrome()
    browser.get(URL)
    yield browser
    browser.quit()


def test_add_contact(browser_webdriver):
    """Test the functionality of adding a new contact."""
    wait = WebDriverWait(browser_webdriver, 10)

    # login
    email_input = (browser_webdriver.find_element
                   (By.XPATH, '//input[@id="email"]'))
    email_input.send_keys("pavel0837mi@gmail.com")

    password_input = (browser_webdriver.find_element
                      (By.XPATH, '//input[@id="password"]'))
    password_input.send_keys("Kpuw!sfV99fcKxm")

    login_button = (browser_webdriver.find_element
                    (By.XPATH, '//button[@id="submit"]'))
    login_button.click()

    # add contact
    add_contact_button = (wait.until
                          (EC.presence_of_element_located
                           ((By.ID, 'add-contact'))))
    add_contact_button.click()

    firstname_input = (browser_webdriver.find_element
                       (By.XPATH, '//input[@id="firstName"]'))
    firstname_input.send_keys("Vasya")

    lastname_input = (browser_webdriver.find_element
                      (By.XPATH, '//input[@id="lastName"]'))
    lastname_input.send_keys("Pupkin")

    date_of_birth_input = (browser_webdriver.find_element
                           (By.XPATH, '//input[@id="birthdate"]'))
    date_of_birth_input.send_keys("1989-10-10")

    phone_input = (browser_webdriver.find_element
                   (By.XPATH, '//input[@id="phone"]'))
    phone_input.send_keys("8005551234")

    email_input = (browser_webdriver.find_element
                   (By.XPATH, '//input[@id="email"]'))
    email_input.send_keys("Vas12345@gmail.com")

    submit_button = wait.until(EC.presence_of_element_located
                               ((By.XPATH, '//button[@id="submit"]')))
    submit_button.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "main-content"), "Vasya Pupkin"))
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "main-content"), "1989-10-10"))
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "main-content"), "vas12345@gmail.com"))
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "main-content"), "8005551234"))

    table = browser_webdriver.find_element(By.CLASS_NAME, "main-content")

    assert "Vasya Pupkin" in table.text, \
        "Контакт 'Vasya Pupkin' не найден в таблице после его добавления"
