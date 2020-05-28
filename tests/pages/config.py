from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Seed(object):
    BASE_URL = "https://solarsunrise.ru"

    def wait_for_presence(self, method, key, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((method, key))
        )
        assert element

    def find_element(self, by, value):
        self.wait_for_presence(by, value)
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        self.wait_for_presence(by, value)
        return self.driver.find_elements(by, value)


def onload(func):
    def wrapper(self, *args, **kwargs):
        self.wait_for_load()
        return func(self, *args, **kwargs)

    return wrapper
