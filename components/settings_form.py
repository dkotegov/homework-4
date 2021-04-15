import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from components.base_component import BaseComponent


class SettingsLocators:
    def __init__(self):
        self.root = '//div[@class="profile-view__wrapper"]'
        self.settings_btn = '//div[@class="user-meta__settings"]'
        self.settings_form = '//div[@class="profile-view__profile-wrapper"]'
        self.element_with_text = lambda text: '//*[contains(text(), "{}")]'.format(text)
        # self.login_label = '//div[@class="user-meta__nickname"]'
        self.login_input = '//*[contains(text(), "Имя")]/input'
        self.email_input = '//*[contains(text(), "Почта")]/input'
        self.old_password = '//*[contains(text(), "Старый пароль")]/input'
        self.new_password = '//*[contains(text(), "Новый пароль")]/input'
        self.again_password = '//*[contains(text(), "Повторить пароль")]/input'
        self.submit_button = '//button[contains(text(), "Сохранить")]'
        self.safety_button = '//a[@class="menu-bar__list-item-text list-item__last-child"]'
        self.info_button = '//a[@class="menu-bar__list-item-text list-item__first-child"]'
        self.safety_clicked_button = '//a[@class="menu-bar__list-item-text list-item__last-child list-item-text_selected"]'
        self.avatar_btn = '//button[@class="user-meta__edit-btn"]'
        self.close_button = '//button[@class="close-btn profile__close-btn"]'
        self.settings_wrapper = '//*[@class="profile-view__profile-wrapper"]'


class SettingsForm(BaseComponent):
    def __init__(self, driver):
        super(SettingsForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = SettingsLocators()

    def open_form(self):
        """
        Открывает панель настроек
        """
        open_form_button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.settings_btn))
        )
        open_form_button.click()

    def check_form_is_open(self) -> bool:
        """
        Проверяет открытие панели настроек
        """
        open_form_button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.settings_form))
        )
        return bool(open_form_button)

    def set_login(self, login: str):
        """
        Вводит логин в окне авторизации
        """
        login_input = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.login_input))
        )
        for i in range(0, len(login)):
            login_input.send_keys(Keys.DELETE)
            login_input.send_keys(Keys.BACKSPACE)
        login_input.send_keys(login)

    def set_email(self, old_email: str,  email: str):
        """
        Вводит логин в окне авторизации
        """
        email_input = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_input))
        )
        for i in range(0, len(old_email)):
            email_input.send_keys(Keys.DELETE)
            email_input.send_keys(Keys.BACKSPACE)
        email_input.send_keys(email)

    def _set_password(self, password: str, locator):
        """
        Вводит логин в окне авторизации
        """
        email_input = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        email_input.send_keys(password)

    def set_old_password(self, password: str):
        """
        Вводит логин в окне авторизации
        """
        self._set_password(password, self.locators.old_password)

    def set_new_password(self, password: str):
        """
        Вводит логин в окне авторизации
        """
        self._set_password(password, self.locators.new_password)

    def set_again_password(self, password: str):
        """
        Вводит логин в окне авторизации
        """
        self._set_password(password, self.locators.again_password)

    def submit_form(self):
        """
        Открывает панель настроек
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.submit_button))
        )
        submit[1].click()

    def submit_form_password(self):
        """
        Открывает панель настроек
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_button))
        )
        submit.click()

    def check_login_changed(self, login) -> bool:
        """
        Проверяет открытие панели настроек
        """
        login_label = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.element_with_text(login)))
        )
        return login_label.text == login.upper()

    def check_email_changed(self, email) -> bool:
        """
        Проверяет открытие панели настроек
        """
        login_label = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.element_with_text(email)))
        )
        return login_label.text == email

    def check_error_with_text(self, error_text: str):
        """
        Ождиает пока не появится ошибка авторизации email-а
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.element_with_text(error_text)))
            )
        except TimeoutException:
            return False
        return True

    def click_safety_button(self):
        """
        Открывает панель настроек
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.safety_button))
        )
        submit.click()

    def click_info_button(self):
        """
        Открывает панель настроек
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.info_button))
        )
        submit.click()

    def check_safety_button_clicked(self) -> bool:
        """
        Проверяет открытие панели настроек
        """
        button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.safety_clicked_button))
        )
        return bool(button)

    def click_upload_avatar(self):
        """
        Открывает панель настроек
        """
        btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.avatar_btn))
        )
        btn.click()

    def click_close_button(self):
        """
        Нажимает на кнопку закоытия инфоблока
        """
        button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.close_button))
        )
        button.click()

    def check_settings_closed(self) -> bool:
        """
        Проверяет, закоыт ли инфоблок
        """
        is_closed = WebDriverWait(self.driver, 30, 0.1).until(
            EC.invisibility_of_element_located((By.XPATH, self.locators.settings_wrapper))
        )
        return is_closed
