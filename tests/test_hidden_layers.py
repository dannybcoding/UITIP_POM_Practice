from pages.hidden_layers_page import HiddenLayersPage

class TestHiddenLayersPage:

    def test_green_button(self, driver):
        page = HiddenLayersPage(driver).load()
        assert page.is_green_visible() == True
        assert page.is_blue_visible() == False
        page.click_green()
        assert page.is_blue_visible() == True

    def test_blue_button(self, driver):
        page = HiddenLayersPage(driver).load()
        page.click_green()
        assert page.is_blue_visible() == True
        page.click_blue()
        assert page.is_blue_visible() == True

