# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def _wait_until_and_get_elem_by_xpath(self, elem):
        return WebDriverWait(self.driver, 120, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def _wait_for_url(self, url):
        return WebDriverWait(self.driver, 120, 0.1).until(EC.url_to_be(url))

    def _check_if_element_exists_by_xpath(self, elem):
        try:
            WebDriverWait(self.driver, 1, 0.1).until(EC.visibility_of_all_elements_located((By.XPATH, elem)))
        except TimeoutException:
            return False
        return True


class Page(object):
    BASE_URL = 'https://account.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    NEXT_BUTTON = '//button[@data-test-id="next-button"]'
    LOGIN_BUTTON = '//a[text()="Войти"]'

    def set_login(self, login):
        self._wait_until_and_get_elem_by_xpath(self.LOGIN).send_keys(login)

    def click_next(self):
        self._wait_until_and_get_elem_by_xpath(self.NEXT_BUTTON).click()

    def set_password(self, pwd):
        self._wait_until_and_get_elem_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self._wait_until_and_get_elem_by_xpath(self.SUBMIT).click()

    def wait_for_cookie(self):
        self._wait_for_url('https://e.mail.ru/inbox/?afterReload=1')


class Directories(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR = '//div[@data-name="createFolder"]'
    FOLDER_NAME_INPUT = '//input[@placeholder="Введите имя папки"]'
    SUBMIT_CREATE_FOLDER_BUTTON = '//div[@class="CreateNewFolderDialog__button--7S1Hs"][1]/button'
    DELETE_FOLDER_BUTTON = '//div[@data-name="remove"]'
    CONFIRM_DELETE_FOLDER_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'
    FOLDER_XPATH_BY_NAME = '//a[@data-qa-type="folder" and @data-qa-name="{}"]'

    def create_folder(self, folder_name):
        self._wait_until_and_get_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR).click()
        elem = self._wait_until_and_get_elem_by_xpath(self.FOLDER_NAME_INPUT)
        elem.clear()
        elem.send_keys(folder_name)
        self._wait_until_and_get_elem_by_xpath(self.SUBMIT_CREATE_FOLDER_BUTTON).click()

    def check_folder_exists(self, folder_name):
        return self._check_if_element_exists_by_xpath(self.FOLDER_XPATH_BY_NAME.format(folder_name))

    def open_folder(self, folder_url):
        self.driver.get(folder_url)

    def delete_folder(self):
        self._wait_until_and_get_elem_by_xpath(self.DELETE_FOLDER_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_FOLDER_BUTTON).click()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    def auth(self, login, password):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.form.set_login(login)
        auth_page.form.click_next()
        auth_page.form.set_password(password)
        auth_page.form.submit()
        auth_page.form.wait_for_cookie()


class Banners(Component):
    BANNER = '//div[@data-qa-modal]'
    MINI_BANNER = '//div[@class="PromoTooltip__root--2vPmD"]'
    CLOSE_MINI_BANNER_BUTTON = '//div[@class="PromoTooltip__close--3zFr1 PromoTooltip__closeLight--JBMkK"]'
    CLOSE_BANNER_BUTTON = '//*[local-name() = "svg" and @class="Dialog__close--1rKyk"]'

    def close_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_BANNER_BUTTON).click()

    def close_mini_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.MINI_BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_MINI_BANNER_BUTTON).click()


class HomePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home/'

    @property
    def folders(self):
        return Directories(self.driver)

    @property
    def banners(self):
        return Banners(self.driver)

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class DirectoryTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_create_directory(self):
        dir_name = "directory_test"

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()

        home_page.folders.create_folder(dir_name)

        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(dir_name))

        home_page.banners.close_mini_banner_if_exists()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)

        home_page.folders.delete_folder()
        home_page.open()

    def test_create_subdirectory(self):
        dir_name = "directory_test"
        subdir_name = "subdirectory_test"
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.folders.create_folder(dir_name)
        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(dir_name))
        home_page.banners.close_mini_banner_if_exists()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)

        home_page.folders.create_folder(subdir_name)
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)
        self.assertTrue(home_page.folders.check_folder_exists(subdir_name))
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name + "/" + subdir_name)
        home_page.folders.delete_folder()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)
        home_page.folders.delete_folder()
