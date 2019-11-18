from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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

    def wait(self, wait_until=None, timeout=10):
        return WebDriverWait(self.driver, timeout).until(wait_until)

    def wait_redirect(self, url = None):
        if url is None:
            self.wait(expected_conditions.url_changes(self.driver.current_url))
        else:
            self.wait(expected_conditions.url_to_be(url))

    def wait_for_css_selector(self, selector = None):
        if selector is None:
            self.wait(expected_conditions.url_changes(self.driver.current_url))
        else:
            return WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )

    def clear_and_send_keys_to_input(self, cssSelector='', keysToSend='a', needToSubmit=False, needToWait=False):
        if needToWait:
            elem = self.wait_for_css_selector(cssSelector)
        else:
            elem = self.driver.find_element_by_css_selector(cssSelector)

        elem.send_keys(keysToSend)
        if needToSubmit:
            elem.submit()

    def click_element(self, cssSelector='', needToWait=False):
        if needToWait:
            elem = self.wait_for_css_selector(cssSelector)
        else:
            elem = self.driver.find_element_by_css_selector(cssSelector)

        elem.click()

    def switch_to_window(self, num = 0):
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(self.driver.window_handles[num])

    def refresh_page(self):
        self.driver.refresh()
