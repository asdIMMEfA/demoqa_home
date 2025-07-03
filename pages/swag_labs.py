from pages.base_page import BasePage
from selenium.common import NoSuchElementException

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_name_field(self):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_login_field(self):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True

