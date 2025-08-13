from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    DEFAULT_WAIT_TIME = 10
    SHORT_WAIT_TIME = 3
    CUSTOM_POLL_FREQUENCY = 2

    def __init__(self, driver: WebDriver):
        """
        Инициализирует базовую страницу.

        :param driver: WebDriver экземпляр для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_WAIT_TIME)

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))












