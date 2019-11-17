from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DefaultPage:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, wait_until=None, timeout=10):
        return WebDriverWait(self.driver, timeout).until(wait_until)

    def wait_redirect(self, url = None):
        if url is None:
            self.wait(EC.url_changes(self.driver.current_url))
        else:
            self.wait(EC.url_to_be(url))

    def wait_for_css_selector(self, selector = None):
        if selector is None:
            self.wait(EC.url_changes(self.driver.current_url))
        else:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )

    def clear_and_send_keys_to_input(self, cssSelector='', keysToSend='a', needToSubmit=False, needToWait=False):
        if needToWait:
            elem = self.wait_for_css_selector(cssSelector)
        else:
            elem = self.driver.find_element_by_css_selector(cssSelector)
        elem.clear()
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
        self.driver.switch_to.window(self.driver.window_handles[num])

    def resresh_page(self):
        self.driver.refresh()

