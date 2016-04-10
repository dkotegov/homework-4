# -*- coding: utf-8 -*-
import os
import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):

    def __init__(self, driver):
        self.driver = driver


class Page(object):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def enter(self):
        return EnterButton(self.driver)


class AuthForm(Component):
    LOGIN = '//*[@id="ph_login"]'
    PASSWORD = '//*[@id="ph_password"]'

    @property
    def submit(self):
        return SubmitLoginButton(self.driver)

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)


class HomePage(Page):
    PATH = ''

    @property
    def form(self):
        return UploadForm(self.driver)

    @property
    def user_name(self):
        return ToolbarGroup(self.driver)

    @property
    def upload(self):
        return UploadButton(self.driver)

    @property
    def toolbar_buttons(self):
        return ToolbarGroup(self.driver)

    def select_file(self, file_name):
        CHECKBOX = "//div[@data-id='/" + file_name + "']/div[@class='b-checkbox__checkmark']"
        self.driver.find_element_by_xpath(CHECKBOX).click()

# в какой момент разлогиниваться?


class UserName(Component):
    USERNAME = '//*[@id="PH_user-email"]'
    EXIT_BUTTON = '//*[@id="PH_logoutLink"]'

    def get(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class DeleteSubmitDialog(Component):
    @property
    def delete_submit(self):
        return DeleteSubmitButton(self.driver)


class ToolbarGroup(Component):
    @property
    def checkbox(self):
        return SelectAllCheckbox(self.driver)

    @property
    def delete(self):
        return DeleteButton(self.driver)

    @property
    def delete_window(self):
        return DeleteSubmitDialog(self.driver)

    LABEL_FOR_EMPTY = '//div[@class="b-datalist__empty__block"]'

    def cloud_is_empty(self):
        return EC.presence_of_element_located(self.LABEL_FOR_EMPTY)

    # def select_file(self, file_name):
    #     self.driver.find_element_by_xpath(file_name).click()

    HOME_BUTTON = '//span[@data-name="home"]'


class UploadForm(Component):
    @property
    def close(self):
        return CloseUploadFormButton(self.driver)


    @property
    def input_file(self):
        return FileInput(self.driver)

    @property
    def drag_and_drop(self):
        return DragAndDrop(self.driver)


class Button(Component):
    BUTTON = ''
    CHECK_ELEMENT = ''

    def go(self):
        self.is_clickable()
        self.do_click()
        self.check_click()

    def is_clickable(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON))
        )

    def do_click(self):
        self.driver.find_element_by_xpath(self.BUTTON).click()

    def check_click(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CHECK_ELEMENT))
        )


class Input(Component):
    INPUT = ''
    DIR_NAME = os.path.dirname(__file__) + "/files_for_upload/"

    def go(self, file_name):
        # self.is_visibility()
        self.send_file(file_name)
        self.check_upload(file_name)

    def is_visibility(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT))
        )

    def send_file(self, filename):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(self.DIR_NAME + filename)

    def check_upload(self, filename):
        CHECK_UPLOAD = '//*[@data-id="/' + filename + '"]'
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, CHECK_UPLOAD))
        )


class EnterButton(Button):
    BUTTON = '//*[@id="PH_authLink"]'
    CHECK_ELEMENT = '//*[@id="ph_login"]'


class SubmitLoginButton(Button):
    BUTTON = '//span[@data-action="login"]'
    CHECK_ELEMENT = '//span[@data-name="home"]'


class UploadButton(Button):
    BUTTON = '//*[@data-name="upload"]/span'
    CHECK_ELEMENT = '//div[@class="b-layer__container"]'


class CloseUploadFormButton(Button):
    BUTTON = "//div[@class='b-layer__placeholder']/button[@data-name='close']"
    CHECK_ELEMENT = '//span[@data-name="home"]'


class DragAndDrop(Input):
    INPUT = '//input[@class="drop-zone__input"]'


class FileInput(Input):
    INPUT = '//input[@class="layer_upload__controls__input"]'


class SelectAllCheckbox(Button):
    BUTTON = '//div[@data-name="toggleBtn"]'
    CHECK_ELEMENT = '//div[@data-name="remove"]'


class DeleteButton(Button):
    BUTTON = '//div[@data-name="remove"]'
    CHECK_ELEMENT = '//div[@class="b-layer__container"]'


class DeleteSubmitButton(Button):
    BUTTON = '//button[@data-name="remove"]'
    CHECK_ELEMENT = '//span[@data-name="home"]'