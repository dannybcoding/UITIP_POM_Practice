from pages.load_delay_page import LoadDelayPage
from pages.home_page import HomePage

class TestLoadDelay:

    def test_load_delay(self, driver):
        page = HomePage(driver).load()
        load_page = page.go_to_load_delay()
        load_page.click_load_delay_button()