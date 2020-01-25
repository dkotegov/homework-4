from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from ..BaseUrls import BaseUrls


class BasicPage(BaseUrls):

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def wait_redirect(self, url, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def wait_render(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_render_all(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

    def wait_render_by_name(self, name, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.NAME, name)))

    def wait_presence_located(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_visible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_invisible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    def open_iframe(self, selector, timeout=10):
        self.driver.switch_to.frame(0)

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def check_exists(self, selector):
        try:
            self.wait_render(selector, 5)
        except TimeoutException:
            return False
        return True
