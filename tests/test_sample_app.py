import pytest
from pages.sample_app_page import SampleAppPage

# The password is always "pwd" on this playground
VALID_USER = "testuser"
VALID_PASS = "pwd"


class TestSampleApp:

    def test_successful_login(self, driver):
        page = SampleAppPage(driver).load()
        page.login(VALID_USER, VALID_PASS)
        assert page.is_logged_in(), f"Expected to be logged in. Status: {page.get_login_status()}"

    def test_failed_login_wrong_password(self, driver):
        page = SampleAppPage(driver).load()
        page.login(VALID_USER, "wrongpassword")
        status = page.get_login_status()
        assert "Invalid" in status or "invalid" in status

    def test_login_then_logout(self, driver):
        page = SampleAppPage(driver).load()
        page.login(VALID_USER, VALID_PASS)
        assert page.is_logged_in()
        page.logout()
        assert not page.is_logged_in()
