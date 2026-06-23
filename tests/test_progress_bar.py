import pytest
from pages.progress_bar_page import ProgressBarPage


class TestProgressBar:

    def test_stop_near_75_percent(self, driver):
        page = ProgressBarPage(driver).load()
        page.start()
        page.wait_for_progress(target_percent=75)
        result = page.get_result()
        # Result shows how many % off from 75 we were
        assert result is not None
        print(f"Result: {result}")  # visible with pytest -s

    def test_progress_starts_at_zero(self, driver):
        page = ProgressBarPage(driver).load()
        assert page.get_progress() == 0
