from pages.default import DefaultPage, Component
from utils.helpers import wait_for_visible
from os import getcwd


class SettingsPage(DefaultPage):
    def __init__(self, driver):
        super().__init__(driver, '/settings')
        self.change_avatar_component = ChangeAvatar(self.driver)
        self.change_info_form = ChangeInfoForm(self.driver)

    def change_avatar(self, filename):
        self.change_avatar_component.upload_file(filename)

    def change_info(self, email=None, password=None, confirm_password=None):
        if email is not None:
            self.change_info_form.fill_email_input(email)
        if password is not None:
            self.change_info_form.fill_password_input(password)
        if confirm_password is not None:
            self.change_info_form.fill_confirm_password_input(confirm_password)

    def submit_change_info(self):
        self.change_info_form.submit()

    def submit_change_avatar(self):
        self.change_avatar_component.submit()

    @property
    def avatar_img_src(self):
        return self.change_avatar_component.get_avatar_img().get_attribute('src')

    @property
    def avatar_error_hint(self):
        return self.change_avatar_component.get_error_hint().text

    @property
    def email_error_hint(self):
        return self.change_info_form.get_email_error_hint().text

    @property
    def password_error_hint(self):
        return self.change_info_form.get_passwords_error_hint().text


class ChangeAvatar(Component):
    AVATAR_FILE_INPUT = '#avatar'
    UPLOAD_AVATAR_BUTTON = '#avatar-upload-button'
    AVATAR_IMG = '#avatar-img'
    ERROR_HINT = '#settings-avatar-errors'

    def upload_file(self, filename):
        wait_for_visible(self.driver, self.AVATAR_FILE_INPUT)
        self.driver.find_element_by_css_selector(self.AVATAR_FILE_INPUT).send_keys(f'{getcwd()}/img/{filename}')

    def submit(self):
        wait_for_visible(self.driver, self.UPLOAD_AVATAR_BUTTON)
        self.driver.find_element_by_css_selector(self.UPLOAD_AVATAR_BUTTON).click()

    def get_avatar_img(self):
        wait_for_visible(self.driver, self.AVATAR_IMG)
        return self.driver.find_element_by_css_selector(self.AVATAR_IMG)

    def get_error_hint(self):
        wait_for_visible(self.driver, self.ERROR_HINT)
        return self.driver.find_element_by_css_selector(self.ERROR_HINT)


class ChangeInfoForm(Component):
    EMAIL = '#user-email'
    NEW_PASSWORD = '#user-password'
    CONFIRM_NEW_PASSWORD = '#user-password-repeat'
    EMAIL_ERROR_HINT = '#settings-errors-email'
    PASSWORDS_ERROR_HINT = '#settings-errors-password'
    SUBMIT_BUTTON = '#settings-save-button'

    def fill_email_input(self, new_email):
        wait_for_visible(self.driver, self.EMAIL)
        self.driver.find_element_by_css_selector(self.EMAIL).click()
        self.driver.find_element_by_css_selector(self.EMAIL).clear()
        self.driver.find_element_by_css_selector(self.EMAIL).send_keys(new_email)

    def fill_password_input(self, new_password):
        wait_for_visible(self.driver, self.NEW_PASSWORD)
        self.driver.find_element_by_css_selector(self.NEW_PASSWORD).click()
        self.driver.find_element_by_css_selector(self.NEW_PASSWORD).send_keys(new_password)

    def fill_confirm_password_input(self, new_password_confirm):
        wait_for_visible(self.driver, self.CONFIRM_NEW_PASSWORD)
        self.driver.find_element_by_css_selector(self.CONFIRM_NEW_PASSWORD).click()
        self.driver.find_element_by_css_selector(self.CONFIRM_NEW_PASSWORD).send_keys(new_password_confirm)

    def submit(self):
        wait_for_visible(self.driver, self.SUBMIT_BUTTON)
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()

    def get_email_error_hint(self):
        wait_for_visible(self.driver, self.EMAIL_ERROR_HINT)
        return self.driver.find_element_by_css_selector(self.EMAIL_ERROR_HINT)

    def get_passwords_error_hint(self):
        wait_for_visible(self.driver, self.PASSWORDS_ERROR_HINT)
        return self.driver.find_element_by_css_selector(self.PASSWORDS_ERROR_HINT)
