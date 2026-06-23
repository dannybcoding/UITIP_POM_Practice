import pytest
from pages.text_input_page import TextInputPage


class TestTextInput:

    def test_button_label_updates(self, driver):
        page = TextInputPage(driver).load()
        new_name = "My New Button"
        page.set_new_button_name(new_name)
        page.click_update_button()
        label = page.get_button_label()
        assert new_name in label, f"Expected '{new_name}' in button label, got '{label}'"
