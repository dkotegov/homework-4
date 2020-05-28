from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent
from random import choice
import os


class SettingsPage(Page):
    PATH = "/settings"
    ROOT = {"method": By.ID, "key": "settings-page"}

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
    profile_nickname_field = '//div[@class="profile-username"]'

    def set_avatar(self, file_name=""):
        if file_name == "":
            num = choice([1, 2, 3, 4])
            file_name = os.getcwd() + "/images/beauty" + str(num) + ".jpg"
        self.driver.find_element(By.ID, "avatarphoto").send_keys(file_name)

    def set_name(self, name):
        self.fill_input(self.driver.find_element_by_xpath(self.name_field), name)

    def set_surname(self, surname):
        self.fill_input(self.driver.find_element_by_xpath(self.surname_field), surname)

    def set_nickname(self, nickname):
        self.fill_input(
            self.driver.find_element_by_xpath(self.nickname_field), nickname
        )

    def set_status(self, status):
        self.fill_input(self.driver.find_element_by_xpath(self.status_field), status)

    def get_name(self, context):
        self.wait_for_visible_text(By.XPATH, self.name_field, context)
        return self.get_value_elem_text(self.name_field)

    def get_surname(self, context):
        self.wait_for_visible_text(By.XPATH, self.surname_field, context)
        return self.get_value_elem_text(self.surname_field)

    def get_nickname(self, context):
        self.wait_for_visible_text(By.XPATH, self.nickname_field, context)
        return self.get_value_elem_text(self.nickname_field)

    def get_status(self, context):
        self.wait_for_visible_text(By.XPATH, self.status_field, context)
        return self.get_value_elem_text(self.status_field)

    def submit_ok_button(self):
        self.driver.find_element_by_xpath(self.ok_btn).click()

    def submit_settings_button(self):
        self.driver.find_element_by_xpath(self.settings_btn).click()

    def submit_exit_button(self):
        self.driver.find_element_by_xpath(self.exit_btn).click()

    fields = {
        "name": name_field,
        "surname": surname_field,
        "nickname": nickname_field,
        "status": status_field,
    }

    def get_value(self, context):
        self.wait_for_visible(By.XPATH, self.fields[context])
        return self.get_value_elem_text(self.fields[context])

    def check_nickname(self):
        self.wait_for_visible(By.XPATH, self.profile_nickname_field)
        return self.get_elem_text(self.profile_nickname_field)
