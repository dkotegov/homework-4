from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers import wait_for_element_by_selector

class DefaultPage:
    URL = None

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
    

class Component:
    def __init__(self, driver):
        self.driver = driver

    def clear_and_send_keys_to_input(self, cssSelector='', keysToSend='a', needToSubmit=False, needToWait=False):
        if needToWait:
            elem = wait_for_element_by_selector(self.driver, cssSelector)
        else:
            elem = self.driver.find_element_by_css_selector(cssSelector)

        elem.clear()
        elem.send_keys(keysToSend)
        if needToSubmit:
            elem.submit()

    def click_element(self, cssSelector='', needToWait=False):
        if needToWait:
            elem = wait_for_element_by_selector(self.driver, cssSelector)
        else:
            elem = self.driver.find_element_by_css_selector(cssSelector)

        elem.click()

    def switch_to_window(self, num = 0):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def refresh_page(self):
        self.driver.refresh()
