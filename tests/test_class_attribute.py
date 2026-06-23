from pages.class_attribute_page import ClassAttributePage
import time

class TestClassAttribute:

    def test_green(self, driver):
        page = ClassAttributePage(driver).load()
        page.click_green()

    def test_blue(self, driver):
        page = ClassAttributePage(driver).load()
        page.click_blue()
        assert page.get_alert_text() == "Primary button pressed"
        page.accept_alert()

        #Make sure alert message is clicked
        page.click_green()


    def test_yellow(self, driver):
        page = ClassAttributePage(driver).load()
        page.click_yellow()

