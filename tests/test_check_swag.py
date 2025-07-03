from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from conftest import browser
from pages.swag_labs import SwagLabs

def test_check_icon_exists(browser):
    page = SwagLabs(browser)
    page.visit()
    try:
        page.exist_icon()
    except NoSuchElementException:
        return None