from pages.visibility_page import VisibilityPage
from pages.base_page import BasePage


class TestVisibility:

    def test_hide_button(self, driver):
        page = VisibilityPage(driver).load()
        assert page.is_button_visible(page.HIDE_BUTTON) is True
        page.hide_button()
        for name, button in page.VISIBILITY_BUTTONS.items():
            assert page.is_button_visible(button) is False, \
                f"{name} button is still visible"
