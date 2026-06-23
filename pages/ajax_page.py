from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AjaxPage(BasePage):
    """
    Page Object for http://uitestingplayground.com/ajax
    A button triggers an AJAX request; the result only appears after a delay.
    Practice: waiting for dynamically loaded content.
    """

    # --- Locators ---
    TRIGGER_BUTTON = (By.CSS_SELECTOR, "#ajaxButton")
    RESULT_LABEL = (By.CSS_SELECTOR, ".bg-success")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/ajax")
        return self

    def trigger_request(self):
        self.click(*self.TRIGGER_BUTTON)

    def get_result_text(self):
        # Uses wait_for_visible — crucial here because content loads after delay
        return self.get_text(*self.RESULT_LABEL)

    def is_result_visible(self):
        return self.is_displayed(*self.RESULT_LABEL)
