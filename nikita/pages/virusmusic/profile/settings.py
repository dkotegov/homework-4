import os

from nikita.pages.virusmusic.default import Page
from nikita.components.virusmusic.profile_data_form import ProfileDataForm
from nikita.components.virusmusic.password_form import PasswordForm
from nikita.utils import wait_for_pop_up, wait_for_element_by_selector, wait_for_element_by_xpath

class SettingsPage(Page):
    PATH = '/settings'
    AVATAR = '#avatar'
    AVATAR_UPLOAD = 'avatar-upload'
    CONTAINERS = 'm-theme-selector-container-name'
    CURRENT_THEME = '.m-theme-big.is-current-theme'
    THEME_CONTAINER = '#{}'
    THEME_SELECTOR = 'div[id="{}"]'
    CURRENT_LANG = './/img[@class="lang-img selected"]/..'
    LANG_CONTAINER = '#lang'
    LANG_SELECTOR = 'div[id="{}"]'

    def load_avatar(self, path):
        self.open()
        wait_for_element_by_selector(self.driver, self.AVATAR)
        self.driver.find_element_by_id(self.AVATAR_UPLOAD).send_keys(path)

    def change_name(self, name):
        self.open()
        form = ProfileDataForm(self.driver)
        form.set_name(name)
        form.submit()

    def get_name(self):
        self.open()
        form = ProfileDataForm(self.driver)
        return form.get_name_value()

    def change_email(self, email):
        self.open()
        form = ProfileDataForm(self.driver)
        form.set_email(email)
        form.submit()

    def get_email(self):
        self.open()
        form = ProfileDataForm(self.driver)
        return form.get_email_value()

    def change_password(self, newPassword, newPasswordConfirm, password):
        self.open()
        form = PasswordForm(self.driver)
        form.set_new_password(newPassword)
        form.set_new_password_confirm(newPasswordConfirm)
        form.set_password(password)
        form.submit()

    def change_theme(self, theme):
        self.open()
        wait_for_element_by_selector(self.driver, self.THEME_CONTAINER.format(theme.split()[0])).click()
        wait_for_element_by_selector(self.driver, self.THEME_SELECTOR.format(theme)).click()

    def open_containers(self):
        self.open()
        for element in self.driver.find_elements_by_class_name(self.CONTAINERS):
            element.click()

    def get_theme(self):
        self.open_containers()
        return wait_for_element_by_selector(self.driver, self.CURRENT_THEME).get_attribute('id')

    def change_language(self, language):
        self.open()
        wait_for_element_by_selector(self.driver, self.LANG_CONTAINER).click()
        wait_for_element_by_selector(self.driver, self.LANG_SELECTOR.format(language)).click()

    def get_language(self):
        return wait_for_element_by_xpath(self.driver, self.CURRENT_LANG).get_attribute('id')
