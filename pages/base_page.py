import pyautogui

from selenium.webdriver import Remote, ActionChains
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

    def set_field(self, locator, value):
        el = self.locate_el(locator)
        el.clear()
        el.send_keys(value)

    def get_popup(self):
        return self.locate_el('.popup-message:last-child')

    def is_popup_success(self):
        return self.get_popup().get_attribute('class').find('success') != -1

    def locate_el(self, css_sel, wait: float = 3.0) -> WebElement:
        waiter = WebDriverWait(self.driver, wait)
        return waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_sel)))

    def click(self, css_sel):
        self.locate_el(css_sel).click()

    def locate_hidden_el(self, css_sel, wait: float = 3.0) -> WebElement:
        waiter = WebDriverWait(self.driver, wait)
        return waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_sel)))

    def click_hidden(self, css_sel):
        el = self.locate_hidden_el(css_sel)
        ActionChains(self.driver).move_to_element(el).perform()
        el.click()

    def drag_and_drop(self, css_sel_source, css_sel_target):
        source = self.locate_hidden_el(css_sel_source)
        target = self.locate_hidden_el(css_sel_target)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def enter_file_path(self, clickf, path):
        old_width = pyautogui.getActiveWindow().width

        clickf()

        new_width = old_width
        while old_width == new_width:
            new_width = pyautogui.getActiveWindow().width
            pyautogui.sleep(0.1)

        pyautogui.write(path)
        pyautogui.press('enter')
