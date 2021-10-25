from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException


class BasePage:
    BASE_URL = 'https://mail.liokor.ru'
    PATH = '/'

    def __init__(self, driver: Remote, base_css_sel=''):
        self.driver = driver
        self.base_css_sel = base_css_sel

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.driver.maximize_window()

    def is_opened(self):
        try:
            self.locate_el(self.base_css_sel)
            return True
        except TimeoutException:
            return False

    def get_popup(self):
        return self.locate_el('.popup-message')

    def locate_el(self, css_sel, wait: float = 3.0) -> WebElement:
        waiter = WebDriverWait(self.driver, wait)
        return waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_sel)))
