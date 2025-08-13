import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from pages.project_page import ProjectPage


@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = Options()

    if os.getenv('CI'):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)

    if not os.getenv('CI'):
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture()
def project_page_fixture(browser):
    browser.get('https://www.simbirsoft.com/portfolio/')
    return ProjectPage(browser)
