from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DefaultPage:
    BASE_URL = 'https://ykoya.ru/'
    PATH = ''
    FOOTER_MY_PRODUCTS = "//div[@class=\"footer-urls-container\"]/a[@href=\"/user/ad\"]"

    def __init__(self, driver):
        self.driver = driver

    def changePath(self, path):
        self.PATH = path

    def open(self):
        url = self.BASE_URL + self.PATH
        self.driver.maximize_window()
        self.driver.get(url)

    def click_footer_my_products(self):
        self.wait(until=EC.element_to_be_clickable((By.XPATH, self.FOOTER_MY_PRODUCTS)))
        link = self.driver.find_element(By.XPATH, self.FOOTER_MY_PRODUCTS)
        link.click()

    def __click_button__(self, selector):
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        link = self.driver.find_element(By.CSS_SELECTOR, selector)
        link.click()

    def wait(self, until, who=None, timeout=30, step=0.1):
        if who is None:
            who = self.driver
        return WebDriverWait(who, timeout, step).until(until)
