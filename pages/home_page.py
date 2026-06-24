from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.load_delay_page import LoadDelayPage


class HomePage(BasePage):
    """Page Object for http://uitestingplayground.com/home"""

    # --- Locators ---
    HEADING = (By.CSS_SELECTOR, "h1")
    NAV_HOME = (By.LINK_TEXT, "Home")
    NAV_RESOURCES = (By.LINK_TEXT, "Resources")

    # Each playground link by its partial link text
    DYNAMIC_ID_LINK = (By.LINK_TEXT, "Dynamic ID")
    CLASS_ATTR_LINK = (By.LINK_TEXT, "Class Attribute")
    AJAX_DATA_LINK = (By.LINK_TEXT, "AJAX Data")
    SAMPLE_APP_LINK = (By.LINK_TEXT, "Sample App")
    CLICK_LINK = (By.LINK_TEXT, "Click")
    TEXT_INPUT_LINK = (By.LINK_TEXT, "Text Input")
    PROGRESS_BAR_LINK = (By.LINK_TEXT, "Progress Bar")
    SHADOW_DOM_LINK = (By.LINK_TEXT, "Shadow DOM")
    LOAD_DELAY_LINK = (By.LINK_TEXT, "Load Delay")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/home")
        return self

    def get_heading(self):
        return self.get_text(*self.HEADING)

    def go_to_dynamic_id(self):
        self.click(*self.DYNAMIC_ID_LINK)

    def go_to_class_attr(self):
        self.click(*self.CLASS_ATTR_LINK)

    def go_to_ajax_data(self):
        self.click(*self.AJAX_DATA_LINK)

    def go_to_sample_app(self):
        self.click(*self.SAMPLE_APP_LINK)

    def go_to_click(self):
        self.click(*self.CLICK_LINK)

    def go_to_text_input(self):
        self.click(*self.TEXT_INPUT_LINK)

    def go_to_progress_bar(self):
        self.click(*self.PROGRESS_BAR_LINK)

    def go_to_shadow_dom(self):
        self.click(*self.SHADOW_DOM_LINK)

    def go_to_load_delay(self):
        self.click(*self.LOAD_DELAY_LINK)
        return LoadDelayPage(self.driver)
