from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class VisibilityPage(BasePage):
    """
    Page Object for http://uitestingplayground.com/visibility
    A page with elements that change visibility.
    """

    # --- Locators ---
    HIDE_BUTTON = (By.ID, "hideButton")
    TRANSPARENT_BUTTON = (By.ID, "transparentButton")
    REMOVED_BUTTON = (By.ID, "removedButton")
    INVISIBLE_BUTTON = (By.ID, "invisibleButton")
    ZERO_WIDTH_BUTTON = (By.ID, "zeroWidthButton")
    DISPLAY_NONE_BUTTON = (By.ID, "notdisplayButton")
    OVERLAPPED_BUTTON = (By.ID, "overlappedButton")
    OFFSCREEN_BUTTON = (By.ID, "offscreenButton")


    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/visibility")
        return self

    def hide_button(self):
        self.click(*self.HIDE_BUTTON)

    def is_button_visible(self, locator):
        try:
            element = self.find(*locator)
        except Exception:
            return False

        if not element.is_displayed():
            return False

        style = self.driver.execute_script(
            "var s = window.getComputedStyle(arguments[0]); return {visibility: s.visibility, opacity: s.opacity};",
            element
        )

        if style["visibility"] != "visible":
            return False

        try:
            opacity = float(style["opacity"])
        except (TypeError, ValueError):
            opacity = 1.0

        if opacity == 0:
            return False

        rect = self.driver.execute_script(
            "return arguments[0].getBoundingClientRect();",
            element
        )

        if rect["width"] == 0 or rect["height"] == 0:
            return False

        viewport_width = self.driver.execute_script("return window.innerWidth")
        viewport_height = self.driver.execute_script("return window.innerHeight")

        if rect["bottom"] < 0 or rect["top"] > viewport_height:
            return False
        if rect["right"] < 0 or rect["left"] > viewport_width:
            return False

        center_x = rect["left"] + rect["width"] / 2
        center_y = rect["top"] + rect["height"] / 2
        top_element = self.driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);",
            center_x,
            center_y,
        )

        if top_element is None:
            return False

        return self.driver.execute_script(
            "return arguments[0] === arguments[1];",
            top_element,
            element,
        )

    VISIBILITY_BUTTONS = {
    "transparent": TRANSPARENT_BUTTON,
    "removed": REMOVED_BUTTON,
    "invisible": INVISIBLE_BUTTON,
    "zero_width": ZERO_WIDTH_BUTTON,
    "display_none": DISPLAY_NONE_BUTTON,
    "overlapped": OVERLAPPED_BUTTON,
    "offscreen": OFFSCREEN_BUTTON
}

