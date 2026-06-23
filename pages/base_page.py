from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


BASE_URL = "http://uitestingplayground.com"


class BasePage:
    """
    Parent class for all Page Objects.
    Contains shared helper methods every page can use.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    def open(self, path=""):
        self.driver.get(f"{BASE_URL}{path}")

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def wait_for_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def wait_for_visible(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def click(self, by, locator):
        self.wait_for_clickable(by, locator).click()

    def type_text(self, by, locator, text):
        element = self.wait_for_visible(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        return self.wait_for_visible(by, locator).text

    def is_displayed(self, by, locator):
        try:
            return self.wait_for_visible(by, locator).is_displayed()
        except Exception:
            return False

    def scroll_into_view(self, locator):
        element = self.find(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        return element

