import time

import pyautogui

from selenium.webdriver import Remote, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import settings as s


class BasePage:
    WAIT_TIME = 1.5

    BASE_URL = s.BASE_URL
    PATH = '/'

    FILE_INPUT = '#filesImageInput'

    def __init__(self, driver: Remote, base_css_sel=''):
        self.driver = driver
        self.base_css_sel = base_css_sel

    def wait_until(self, cond_f, wait: float = None):
        if wait is None:
            wait = self.WAIT_TIME
        waiter = WebDriverWait(self.driver, wait)
        return waiter.until(cond_f)

    def open(self):
        self.driver.get(self.BASE_URL + self.PATH)
        self.driver.maximize_window()

    def is_opened(self):
        if not self.base_css_sel:
            raise Exception('base_css_sel is empty, unable to check if page is opened')

        try:
            self.locate_el(self.base_css_sel)
            return True
        except TimeoutException:
            return False

    def send_file(self, open_click, path):
        open_click()

        avatar_input = self.locate_hidden_el(self.FILE_INPUT)
        avatar_input.send_keys(path)

        # closing file select dialog
        # this probably won't work on macOS
        self.close_browser_dialogue()

    def set_field(self, locator, value):
        el = self.locate_el(locator)
        el.clear()
        if value:
            el.send_keys(value)
        else:
            # clear() not triggering "input" event
            el.send_keys('w' + Keys.BACKSPACE)

    def is_windows(self):
        return self.driver.capabilities.get('platformName', 'windows') == 'windows'

    def select_all(self, el: WebElement):
        if self.is_windows():
            el.send_keys(Keys.CONTROL + 'a')
        else:
            el.send_keys(Keys.COMMAND + 'a')

    def get_popup(self):
        return self.locate_el('.popup-message:last-child')

    def is_popup_success(self):
        self.locate_el('.popup-message.success:last-child')
        return 'success' in self.get_popup().get_attribute('class')

    def is_popup_error(self):
        self.locate_el('.popup-message.error:last-child')
        return 'error' in self.get_popup().get_attribute('class')

    def locate_el(self, css_sel, wait: float = 3.0) -> WebElement:
        return self.wait_until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_sel)), wait)

    def locate_hidden_el(self, css_sel, wait: float = 3.0) -> WebElement:
        return self.wait_until(EC.presence_of_element_located((By.CSS_SELECTOR, css_sel)), wait)

    def close_browser_dialogue(self):
        # waits for active window to change and returns it
        def window_changed(driver):
            active_window = pyautogui.getActiveWindow()
            if driver.get_window_size()['width'] == active_window.width:
                return False
            return active_window

        dialogue_window = self.wait_until(window_changed)
        dialogue_window.close()

    def click(self, css_sel):
        self.locate_el(css_sel).click()

    def click_hidden(self, css_sel):
        el = self.locate_hidden_el(css_sel)
        ActionChains(self.driver).move_to_element(el).perform()
        el.click()

    def drag_and_drop(self, css_sel_source, css_sel_target):
        source = self.locate_hidden_el(css_sel_source)
        target = self.locate_hidden_el(css_sel_target)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
