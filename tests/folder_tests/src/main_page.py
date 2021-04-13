from selenium.webdriver.support.ui import WebDriverWait
from tests.folder_tests.page_component import Page, Component

import time


class MainPage(Page):
    PATH = ''

    @property
    def add_folder_form(self):
        return AddFolderForm(self.driver)

    @property
    def remove_folder_form(self):
        return RemoveFolderForm(self.driver)

    @property
    def edit_folder_form(self):
        return EditFolderForm(self.driver)

    @property
    def edit_password_form(self):
        return EditPasswordForm(self.driver)

    @property
    def main_form(self):
        return MainForm(self.driver)


class MainForm(Component):
    CREATE_BUTTON = '//span[text()="Добавить папку"]'
    REMOVE_BUTTON = '//*[@data-test-id="folder-delete"]'
    OPEN_EDITOR = '//*[@data-test-id="folder-edit"]'

    CHECKBOX = '//*[@data-test-id="folder-pop3"]'

    def add_folder_popup(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_BUTTON)
        )
        button.click()

    def remove_folder_popup(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_BUTTON)
        )
        button.click()

    def click_pop3_inbox(self):
        checkboxes = self.driver.find_elements_by_xpath(self.CHECKBOX)
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(1)
            checkbox.click()

    def open_folder_editor(self):
        editor = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OPEN_EDITOR)
        )
        editor.click()


class AddFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = 'c01420'
    FOLDER_FRAME = '//input[@name="name"]'
    ADD_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_class_name(self.CROSS_BUTTON).click()

    def create_folder(self, folder_name):
        self.driver.find_element_by_xpath(self.FOLDER_FRAME).send_keys(folder_name)
        self.driver.find_element_by_xpath(self.ADD_FOLDER_BUTTON).click()


class RemoveFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = 'c01420'
    DELETE_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_class_name(self.CROSS_BUTTON).click()

    def remove_folder(self, folder_name):
        self.driver.find_element_by_xpath(self.DELETE_FOLDER_BUTTON).click()


class EditFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = 'c01420'
    UNAVAILABLE_POP3 = '//*[@data-test-id="pop3"]'
    PROTECTED_PASSWORD = '//*[@data-test-id="hasPassword"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_class_name(self.CROSS_BUTTON).click()

    def unavailable_pop3(self):
        self.driver.find_element_by_xpath(self.UNAVAILABLE_POP3).click()

    def protected_by_password(self):
        self.driver.find_element_by_xpath(self.PROTECTED_PASSWORD).click()


class EditPasswordForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = 'c01420'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_class_name(self.CROSS_BUTTON).click()
