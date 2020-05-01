from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.solarsunrise_urls import ProfilePage
from random import choice
import os


class SettingsPage(Page):
    PATH = '/settings'
    ROOT = {
        'method': By.ID,
        'key': 'settings-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()

    @property
    def form(self):
        return SettingsForm(self.driver)


class SettingsForm(FormComponent):
    file_field = '//input[@id="avatarphoto"]'
    name_field = '//input[@id="name"]'
    surname_field = '//input[@id="surname"]'
    nickname_field = '//input[@id="username"]'
    status_field = '//input[@id="status"]'
    ok_btn = '//input[@class="button-save button-save_pos"]'
    exit_btn = '//a[@href="/profile"]'
    settings_btn = '//img[@data-section="/settings"]'

    def set_avatar(self, file_name=''):
        if file_name == '':
            num = choice([1, 2, 3, 4])
            file_name = os.getcwd() + '/images/beauty' + str(num) + '.jpg'
        self.driver.find_element(By.ID, "avatarphoto").send_keys(file_name)

    def set_name(self, name):
        self.fill_input(self.driver.find_element_by_xpath(self.name_field), name)

    def set_surname(self, surname):
        self.fill_input(self.driver.find_element_by_xpath(self.surname_field), surname)

    def set_nickname(self, nickname):
        self.fill_input(self.driver.find_element_by_xpath(self.nickname_field), nickname)

    def set_status(self, status):
        self.fill_input(self.driver.find_element_by_xpath(self.status_field), status)

    def get_name(self):
        self.wait_for_visible(By.XPATH, self.name_field)
        return self.get_value_elem_text(self.name_field)

    def get_surname(self):
        self.wait_for_visible(By.XPATH, self.surname_field)
        return self.get_value_elem_text(self.surname_field)

    def get_nickname(self):
        self.wait_for_visible(By.XPATH, self.nickname_field)
        return self.get_value_elem_text(self.nickname_field)

    def get_status(self):
        self.wait_for_visible(By.XPATH, self.status_field)
        return self.get_value_elem_text(self.status_field)

    def submit(self, name):
        self.driver.find_element_by_xpath(name).click()

    set_func_dict = {
        'name': set_name,
        'surname': set_surname,
        'nickname': set_nickname,
        'status':  set_status
    }

    get_fields_dict = {
        'name': get_name,
        'surname': get_surname,
        'nickname': get_nickname,
        'status': get_status
    }

    fields = {
        'name': name_field,
        'surname': surname_field,
        'nickname': nickname_field,
        'status': status_field
    }

    def change_field(self, field_name, context):
        self.set_func_dict[field_name](self, context)

        self.submit(self.ok_btn)
        ProfilePage(self.driver, open=False).wait_for_load()
        self.submit(self.settings_btn)

        SettingsPage(self.driver, open=False).wait_for_load()
        text = self.get_fields_dict[field_name](self)
        assert text == context, 'Field was not changed'

    def change_photo(self, file_name=''):
        self.set_avatar(file_name)
        self.submit(self.ok_btn)
        ProfilePage(self.driver, open=False).wait_for_load()
        self.submit(self.settings_btn)

    def change_all_fields(self, name, surname, nickname, status, file_name=''):
        self.set_name(name)
        self.set_surname(surname)
        self.set_nickname(nickname)
        self.set_status(status)
        self.set_avatar(file_name)

        self.submit(self.ok_btn)
        ProfilePage(self.driver, open=False).wait_for_load()
        self.submit(self.settings_btn)

        SettingsPage(self.driver, open=False).wait_for_load()
        assert self.get_name() == name, 'Name was not changed'
        assert self.get_surname() == surname, 'Surname was not changed'
        assert self.get_nickname() == nickname, 'Nickname was not changed'
        assert self.get_status() == status, 'Status was not changed'

    def change_nickname_on_existing(self, nickname):
        self.set_nickname(nickname)

        self.submit(self.ok_btn)
        self.wait_alert_settings()

    def change_empty_field(self, field_name, context):
        text_one = self.get_fields_dict[field_name](self)

        self.set_func_dict[field_name](self, context)

        self.submit(self.ok_btn)
        ProfilePage(self.driver, open=False).wait_for_load()
        self.submit(self.settings_btn)

        SettingsPage(self.driver, open=False).wait_for_load()

        self.wait_for_visible_text(By.XPATH, self.fields[field_name], text_one)

        text = self.get_fields_dict[field_name](self)
        assert text != context, 'Fields with equal values'

    def go_to_profile(self):
        self.submit(self.exit_btn)
        ProfilePage(self.driver, open=False).wait_for_load()
