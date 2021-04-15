from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException


class RegLocators:
    def __init__(self):
        self.header = '//h1[@class="popup-container__heading"]'
        self.nickname_field = '//input[@name="nickname"]'
        self.email_field = '//input[@type="email"]'
        self.password_field = '//input[@type="password"]'
        self.repeated_password_field = '//input[@name="repeat_password"]'
        self.submit_btn = '//button[@type="submit"]'
        self.email_error_label = '//span[@class="error" and @id="email"]'
        self.password_error_label = '//span[@class="error" and @id="password"]'
        self.repeated_password_error_label = '//span[@class="error" and @id="repeat_password"]'
        self.auth_btn = '//a[@class="popup-helper__modal"]'
        self.close_btn = '//img[@class="btn-close__img"]'
        self.popup = '//div[@class="popup"]'


class RegForm(BaseComponent):
    def __init__(self, driver):
        super(RegForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = RegLocators()
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется попап регистрации
        """
        try:
            element = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.header), "Регистрация"))
        except TimeoutException:
            return False
        return True

    def submit(self):
        """
        Завершает регистрацию
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_btn))
        )
        submit.click()

    def set_nickname(self, nickname: str):
        """
        Вводит логин в окне регистрации
        """
        user_nickname = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.nickname_field))
        )
        user_nickname.send_keys(nickname)

    def set_email(self, email: str):
        """
        Вводит логин в окне регистрации
        """
        user_email = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_field))
        )
        user_email.send_keys(email)

    def set_password(self, pwd: str):
        """
        Вводит пароль в окне регистрации
        """
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.password_field))
        )
        password.send_keys(pwd)

    def set_repeated_password(self, pwd: str):
        """
        Вводит повторный пароль в окне регистрации
        """
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.repeated_password_field))
        )
        password.send_keys(pwd)

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

    def check_repeated_password_error(self, error_text: str):
        """
        Ождиает пока не появится ошибка авторизации пароля
        """
        try:
            element = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.repeated_password_error_label), error_text))
        except TimeoutException:
            return False
        return True

    def click_auth_btn(self):
        """
        Переходит на страницу авторизации
        """
        btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.auth_btn))
        )
        btn.click()

    def click_close_btn(self):
        """
        Кликает на 'закрыть'
        """
        close_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.close_btn))
        )
        close_btn.click()

    def check_disappear(self):
        """
        Проверяет, закрыт ли попап
        """
        try:
            element = WebDriverWait(self.driver, 3, 0.1).until(
                EC.visibility_of_element_located((By.XPATH, self.locators.popup)))
        except TimeoutException:
            return True
        return False
