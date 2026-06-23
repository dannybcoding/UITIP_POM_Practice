from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ClassAttributePage(BasePage):

    # Locators
    GREEN_BUTTON = (By.CSS_SELECTOR, "button.btn-success")
    BLUE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    YELLOW_BUTTON = (By.CSS_SELECTOR, "button.btn-warning")
    #OK_BUTTON = (By.XPATH, "//button[text()='OK']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/classattr")
        return self

    def click_green(self):
        self.click(*self.GREEN_BUTTON)

    def click_blue(self):
        self.click(*self.BLUE_BUTTON)

    def click_yellow(self):
        self.click(*self.YELLOW_BUTTON)

