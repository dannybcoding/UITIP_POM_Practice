import pytest
from pages.ajax_page import AjaxPage


class TestAjaxData:

    def test_result_appears_after_request(self, driver):
        """
        Clicking the button triggers an AJAX call that takes ~15 seconds.
        The BasePage wait handles this automatically via WebDriverWait.
        """
        page = AjaxPage(driver).load()
        page.trigger_request()
        # wait_for_visible inside get_result_text will wait up to 15s
        result = page.get_result_text()
        assert result, "Expected a result label to appear after AJAX call"

    def test_result_not_visible_before_click(self, driver):
        page = AjaxPage(driver).load()
        assert not page.is_result_visible(), "Result should not be visible before triggering"
