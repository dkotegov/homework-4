from components.navbar_form import NavbarForm
from components.auth_form import AuthForm
from components.subscription_form import SubscriptionForm
from components.settings_form import SettingsForm
from pages.base import BasePage
import pyautogui
import os
import time


class ProfilePage(BasePage):
    """
    Страница поиска
    """

    def __init__(self, driver):
        self.PATH = 'profile'
        self.settings_form = SettingsForm(driver)
        self.subscription_form = SubscriptionForm(driver)
        super(ProfilePage, self).__init__(driver, self.settings_form.locators.root)
        self.navbar_form = NavbarForm(self.driver)

    def click_settings_form_button(self):
        self.settings_form.open_form()

    def check_settings_form_open(self) -> bool:
        return self.settings_form.check_form_is_open()

    def change_login(self, login):
        self.settings_form.set_login(login)
        self.settings_form.submit_form()

    def change_email(self, old_email, email):
        self.settings_form.set_email(old_email, email)
        self.settings_form.submit_form()

    def check_login_changed(self, login) -> bool:
        return self.settings_form.check_login_changed(login)

    def check_email_changed(self, email) -> bool:
        return self.settings_form.check_email_changed(email)

    def check_error_with_text(self, text: str) -> bool:
        return self.settings_form.check_error_with_text(text)

    def click_safety_button(self):
        self.settings_form.click_safety_button()

    def click_info_button(self):
        self.settings_form.click_info_button()

    def check_safety_button_clicked(self) -> bool:
        return self.settings_form.check_safety_button_clicked()

    def change_password(self, old_password, password):
        self.settings_form.set_old_password(old_password)
        self.settings_form.set_new_password(password)
        self.settings_form.set_again_password(password)
        self.settings_form.submit_form_password()

    def change_new_password(self, password):
        self.settings_form.set_new_password(password)

    def change_again_password(self, password):
        self.settings_form.set_again_password(password)

    def submit_form(self):
        self.settings_form.submit_form_password()

    def check_changing_avatar(self) -> bool:
        prev = self.navbar_form.current_avatar()
        self.settings_form.click_upload_avatar()
        pyautogui.write(os.path.abspath('./img/avatar.jpg'))
        pyautogui.press('enter')
        pyautogui.press('enter')
        self.open()
        curr = self.navbar_form.current_avatar()
        return not prev == curr

    def click_close_button(self):
        self.settings_form.click_close_button()

    def check_close_clicked(self) -> bool:
        return self.settings_form.check_settings_closed()

    def click_subscription_button(self):
        self.subscription_form.click_subscription()

    def check_umoney_redirected(self) -> bool:
        return self.subscription_form.check_umoney_open()
