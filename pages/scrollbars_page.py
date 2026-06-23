from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Scrollbars_Page (BasePage):

    #Locators
    HIDDEN_BUTTON = (By.CSS_SELECTOR, "#hidingButton")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/scrollbars")
        return self

    def click_hidden_button(self):
        self.scroll_into_view(self.HIDDEN_BUTTON)
        self.click(*self.HIDDEN_BUTTON)
