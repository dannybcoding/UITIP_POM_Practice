from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextInputPage(BasePage):
    """
    Page Object for http://uitestingplayground.com/textinput
    Typing into this field updates the button label — but only if done correctly.
    Practice: reliable text entry.
    """

    # --- Locators ---
    TEXT_INPUT = (By.CSS_SELECTOR, "#newButtonName")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "#updatingButton")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/textinput")
        return self

    def set_new_button_name(self, name):
        self.type_text(*self.TEXT_INPUT, name)

    def click_update_button(self):
        self.click(*self.UPDATE_BUTTON)

    def get_button_label(self):
        return self.wait_for_visible(*self.UPDATE_BUTTON).get_attribute("value") \
               or self.get_text(*self.UPDATE_BUTTON)
