import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # aktifkan untuk CI/CD
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
