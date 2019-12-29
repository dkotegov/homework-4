from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasicPage:
    MAIL_URL = 'https://e.mail.ru/inbox'
    LOGIN_URL = 'https://account.mail.ru/login'
    AUTH_URL = 'https://e.mail.ru/login'
    SIGNUP_URL = 'https://account.mail.ru/signup'
    SETTINGS_URL = 'https://e.mail.ru/settings/userinfo'
    driver = None

    def wait_redirect(self, url, timeout=100):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def wait_render(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_render_by_name(self, name, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.NAME, name)))

    def wait_presence_located(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_invisible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def open_iframe(self, selector, timeout=10):
        self.driver.switch_to.frame(0)
