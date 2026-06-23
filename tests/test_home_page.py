import pytest
from pages.home_page import HomePage


class TestHomePage:

    def test_page_title(self, driver):
        page = HomePage(driver).load()
        assert "UI Test Automation Playground" in driver.title

    def test_heading_visible(self, driver):
        page = HomePage(driver).load()
        heading = page.get_heading()
        assert "UI Test Automation" in heading
