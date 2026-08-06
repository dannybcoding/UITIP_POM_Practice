import pytest
from pages.dynamic_id_page import DynamicIdPage


class TestDynamicId:

    def test_button_is_clickable(self, driver):
        """
        The ID on this button changes every reload.
        We locate it by CSS class instead — a stable selector.
        """
        page = DynamicIdPage(driver).load()
        # Should not raise — if we used a dynamic ID this would fail intermittently
        page.click_button()

    def test_ids_differ_between_page_loads(self, driver):
        """Confirm the ID really does change, to understand WHY we avoid it."""
        page = DynamicIdPage(driver).load()

        btn1_id = page.get_button_id()
        driver.refresh()
        btn2_id = page.get_button_id()
        
        print(f"Button ID on first load: {btn1_id}")
        print(f"Button ID after reload: {btn2_id}")

        assert btn1_id != btn2_id, "IDs should be different after reload"
 