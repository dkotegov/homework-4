from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Component(object):
    FORM = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def is_open(self):
        try:
            WebDriverWait(self.driver, 3, 0.1).until(lambda d: d.find_element_by_xpath(self.FORM))
        except TimeoutException:
            return False
        return True
