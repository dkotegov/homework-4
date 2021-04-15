from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException


class AuthLocators:
    def __init__(self):
        self.root = '//div[@class="popup-container"]'
        self.email_field = '//input[@type="email"]'
        self.password_field = '//input[@type="password"]'
        self.submit_btn = '//button[@type="submit"]'
        self.password_error_label = '//span[@class="error" and @id="password"]'
        self.email_error_label = '//span[@class="error" and @id="email"]'
        self.reg_btn = '//a[@class="popup-helper__modal"]'
        self.header = '//h1[@class="popup-container__heading"]'


class AuthForm(BaseComponent):
    def __init__(self, driver):
        super(AuthForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = AuthLocators()

    def set_email(self, email: str):
        """
        Вводит логин в окне авторизации
        """
        user_email = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_field))
        )
        user_email.send_keys(email)

    def set_password(self, pwd: str):
        """
        Вводит пароль в окне авторизации
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

    def click_reg_btn(self):
        """
        Переходит на страницу регистрации
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.reg_btn))
        )
        submit.click()
    
    def check_password_error(self, error_text: str):
        """
        Ождиает пока не появится ошибка авторизации пароля
        """
        try:
            element = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.password_error_label), error_text))
        except TimeoutException:
            return False
        return True
    
    def check_email_error(self, error_text: str):
        """
        Ождиает пока не появится ошибка авторизации email-а
        """
        try:
            element = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.email_error_label), error_text))
        except TimeoutException:
            return False
        return True

    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется попап регистрации
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.header)))
        if element:
            return element.text == "Авторизация"
        return False