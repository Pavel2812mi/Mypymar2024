"""add, edit and delete contact selenium tests"""


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


@pytest.fixture()
def login(browser_webdriver):
    """browser login"""
    email_input = (browser_webdriver.find_element
                   (By.XPATH, '//input[@id="email"]'))
    email_input.send_keys("pavel0837mi@gmail.com")

    password_input = (browser_webdriver.find_element
                      (By.XPATH, '//input[@id="password"]'))
    password_input.send_keys("Kpuw!sfV99fcKxm")

    login_button = (browser_webdriver.find_element
                    (By.XPATH, '//button[@id="submit"]'))
    login_button.click()


@pytest.fixture()
def wait(browser_webdriver):
    """Create a WebDriverWait instance."""
    return WebDriverWait(browser_webdriver, 10)


def test_add_contact(browser_webdriver, login, wait):
    """Test the functionality of adding a new contact."""
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

    submit_button = wait.until(EC.presence_of_element_located
                               ((By.XPATH, '//button[@id="submit"]')))
    submit_button.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "contactTable"), "Vasya Pupkin"))
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "contactTable"), "1989-10-10"))

    table = browser_webdriver.find_element(By.CLASS_NAME, "contactTable")

    assert "Vasya Pupkin" in table.text, \
        "Контакт 'Vasya Pupkin' не найден в таблице после его добавления"


def test_edit_contact(browser_webdriver, login, wait):
    """Test the functionality of editing a contact."""
    contact_name_button = wait.until(EC.presence_of_element_located
                                     ((By.XPATH, '//tr[@class'
                                                 '="contactTableBodyRow"]'
                                                 '/td[text()='
                                                 '"Vasya Pupkin"]')))
    contact_name_button.click()

    edit_button = wait.until(EC.presence_of_element_located
                             ((By.XPATH, '//button[@id="edit-contact"]')))
    edit_button.click()

    firstname_input = (browser_webdriver.find_element
                       (By.XPATH, '//input[@id="firstName"]'))
    firstname_input.clear()
    firstname_input.send_keys("Mikhail")

    lastname_input = (browser_webdriver.find_element
                      (By.XPATH, '//input[@id="lastName"]'))
    lastname_input.clear()
    lastname_input.send_keys("Danilov")

    submit_button = (wait.until
                     (EC.presence_of_element_located
                      ((By.XPATH, '//button[@id="submit"]'))))
    submit_button.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.ID, "firstName"), "Mikhail"))

    wait.until(EC.text_to_be_present_in_element(
        (By.ID, "lastName"), "Danilov"))

    first_name_element = browser_webdriver.find_element(By.ID, "firstName")
    last_name_element = browser_webdriver.find_element(By.ID, "lastName")

    assert first_name_element.text == "Mikhail", \
        (f"Ошибка: ожидалось имя 'Mikhail', "
         f"но получено '{first_name_element.text}'")
    assert (last_name_element.text ==
            "Danilov"), (f"Ошибка: ожидалось имя 'Danilov',"
                         f" но получено '{last_name_element.text}'")


def test_delete_contact(browser_webdriver, login, wait):
    """Test the functionality of deleting a contact."""
    contact_name_button = wait.until(EC.presence_of_element_located
                                     ((By.XPATH, '//tr[@class'
                                                 '="contactTableBodyRow"]'
                                                 '/td[text()'
                                                 '="Mikhail Danilov"]')))
    contact_name_button.click()

    delete_button = wait.until(EC.presence_of_element_located
                               ((By.XPATH, '//button[@id="delete"]')))
    delete_button.click()

    alert = WebDriverWait(browser_webdriver, 5).until(EC.alert_is_present())
    alert.accept()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "contactTableHead"),
        "Name"))

    contact_table = wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "contactTable")))

    assert "Mikhail Danilov" not in contact_table.text, \
        "Ошибка: 'Mikhail Danilov' не был удален из таблицы"
