from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent

class AuthLocators:
    def __init__(self):
        self.email_field = '//input[@id="emailAuth"]'
        self.password_field = '//input[@id="passAuth"]'
        self.submit_btn = '//button[@id="entBtnAuth"]'
        self.profile_btn = '//a[@href="/profile"]'
        self.login_btn = '//a[@href="/auth"]'


class AuthForm(BaseComponent):
    def __init__(self, driver):
        super(AuthForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = AuthLocators()

    PROFILE_BUTTON = '//a[@href="/profile"]'

    def set_email(self, email: str):
        """
        Вводит логин в окне авторизации
        :param email: email пользователя
        """
        user_email = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_field))
        )
        user_email.send_keys(email)

    def set_password(self, pwd: str):
        """
        Вводит пароль в окне авторизации
        :param pwd: пароль пользователя
        """
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.password_field))
        )
        password.send_keys(pwd)

    def submit(self):
        """
        Завершает авторизацию
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_btn))
        )
        submit.click()

    def wait_for_mainpage(self):
        """
        Ождиает пока не откроется главная страница
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.locators.profile_btn)
        )

    def is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.login_btn)))
            return True
        except:
            return False
