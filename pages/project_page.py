from selenium.webdriver.common.by import By
from .base_page import BasePage

LANG = (By.XPATH, '//a[@class="gh-tools-lang"]')

class ProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_element(self):
        self.get_element(LANG).click()

    def get_text(self):
        return self.get_element(LANG).text
