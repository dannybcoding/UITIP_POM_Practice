from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SampleAppPage(BasePage):
    """
    Page Object for http://uitestingplayground.com/sampleapp
    A simple login form with dynamically generated element attributes.
    """

    # --- Locators ---
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='UserName']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login")
    LOGIN_STATUS = (By.CSS_SELECTOR, "#loginstatus")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/sampleapp")
        return self

    def login(self, username, password):
        self.type_text(*self.USERNAME_INPUT, username)
        self.type_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

    def get_login_status(self):
        return self.get_text(*self.LOGIN_STATUS)

    def is_logged_in(self):
        return "Welcome" in self.get_login_status()

    def logout(self):
        self.click(*self.LOGIN_BUTTON)
