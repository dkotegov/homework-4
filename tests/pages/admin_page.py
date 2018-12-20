# coding=utf-8
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.component import Component
from tests.pages.page import Page


class AdminPage(Page):
    BASE_URL = 'http://176.119.156.90/'
    PATH = 'admin.html'

    NAV_BUTTONS_ID = {
        'source_form': 'b1',
        'user_form': 'b2',
        'source_list': 'b4',
        'user_list': 'b3',
        'reset_btn': 'b5'
    }

    PAGES_ID = {
        'source_form': 'box1',
        'user_form': 'box2',
        'source_list': 'box4',
        'user_list': 'box3',
        'users_source': 'box5'
    }

    @property
    def user_form(self):
        return UserForm(self.driver)

    @property
    def source_form(self):
        return SourceForm(self.driver)

    @property
    def user_list(self):
        return UserList(self.driver)

    @property
    def source_list(self):
        return SourceList(self.driver)

    def goto_user_form(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['user_form']).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.PAGES_ID['user_form']))
        )

    def goto_user_list(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['user_list']).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.PAGES_ID['user_list']))
        )

    def goto_source_form(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['source_form']).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.PAGES_ID['source_form']))
        )

    def goto_source_list(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['source_list']).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.PAGES_ID['source_list']))
        )

    def add_user(self, name, password):
        self.goto_user_form()
        self.user_form.clear_login()
        self.user_form.clear_password()
        self.user_form.set_login(name)
        self.user_form.set_password(password)
        self.user_form.submit()
        alert_text = self.alert_accept()
        return alert_text

    def add_source(self, name, description, number, src_id):
        self.goto_source_form()
        self.source_form.clear_form()
        self.source_form.set_id(src_id)
        self.source_form.set_name(name)
        self.source_form.set_description(description)
        self.source_form.set_number(number)
        self.source_form.attach_image()
        self.source_form.submit()
        alert_text = self.alert_accept()
        return alert_text

    def reset(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['reset_btn']).click()
        WebDriverWait(self.driver, 10, 0.1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        WebDriverWait(self.driver, 10, 0.1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()


class UserForm(Component):
    LOGIN_ID = "fieldLogin"
    PASSWORD_ID = "fieldPassword"
    DEPARTMENT_LIST_ID = "fieldDepartment"
    SUBMIT_ID = "sendButtonUser"

    def set_login(self, login):
        self.get_elem_by_id(self.LOGIN_ID).send_keys(login)

    def set_password(self, pswd):
        self.get_elem_by_id(self.PASSWORD_ID).send_keys(pswd)

    def clear_login(self):
        self.get_elem_by_id(self.LOGIN_ID).clear()

    def clear_password(self):
        self.get_elem_by_id(self.PASSWORD_ID).clear()

    def submit(self):
        self.get_elem_by_id(self.SUBMIT_ID).click()


class UserList(Component):
    TABLE_BOX_ID = "usersBox"
    NUM_RECORDS_IN_TABLE = "#usersBox table tr"

    def count_records(self):
        count = len(self.driver.find_elements_by_css_selector(self.NUM_RECORDS_IN_TABLE))
        return count


class SourceForm(Component):
    IDENTIFIER_ID = "fieldId"
    NAME_ID = "fieldName"
    DESCRIPTION_ID = "fieldDescription"
    NUMBER_ID = "fieldNumber"
    IMAGE_INPUT_ID = "fieldImage"
    SUBMIT_ID = "sendButton"

    def set_id(self, id_num):
        self.get_elem_by_id(self.IDENTIFIER_ID).send_keys(id_num)

    def set_name(self, name):
        self.get_elem_by_id(self.NAME_ID).send_keys(name)

    def set_description(self, description):
        self.get_elem_by_id(self.DESCRIPTION_ID).send_keys(description)

    def set_number(self, number):
        self.get_elem_by_id(self.NUMBER_ID).send_keys(number)

    def submit(self):
        self.get_elem_by_id(self.SUBMIT_ID).click()

    def attach_image(self):
        self.get_elem_by_id(self.IMAGE_INPUT_ID).send_keys(
            os.path.join(os.getcwd(), 'tests/img/test_img.jpg'))

    def clear_form(self):
        self.get_elem_by_id(self.IDENTIFIER_ID).clear()
        self.get_elem_by_id(self.NAME_ID).clear()
        self.get_elem_by_id(self.DESCRIPTION_ID).clear()
        self.get_elem_by_id(self.NUMBER_ID).clear()
        self.get_elem_by_id(self.IMAGE_INPUT_ID).clear()


class SourceList(Component):
    TABLE_BOX_ID = "sourceBox"
    NUM_RECORDS_IN_TABLE = "#sourceBox table tr"

    def count_records(self):
        count = len(self.driver.find_elements_by_css_selector(self.NUM_RECORDS_IN_TABLE))
        return count
