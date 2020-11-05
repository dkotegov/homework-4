import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from romanov.app.myWebElement import MyWebElement
from selenium.webdriver.firefox.webdriver import Options as FirefoxOptions
from selenium.webdriver.chrome.webdriver import Options as ChromeOptions

class Connect:
    def __init__(self):
        self.timeout = 15
        self.username = os.environ.get('LOGIN', 'test1234678')
        self.password = os.environ.get('PASSWORD', '123456')
        self.browser = os.environ.get('BROWSER', 'CHROME')

        self.options = None
        if self.browser == 'CHROME':
            self.options = ChromeOptions()
            self.options.add_argument("--incognito")
        elif self.browser == 'FIREFOX':
            self.options = FirefoxOptions()
            self.options.addArguments("-private")

        self.driver: Remote = None
        self.wait: WebDriverWait = None

    def init(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.browser).copy(),
            options=self.options
        )
        self.wait = WebDriverWait(self.driver, self.timeout)

    def destroy(self):
        self.driver.quit()

    def load_wait(self, id=None, css=None):
        if css:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, css)))
        else:
            self.wait.until(presence_of_element_located((By.ID, id)))

    def find_el_id(self, id):
        return MyWebElement(self.driver.find_element_by_id(id), id=id)

    def find_el_css(self, css):
        return MyWebElement(self.driver.find_element_by_css_selector(css), css=css)

    def find_els_css(self, css):
        return [MyWebElement(el) for el in self.driver.find_elements_by_css_selector(css)]

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)


connect = Connect()
