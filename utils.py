from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Utils:
    BASE_URL = 'https://m.calendar.mail.ru/'
    LOGIN_URL = 'https://m.calendar.mail.ru/login'
    sidebar = '.header-menu-item.header-menu-item__sidebutton.header-menu-item__list'
    driver = None
    login_input = 'input[name=Login]'
    password_input = 'input[name=Password]'
    login_button = '.login-button'

    def sign_in(self, login, password):

        def open():
            self.driver.get(self.LOGIN_URL)
            self.wait_redirect(self.LOGIN_URL)
            self.driver.maximize_window()

        def enter_login(login):
            elem = self.wait_renderbtn(self.login_input)
            elem.send_keys(login)

        def enter_password(password):
            elem = self.wait_renderbtn(self.password_input)
            elem.send_keys(password)

        def func_login():
            elem = self.wait_renderbtn(self.login_button)
            elem.click()

        open()
        enter_login(login)
        enter_password(password)
        func_login()
        self.wait_redirect(self.BASE_URL, 10)

    def wait_redirect(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def wait_renderbtn(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_presence_located(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_invisible(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def open_sidebar(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.sidebar))).click()
