import time

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    time.sleep(10)

    yield

    browser.quit()