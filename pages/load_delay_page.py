from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoadDelayPage(BasePage):

    #LOCATORS
    DELAY_BUTTON = (By.XPATH, "//button[text()='Button Appearing After Delay']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/loaddelay")
        return self

    def click_load_delay_button(self):
        self.wait_for_visible(*self.DELAY_BUTTON)
        self.click(*self.DELAY_BUTTON)
