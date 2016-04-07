# -*- coding: utf-8 -*-
from page_objects import *
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


def get_evironment():
    name_of_browser_var = 'HW4BROWSER'
    name_of_password_var = 'HW4PASSWORD'
    try:
        BROWSER = os.environ[name_of_browser_var]
        PASSWORD = os.environ[name_of_password_var]
        print BROWSER, PASSWORD
    except KeyError:
        print "Oops! I can not find a variable: " + name_of_browser_var + " or " + name_of_password_var


def login(self):
    USEREMAIL = 'selenium.panichkina'
    PASSWORD = os.environ['HW4PASSWORD']

    auth_page = AuthPage(self.driver)
    auth_page.open()
    auth_page.top_menu.open_form()
    auth_form = auth_page.form
    auth_form.load_form()
    auth_form.set_login(USEREMAIL)
    auth_form.set_password(PASSWORD)
    auth_form.submit()


class AuthTest(unittest.TestCase):
    USEREMAIL = 'selenium.panichkina'
    USERDOMAIN = '@mail.ru'
    USERNAME = USEREMAIL + USERDOMAIN
    PASSWORD = os.environ['HW4PASSWORD']

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.top_menu.open_form()
        auth_form = auth_page.form
        auth_form.load_form()
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        # Проверка
        home_page = HomePage(self.driver)
        user_name = home_page.top_menu.get_username()
        self.assertEqual(self.USERNAME, user_name)

        # home_page.top_menu.logout(self.driver)


def open_upload_form(self):
    home_page = HomePage(self.driver)
    home_page.toolbar_group.load_page()
    home_page.toolbar_group.open_form()
    upload_form = home_page.form
    upload_form.load_form()


class CloseTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        login(self)

    def tearDown(self):
        self.driver.quit()

    def test_for_X(self):
        # Подготовка
        home_page = HomePage(self.driver)
        home_page.toolbar_group.load_page()
        home_page.toolbar_group.open_form()
        upload_form = home_page.form
        upload_form.load_form()
        # Действия теста
        upload_form.load_close()
        upload_form.close_by_x()
        # Проверка

    def test_for_layer(self):
        # Подготовка
        home_page = HomePage(self.driver)
        home_page.toolbar_group.load_page()
        home_page.toolbar_group.open_form()
        upload_form = home_page.form
        upload_form.load_form()
        # Действия теста
        upload_form.load_layer()
        upload_form.close_by_layer()
        # Проверка
        #TODO проверка


class UploadTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        login(self)
        self.init()

    def tearDown(self):
        self.driver.quit()

    def init(self):
        home_page = HomePage(self.driver)
        home_page.toolbar_group.load_page()
        home_page.toolbar_group.open_form()
        self.upload_form = home_page.form
        self.upload_form.load_form()

    def test_for_select(self):
        # Подготовка
        # home_page = HomePage(self.driver)
        # home_page.toolbar_group.load_page()
        # home_page.toolbar_group.open_form()
        # upload_form = home_page.form
        # upload_form.load_form()
        # Действия теста
        self.upload_form.input_file()
        # Проверка
        self.assertTrue(self.upload_form.check_upload(), "Load file not found")

    def test_for_drop(self):
        # # Подготовка
        # home_page = HomePage(self.driver)
        # home_page.toolbar_group.load_page()
        # home_page.toolbar_group.open_form()
        # upload_form = home_page.form
        # upload_form.load_form()
        # Действия теста
        self.upload_form.drop_zone()
        # Проверка
        self.assertTrue(self.upload_form.check_drop(), "Load file not found")


class DeleteTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        login(self)

    def tearDown(self):
        self.driver.quit()

    def test_delete_all(self):
        # Подготовка
        home_page = HomePage(self.driver)
        toolbar_group = home_page.toolbar_group
        toolbar_group.load_page()
        # Действия теста
        toolbar_group.select_all()
        toolbar_group.start_remove_dialog()
        toolbar_group.load_dialog()
        toolbar_group.remove()
        # Проверка
        self.assertTrue(toolbar_group.check_delete(), "Delete Fail")