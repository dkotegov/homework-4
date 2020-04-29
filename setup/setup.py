import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from setup.CustomWebElement import CustomWebElement


class BrowserTypes:
    CHROME = 'chrome'
    FIREFOX = 'firefox'


class Accessor:
    def __init__(self, max_wait_timeout=10):
        self.browser = os.environ.get('BROWSER', 'CHROME').lower()
        self.username = os.environ.get('USERNAME', 'test@test.test')
        self.password = os.environ.get('PASSWORD', 'testtest')
        self.max_wait_timeout = max_wait_timeout
        self.__waiter: WebDriverWait = None
        self.__driver: WebDriver = None
        self._init_driver()

    def _init_driver(self):
        if self.browser == BrowserTypes.FIREFOX:
            options = FirefoxOptions()
            desired_capabilities = DesiredCapabilities.FIREFOX
        elif self.browser == BrowserTypes.CHROME:
            options = ChromeOptions()
            options.add_argument('--allow-running-insecure-content')
            options.add_argument('--ignore-certificate-errors')

            desired_capabilities = DesiredCapabilities.CHROME
        else:
            raise Exception("please specify browser in BROWSER env variable")

        self.__driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                         desired_capabilities=desired_capabilities,
                                         options=options)
        self.__waiter = WebDriverWait(self.__driver, self.max_wait_timeout)

    def shutdown(self):
        if self.__driver is not None:
            self.__driver.quit()

    def wait_for_load(self, id_locator=None, css_locator=None):
        if id_locator is not None:
            self.waiter.until(presence_of_element_located((By.ID, id_locator))).click()
        elif css_locator:
            self.waiter.until(presence_of_element_located((By.CSS_SELECTOR, css_locator))).click()
        else:
            raise Exception("please specify type of selector")

    def find_element_by_css_selector(self, selector: str) -> CustomWebElement:
        return CustomWebElement(self.driver.find_element_by_css_selector(selector), css_locator=selector)

    def find_element_by_id(self, selector: str) -> CustomWebElement:
        return CustomWebElement(self.driver.find_element_by_id(selector), id_locator=selector)

    def wait(self, sec: float):
        self.driver.implicitly_wait(sec)

    @property
    def driver(self) -> WebDriver:
        return self.__driver

    @property
    def current_url(self):
        return self.__driver.current_url

    @property
    def waiter(self) -> WebDriverWait:
        return self.__waiter
