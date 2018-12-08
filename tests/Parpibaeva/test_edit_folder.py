# -*- coding: utf-8 -*-

import unittest
import os

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = "Test_Nadya"
    FOLDER_NAME_EDITED = "Test_Nadya_Edited"
    FOLDER_NAME_NESTED = "Test_Nadya_Nested"
    FOLDER_PASSWORD = "kek_lol"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver_mac')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)  # Авторизация
        auth_page.form.authorize(self.USEREMAIL, self.PASSWORD)

        self.main_page = MainPage(self.driver)
        sidebar = self.main_page.sidebar
        sidebar.create_new_dir()
        folder_create = self.main_page.folder_create
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.submit()

    def tearDown(self):
        sidebar = self.main_page.sidebar
        if sidebar.is_folder_created(self.FOLDER_NAME):
            sidebar.right_click_by_folder(self.FOLDER_NAME)
        else:
            sidebar.right_click_by_folder(self.FOLDER_NAME_EDITED)
        sidebar.click_delete()
        sidebar.submit_delete()
        self.driver.quit()

    def test_edit_folder_name(self):
        sidebar = self.main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_edit()

        folder_edit = self.main_page.folder_edit
        folder_edit.clear_old_name()
        folder_edit.set_name(self.FOLDER_NAME_EDITED)
        folder_edit.submit()

        self.assertTrue(sidebar.is_folder_created(
            self.FOLDER_NAME_EDITED), "Folder not found after it was renamed")

    def test_edit_folder_nested(self):
        sidebar = self.main_page.sidebar

        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_edit()

        folder_edit = self.main_page.folder_edit
        folder_edit.click_select_parent_inbox()
        folder_edit.select_parent_inbox()
        folder_edit.submit()
        self.assertTrue(sidebar.is_folder_exists(self.FOLDER_NAME),
                        "Nested folder not found after it was created")
        self.assertTrue(sidebar.is_folder_nested(
            self.FOLDER_NAME), "Folder is not nested")
