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
    def clear_folder_form(self):
        return ClearFolderForm(self.driver)

    @property
    def main_form(self):
        return MainForm(self.driver)


class MainForm(Component):
    CREATE_BUTTON = '//span[text()="Добавить папку"]'
    REMOVE_BUTTON = '//*[@data-test-id="folder-delete"]'
    CLEAR_BUTTON = '//*[@data-test-id="folder-clear"]'
    OPEN_EDITOR = '//*[@data-test-id="folder-edit"]'
    CROSS_BUTTON = '//*[@data-test-id="cross"]'

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
            checkbox.click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_xpath(self.CROSS_BUTTON).click()

    def open_folder_editors(self):
        editors = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.OPEN_EDITOR)
        )
        for editor in editors[0:6]:
            editor.click()
            time.sleep(1)
            self.close_folder_popup_by_cross()
        editors[1].click()

    def open_folder_editor(self):
        editor = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OPEN_EDITOR)
        )
        editor.click()


    def clear_folder_popup(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CLEAR_BUTTON)
        )
        button.click()


class AddFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = '//*[@data-test-id="cross"]'
    FOLDER_FRAME = '//input[@name="name"]'
    ADD_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_xpath(self.CROSS_BUTTON).click()

    def create_folder(self, folder_name):
        self.driver.find_element_by_xpath(self.FOLDER_FRAME).send_keys(folder_name)
        self.driver.find_element_by_xpath(self.ADD_FOLDER_BUTTON).click()


class RemoveFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = '//*[@data-test-id="cross"]'
    DELETE_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_xpath(self.CROSS_BUTTON).click()

    def remove_folder(self, folder_name):
        self.driver.find_element_by_xpath(self.DELETE_FOLDER_BUTTON).click()


class EditFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = '//*[@data-test-id="cross"]'
    UNAVAILABLE_POP3 = '//*[@data-test-id="pop3"]'
    PROTECTED_PASSWORD = '//*[@data-test-id="hasPassword"]'
    SET_PASSWORD = '//*[@data-test-id="submit"]'
    RETURN_BACK = '//*[@data-test-id="cancel"]'

    PASSWORD = '//*[@data-test-id="password"]'
    REPEAT_PASSWORD = '//*[@data-test-id="passwordRepeat"]'
    SAVE_PASSWORD = '//*[@data-test-id="submit"]'

    SECRET_QUESTION = '//*[@data-test-id="question"]'
    SECRET_ANSWER = '//*[@data-test-id="answer"]'
    CURRENT_PASSWORD = '//*[@data-test-id="userPassword"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_xpath(self.CROSS_BUTTON).click()

    def unavailable_pop3(self):
        self.driver.find_element_by_xpath(self.UNAVAILABLE_POP3).click()

    def protected_by_password(self):
        self.driver.find_element_by_xpath(self.PROTECTED_PASSWORD).click()

    def set_password_popup(self):
        self.driver.find_element_by_xpath(self.SET_PASSWORD).click()

    def return_back(self):
        self.driver.find_element_by_xpath(self.RETURN_BACK).click()

    def set_folder_pwd(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def repeat_folder_pwd(self, pwd):
        self.driver.find_element_by_xpath(self.REPEAT_PASSWORD).send_keys(pwd)

    def secret_question(self, question):
        self.driver.find_element_by_xpath(self.SECRET_QUESTION).send_keys(question)

    def secret_answer(self, answer):
        self.driver.find_element_by_xpath(self.SECRET_ANSWER).send_keys(answer)

    def set_current_pwd(self, pwd):
        self.driver.find_element_by_xpath(self.CURRENT_PASSWORD).send_keys(pwd)

    def save_folder_pwd(self):
        self.driver.find_element_by_xpath(self.SAVE_PASSWORD).click()

    def set_password(self, folder_pwd, repeated_pwd, question, answer, user_pwd):
        self.set_folder_pwd(folder_pwd)
        self.repeat_folder_pwd(repeated_pwd)
        self.secret_question(question)
        self.secret_answer(answer)
        self.set_current_pwd(user_pwd)
        self.save_folder_pwd()


class ClearFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = '//*[@data-test-id="cross"]'
    CLEAR_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_xpath(self.CROSS_BUTTON).click()

    def clear_folder(self):
        self.driver.find_element_by_xpath(self.CLEAR_FOLDER_BUTTON).click()