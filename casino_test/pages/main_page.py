"""Module representing the main page object."""

from selenium.webdriver.common.by import By
from casino_test.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainPage(BasePage):
    """
    Represents the Main page of the web application.
    """

    def __init__(self, driver, URL):
        super().__init__(driver, URL)
        self.sign_up_button = (By.XPATH, "//div[@class='panel button SimpleButton SimpleButton_v_flat SimpleButton"
                                         "_c_gradient_primary SimpleButton_use_text MiniUserInfo"
                                         "__sign_up_button SimpleButton_interactive']")
        self.nickname_input = (By.XPATH, "(//input[@class='Input Input_v_rounded_outline Input_c_blue with_clear_button'])[1]")
        self.email_input = (By.XPATH, "//input[@class='Input Input_v_rounded_outline Input_c_blue with_clear_button' and @type='email']")
        self.password_input = (By.XPATH, "(//input[@class='Input Input_v_rounded_outline Input_c_blue' and @type='password'])[1]")
        self.confirm_password_input = (By.XPATH, "(//input[@class='Input Input_v_rounded_outline Input_c_blue' and @type='password'])[2]")
        self.send_button = (By.XPATH,
                            "//div[@class='panel button SimpleButton SimpleButton_v_flat SimpleButton_c_gradient_primary SimpleButton_use_text"
                            " widget-form-button send-form SimpleButton_interactive']")

        self.casino_button = (By.XPATH, '(//div[contains(@class, "TabButton__content")])[3]')
        self.casino_first_game_image = (By.XPATH, '(//div[@class="image"])[1]')
        self.casino_first_game_button = (By.XPATH, '//div[@class="panel WidgetCasinoGameListItemContainer__play"]')
        self.open(self.url)

    def click_sign_up_button(self):
        """
        Clicks the "Sign up" button.
        """
        WebDriverWait(self.driver, 1990).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='panel button SimpleButton SimpleButton_v_flat SimpleButton_c_gradient_primary"
                                        " SimpleButton_use_text MiniUserInfo__sign_up_button SimpleButton_interactive']"))
        ).click()

    def enter_nickname(self, nickname):
        """
        Enters the provided nickname into the nickname input field.
        """
        el_in = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(self.nickname_input)
        )
        el_in.send_keys(nickname)

    def enter_email(self, email):
        """
        Enters the provided email address into the email input field.
        """
        el_in = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(self.email_input)
        )
        el_in.send_keys(email)

    def enter_password(self, password):
        """
        Enters the provided password into the password input field.

        Args:
            password (str): The password to enter.
        """
        el_in = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(self.password_input)
        )
        el_in.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        """
        Enters the provided password again into the password input field.

        Args:
            confirm_password (str): The password to enter.
        """
        el_in = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(self.password_input)
        )
        el_in.send_keys(confirm_password)

    def click_send_button(self):
        """Clicks the "send" button on the signup form."""
        btn = self.find_element(self.send_button)
        btn.click()
        time.sleep(5)

    def complete_signup(self, nickname, email, password, confirm_password):
        """
        signup
        """
        self.click_sign_up_button()
        self.enter_email(email)
        self.enter_nickname(nickname)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_send_button()

    def click_casino_button(self):
        """
        Clicks the "Casino" button.
        """
        el_in = WebDriverWait(self.driver, 55).until(
            EC.presence_of_element_located(self.casino_button)
        )
        el_in.click()
        time.sleep(150)

    def click_casino_first_game_button(self):
        """
        Clicks the "Casino" first game button.
        """
        image = WebDriverWait(self.driver, 55).until(
            EC.presence_of_element_located(self.casino_first_game_image)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(image).perform()

        play_button = WebDriverWait(self.driver, 55).until(
            EC.presence_of_element_located(self.casino_first_game_button)
        )

        play_button.click()

    def navigate_to_casino_first_game(self):
        """
        Navigates to casino first game
        """
        self.click_casino_button()
        self.click_casino_first_game_button()