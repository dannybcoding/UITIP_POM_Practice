from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class HiddenLayersPage(BasePage):

    # Locators
    GREEN_BUTTON = (By.CSS_SELECTOR, "button.btn-success")
    BLUE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/hiddenlayers")
        return self

    def click_green(self):
        self.click(*self.GREEN_BUTTON)

    def click_blue(self):
        self.click(*self.BLUE_BUTTON)

    def is_blue_visible(self):
        return self.is_visible(self.BLUE_BUTTON)

    def is_green_visible(self):
        return self.is_visible(self.GREEN_BUTTON)

