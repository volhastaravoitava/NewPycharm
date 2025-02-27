from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture()  # предусловие для открытия браузера
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()  # постусловие