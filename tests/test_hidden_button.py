import pytest
from selenium import webdriver
import time

from pages.base_page import BasePage
from pages.scrollbars_page import Scrollbars_Page

class Test_hidden_button:

    def test_button_is_clickable(self, driver):
        page = Scrollbars_Page(driver).load()
        page.click_hidden_button()
        #time.sleep(4)
