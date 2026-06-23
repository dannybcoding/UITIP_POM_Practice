import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Sets up a Chrome WebDriver instance before each test
    and tears it down after. Scope='function' means a fresh
    browser is used for every individual test.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment to run headless (no browser window)
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)  # seconds

    yield driver  # Test runs here

    driver.quit()
