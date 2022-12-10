import pytest
from selene.support.shared import browser
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
