from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class ProgressBarPage(BasePage):
    """
    Page Object for http://uitestingplayground.com/progressbar
    Practice: polling a progress bar and stopping at the right moment.
    """

    # --- Locators ---
    START_BUTTON = (By.CSS_SELECTOR, "#startButton")
    STOP_BUTTON = (By.CSS_SELECTOR, "#stopButton")
    PROGRESS_BAR = (By.CSS_SELECTOR, "#progressBar")
    RESULT_LABEL = (By.CSS_SELECTOR, "#result")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.open("/progressbar")
        return self

    def start(self):
        self.click(*self.START_BUTTON)

    def stop(self):
        self.click(*self.STOP_BUTTON)

    def get_progress(self):
        bar = self.wait_for_visible(*self.PROGRESS_BAR)
        return int(bar.get_attribute("aria-valuenow") or bar.text.replace("%", ""))

    def wait_for_progress(self, target_percent, poll_interval=0.2):
        """Poll until the bar reaches target_percent, then stop."""
        while True:
            current = self.get_progress()
            if current >= target_percent:
                self.stop()
                break
            time.sleep(poll_interval)

    def get_result(self):
        return self.get_text(*self.RESULT_LABEL)
