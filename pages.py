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

# в какой момент разлогиниваться?


class UserName(Component):
    USERNAME = '//*[@id="PH_user-email"]'
    EXIT_BUTTON = '//*[@id="PH_logoutLink"]'

    def get(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class ToolbarGroup(Component):
    UPLOAD_BUTTON = "(//div[@data-name='upload']])[1]"
    UPLOAD_BUTTON1 = "(//div[@class='b-toolbar__btn'])[0]"
    UPLOAD_BUTTON_CSS = 'i.ico_toolbar_upload'
     # Delete all
    SELECT_CHECKBOX = '//div[@data-name="toggleBtn"]'

    REMOVE_DIALOG_BUTTON = '//div[@data-name="remove"]'
    DIALOG_WINDOW = '//div[@class="b-layer__container"]'
    REMOVE_BUTTON = '//button[@data-name="remove"]'

    HOME_BUTTON = '//span[@data-name="home"]'

    def load_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.UPLOAD_BUTTON_CSS))
        )

    def open_form(self):
        self.driver.find_element_by_css_selector(self.UPLOAD_BUTTON_CSS).click()

    def select_all(self):
        self.driver.find_element_by_xpath(self.SELECT_CHECKBOX).click()

    def start_remove_dialog(self):
        self.driver.find_element_by_xpath(self.REMOVE_DIALOG_BUTTON).click()

    def load_dialog(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DIALOG_WINDOW))
        )

    def remove(self):
        self.driver.find_element_by_xpath(self.REMOVE_BUTTON).click()

    def check_delete(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_BUTTON))
        )


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
    FILE = ''
    CHECK_UPLOAD = ''
    DIR_NAME = os.path.dirname(__file__) + "/files_for_upload"

    def go(self):
        # self.is_visibility()
        self.send_file()
        self.check_upload()

    def is_visibility(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT))
        )

    def send_file(self):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(self.DIR_NAME + self.FILE)

    def check_upload(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CHECK_UPLOAD))
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
    FILE = "/test2.png"
    CHECK_UPLOAD = '//*[@data-id="' + FILE + '"]'


class FileInput(Input):
    INPUT = '//input[@class="layer_upload__controls__input"]'
    FILE = "/test.png"
    CHECK_UPLOAD = '//*[@data-id="' + FILE + '"]'