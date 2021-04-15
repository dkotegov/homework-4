from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Component(object):
    container = ''

    def __init__(self, driver: Remote):
        self.driver = driver

    def _fill_input(self, by, selector, content, send_enter=False, click=True):
        if click:
            self._wait_clickable(by, selector)
            self._find(selector, by).click()

        self._find(selector, by).send_keys(content)
        if send_enter:
            self._find(selector, by).send_keys(Keys.RETURN)

    def _find(self, selector, by=By.CSS_SELECTOR) -> WebElement:
        return self.driver.find_element(by, selector)

    def _clear(self, by, selector):
        text = self._find(selector, by).text
        while text != '':
            self._find(selector, by).send_keys(Keys.END + Keys.BACKSPACE * len(text))
            text = self._find(selector, by).text

    def _clear_input(self, by, selector, send_enter=False, click=True):
        if click:
            self._wait_clickable(by, selector)
            self._find(selector, by).click()
        self._find(selector, by).send_keys(Keys.END)
        self._clear(by, selector)
        if send_enter:
            self._find(selector, by).send_keys(Keys.RETURN)

    def wait_self(self, by=By.CSS_SELECTOR):
        return self._wait_visible(by, self.container)

    def wait_until_disappear_self(self, by=By.CSS_SELECTOR):
        return self._dis_wait_visible(by, self.container)

    def _wait_text(self, by, selector, text):
        return self._wait(expected_conditions.text_to_be_present_in_element, by, selector, text)

    def _dis_wait_text(self, by, selector, text):
        return self._wait_not(expected_conditions.text_to_be_present_in_element, by, selector, text)

    def _wait_visible(self, by, selector):
        return self._wait(expected_conditions.visibility_of_element_located, by, selector)

    def _wait_presence(self, by, selector):
        return self._wait(expected_conditions.presence_of_element_located, by, selector)

    def _dis_wait_visible(self, by, selector):
        return self._wait_not(expected_conditions.visibility_of_element_located, by, selector)

    def _wait_clickable(self, by, selector):
        return self._wait(expected_conditions.element_to_be_clickable, by, selector)

    def _wait(self, condition: expected_conditions, by, selector, *args):
        return WebDriverWait(self.driver, 30, 0.1).until(
            condition((by, selector), *args)
        )

    def _wait_not(self, condition, by, selector, *args):
        WebDriverWait(self.driver, 30, 0.1).until_not(
            condition((by, selector), *args)
        )
