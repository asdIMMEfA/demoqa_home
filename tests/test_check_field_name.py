from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.swag_labs import SwagLabs

def test_check_icon_exists(browser):
    page = SwagLabs(browser)
    page.visit()
    try:
        page.exist_name_field()
    except NoSuchElementException:
        return None