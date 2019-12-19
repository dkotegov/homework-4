from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGIN_URL = 'https://m.calendar.mail.ru/login'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.LOGIN_URL)
        self.login_input = 'input[name=Login]'
        self.password_input = 'input[name=Password]'
        self.register_button = '.calendar-title'
        self.login_button = '.login-button'
        self.forgot_password_button = '.calendar-title'
        self.html_validation = 'validationMessage'

    def open(self):
        url = self.LOGIN_URL
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_login(self, login):
        elem = self.driver.find_element_by_css_selector(self.login_input)
        elem.send_keys(login)

    def enter_password(self, password):
        elem = self.driver.find_element_by_css_selector(self.password_input)
        elem.send_keys(password)

    def login(self):
        elem = self.driver.find_element_by_css_selector(self.login_button)
        elem.click()

    def register(self):
        elem = self.driver.find_element_by_css_selector(self.register_button)
        elem.click()

    def forgot_password(self):
        elem = self.driver.find_element_by_css_selector(self.forgot_password_button)
        elem.click()

    def get_email_valigation_message(self):
        elem = self.driver.find_element_by_css_selector(self.login_input)
        validation_message = elem.get_attribute(self.html_validation)
        return validation_message.encode('utf-8', errors='ignore')

    def wait_redirect(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
