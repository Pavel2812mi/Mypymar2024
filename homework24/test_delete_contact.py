"""delete contact test"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest

URL = 'https://thinking-tester-contact-list.herokuapp.com/'


@pytest.fixture()
def browser_webdriver():
    """Set up and teardown for a Chrome browser instance."""
    browser = webdriver.Chrome()
    browser.get(URL)
    yield browser
    browser.quit()


def test_delete_contact(browser_webdriver):
    """Test the functionality of deleting a new contact."""
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
    add_contact_button = wait.until(EC.presence_of_element_located
                                    ((By.ID, 'add-contact')))
    add_contact_button.click()

    firstname_input = (browser_webdriver.find_element
                       (By.XPATH, '//input[@id="firstName"]'))
    firstname_input.send_keys("Andrei")

    lastname_input = (browser_webdriver.find_element
                      (By.XPATH, '//input[@id="lastName"]'))
    lastname_input.send_keys("Egorov")

    submit_button = wait.until(EC.presence_of_element_located
                               ((By.XPATH, '//button[@id="submit"]')))
    submit_button.click()

    name_button = (wait.until
                   (EC.presence_of_element_located
                    ((By.XPATH, '//tr[@class="contactTableBodyRow"]'
                                '/td[text()="Andrei Egorov"]'))))
    name_button.click()

    # delete contact
    delete_button = wait.until(EC.presence_of_element_located
                               ((By.XPATH, '//button[@id="delete"]')))
    delete_button.click()

    alert = Alert(browser_webdriver)
    alert.accept()
    time.sleep(5)

    main_content = (browser_webdriver.find_element
                    (By.CLASS_NAME, "main-content"))

    assert "Andrei Egorov" not in main_content.text, \
        "Ошибка: 'Andrei Egorov' не удален из таблицы"
