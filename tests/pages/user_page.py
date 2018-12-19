# coding=utf-8
import os

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.component import Component
from tests.pages.page import Page


class UserPage(Page):
    BASE_URL = 'http://176.119.156.90/'
    PATH = 'client/'

    NAV_BUTTONS_ID = {
        'all_things': 'allThingsBtn',
        'my_things': 'myThingsBtn'
    }

    PAGES_ID = {
        'all_things': 'allThingsBox',
        'my_things': 'myOwnThingsToReturn'
    }

    USER_INFO_LOGIN_ID = "userLogin"

    @property
    def login_form(self):
        return LoginForm(self.driver)

    @property
    def all_things_list(self):
        return AllThingsList(self.driver)

    @property
    def my_things_list(self):
        return MyThingsList(self.driver)

    @property
    def color_changer(self):
        return ColorChanger(self.driver)

    def goto_all_things(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['all_things']).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.PAGES_ID['all_things']))
        )

    def goto_my_things(self):
        self.driver.find_element_by_id(self.NAV_BUTTONS_ID['my_things']).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.PAGES_ID['my_things']))
        )

    def sign_in(self, login, password):
        self.login_form.set_login(login)
        self.login_form.set_password(password)
        self.login_form.submit()
        self.wait_office_login()

    def wait_office_login(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.ID, self.USER_INFO_LOGIN_ID))
        )

    def get_user_info_login(self):
        return self.driver.find_element_by_id(self.USER_INFO_LOGIN_ID).text


class LoginForm(Component):
    LOGIN_INPUT_ID = "loginField"
    PASSWORD_INPUT_ID = "passwordField"
    SUBMIT_BTN_ID = "signInBtn"

    def set_login(self, login):
        self.get_elem_by_id(self.LOGIN_INPUT_ID).send_keys(login)

    def set_password(self, pswd):
        self.get_elem_by_id(self.PASSWORD_INPUT_ID).send_keys(pswd)

    def submit(self):
        self.get_elem_by_id(self.SUBMIT_BTN_ID).click()

    def get_empty_login_msg(self):
        return "Login is empty."

    def get_empty_password_msg(self):
        return "Password is empty."

    def get_invalid_login_msg(self):
        return "Login contains bad chars."

    def get_invalid_password_msg(self):
        return "Password contains bad chars."

    def get_auth_err_msg(self):
        return "Bad login or password."


class AllThingsList(Component):
    ALL_THINGS_BOX_ID = "allThingsBox"
    TAKE_BTN_CSS = "#allThingsBox button"
    ALL_THINGS_LIST_CSS = "#allThingsBox > div table"
    THING_COUNTER_CSS = ".thingCounterClass"

    def click_take_btn_last(self):
        self.get_last_elem_by_css(self.TAKE_BTN_CSS).click()

    def get_ok_msg(self):
        return "Taking source success."

    def get_not_enough_msg(self):
        return "Not enough source."

    def get_counter_of_last_thing(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.THING_COUNTER_CSS))
        )
        counter_element = WebDriverWait(self.driver, 10, 0.1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.THING_COUNTER_CSS))
        )
        return int(counter_element.text)

    def take_num_of_last_thing(self, num):
        self.click_take_btn_last()
        self.alert_input_and_accept(num)
        alert_text = self.alert_accept()
        return alert_text


class MyThingsList(Component):
    MY_THINGS_BOX_ID = "myOwnThingsToReturn"
    RETURN_BTN_CSS = "#myOwnThingsToReturn button"
    MY_THINGS_LIST_CSS = "#myOwnThingsToReturn > div table"
    THING_COUNTER_CSS = ".returnThingHaveNumberClass"

    def click_return_btn_last(self):
        self.get_last_elem_by_css(self.RETURN_BTN_CSS).click()

    def get_number_of_things_in_list(self):
        self.get_length_of_elem_list_by_css(self.MY_THINGS_LIST_CSS)

    def get_ok_msg(self):
        return "Returning source success."

    def get_not_enough_msg(self):
        return "You have not enough source"

    def get_counter_of_last_thing(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.THING_COUNTER_CSS))
        )
        counter_element = WebDriverWait(self.driver, 10, 0.1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.THING_COUNTER_CSS))
        )
        return int(counter_element.text)

    def return_num_of_last_thing(self, num):
        self.click_return_btn_last()
        self.alert_input_and_accept(num)
        alert_text = self.alert_accept()
        return alert_text


class ColorChanger(Component):
    COLOR_CHANGE_BTN_ID = "changeColorBtn"
    BODY_BACKGROUND_CSS = "body"

    def click_color_change_btn_last(self):
        self.get_elem_by_id(self.COLOR_CHANGE_BTN_ID).click()

    def get_background_color(self):
        return self.get_one_elem_by_css(self.BODY_BACKGROUND_CSS).value_of_css_property('background-color')

    def get_color_from_localstorage(self, key="color"):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)
