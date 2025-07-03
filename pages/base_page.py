from selenium.webdriver.common.by import By
import time
import conftest

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == 'https://www.saucedemo.com/':
            return True
        else:
            return False