import os
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from pages.project_page import ProjectPage


@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = Options()

    if os.getenv('CI'):
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(options=chrome_options)

    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()


@pytest.fixture()
def project_page_fixture(browser):
    browser.get('https://www.simbirsoft.com/portfolio/')
    return ProjectPage(browser)
