from selenium import webdriver
import pytest
from pages.project_page import ProjectPage

@pytest.fixture(scope='function', autouse=True)
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()



@pytest.fixture()
def project_page_fixture(browser):
    browser.get('https://www.simbirsoft.com/portfolio/')
    return ProjectPage(browser)