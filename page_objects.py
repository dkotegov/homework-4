# -*- coding: utf-8 -*-
import os
import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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
    def top_menu(self):
        return TopMenuBefore(self.driver)


class TopMenuBefore(Component):
    ENTER_BUTTON = '//*[@id="PH_authLink"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.ENTER_BUTTON).click()


class AuthForm(Component):
    LOGIN = '//*[@id="ph_login"]'
    PASSWORD = '//*[@id="ph_password"]'
    SUBMIT = '//input[@class="x-ph__button__input"]'

    def load_form(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN))
        )

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class HomePage(Page):
    PATH = ''


    @property
    def top_menu(self):
        return TopMenuAfter(self.driver)

    @property
    def form(self):
        return UploadForm(self.driver)

    @property
    def toolbar_group(self):
        return ToolbarGroup(self.driver)

# при регистрации и в облаке TopMenu это один и тот жк компонент?
# в какой момент разлогиниваться?


class TopMenuAfter(Component):
    USERNAME = '//*[@id="PH_user-email"]'
    EXIT_BUTTON = '//*[@id="PH_logoutLink"]'

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )

    def logout(self):
        self.driver.find_element_by_xpath(self.EXIT_BUTTON).click()


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
    FORM = '//div[@class="b-layer__container"]'
    # Close
    CLOSE = "//div[@class='b-layer__placeholder']/button[@data-name='close']"
    CLOSE_CSS = '.ico.ico_layer_close.ico_layer'
    LAYER = '//div[@class="b-layer__wrapper3"]'
    ## Upload
    #  Select
    FILE_INPUT = '//input[@class="layer_upload__controls__input"]'
    DIR_NAME = os.path.dirname(__file__) + "/files_for_upload"
    FILE_NAME = "/test.png"
    FILE_IN_CLOUD = '//*[@data-id="' + FILE_NAME + '"]'
    # Drag and drop
    DROP_ZONE = '//input[@class="drop-zone__input"]'
    FILE_NAME_D = "/test2.png"
    FILE_IN_CLOUD_D = '//*[@data-id="' + FILE_NAME_D + '"]'
    
    def load_form(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FORM))
        )

    def load_close(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE))
        )

    def load_layer(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LAYER))
        )

    def close_by_layer(self):
        self.driver.find_element_by_xpath(self.LAYER).click()

    def close_by_x(self):
        self.driver.find_element_by_xpath(self.CLOSE).click()

    def input_file(self):
        self.driver.find_element_by_xpath(self.FILE_INPUT).send_keys(self.DIR_NAME + self.FILE_NAME)

    def check_upload(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FILE_IN_CLOUD))
        )

    def drop_zone(self):
        self.driver.find_element_by_xpath(self.DROP_ZONE).send_keys(self.DIR_NAME + self.FILE_NAME_D)

    def check_drop(self):
        return WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, self.FILE_IN_CLOUD_D))
        )
