import urllib.parse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def _wait_until_and_click_elem_by_xpath(self, elem):
        return WebDriverWait(self.driver, 120, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def _wait_for_url(self, url):
        return WebDriverWait(self.driver, 120, 0.1).until(EC.url_to_be(url))

    def _check_if_element_exists_by_xpath(self, elem):
        try:
            WebDriverWait(self.driver, 1, 0.1).until(EC.visibility_of_all_elements_located((By.XPATH, elem)))
        except TimeoutException:
            return False
        return True


class Page(object):
    BASE_URL = 'https://account.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
