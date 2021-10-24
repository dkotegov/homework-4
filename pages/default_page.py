from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DefaultPage:
    BASE_URL = 'https://ykoya.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.maximize_window()
        self.driver.get(url)

    def __click_button__(self, selector):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        link = self.driver.find_element(By.CSS_SELECTOR, selector)
        link.click()

    def wait(self, until, who=None, timeout=30, step=0.1):
        if who is None:
            who = self.driver
        return WebDriverWait(who, timeout, step).until(until)
