from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicIdPage(BasePage):
    """
    Page Object for http://uitestingplayground.com/dynamicid
    Demonstrates that buttons have IDs that change on every page load.
    The correct approach is to find elements by stable attributes instead.
    """

    # --- Locators ---
    # BAD example — do NOT use dynamic IDs like "id=button-abc123"
    # GOOD example — use class or text content
    BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    HEADING = (By.CSS_SELECTOR, "h3")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/dynamicid")
        return self

    def click_button(self):
        self.click(*self.BUTTON)

    def get_heading(self):
        return self.get_text(*self.HEADING)
