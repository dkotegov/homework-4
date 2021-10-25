
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default_page import DefaultPage


class LoginPage(DefaultPage):
    PATH = ""
    TITLE = ".auth-content-inner__title"
    LOGIN = ".auth-content-form__tel"
    PASSWORD = ".auth-content-form__password"
    SUBMIT = ".auth-content-form__button"
    LOGIN_BUTTON = ".header-right__account"
    LOGINED = ".header-right-avatar__img"

    def auth(self):
        self.__click_button__(self.LOGIN_BUTTON)
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.LOGIN)))
        self.wait(until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.PASSWORD)))
        login = self.driver.find_element(By.CSS_SELECTOR, self.LOGIN)
        login.send_keys("4444444444")
        password = self.driver.find_element(By.CSS_SELECTOR, self.PASSWORD)
        password.send_keys("Qwerty123")
        self.__click_button__(self.SUBMIT)
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.LOGINED)))

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
