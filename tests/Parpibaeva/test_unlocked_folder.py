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

    def tearDown(self):
        self.driver.quit()

    def test_create_folder(self):
        sidebar = self.main_page.sidebar

        folder_create = self.main_page.folder_create
        folder_create.create_folder(self.FOLDER_NAME)

        self.assertTrue(sidebar.is_folder_created(
            self.FOLDER_NAME), "Folder not found after it was created")

        sidebar.delete_folder_by_name(self.FOLDER_NAME)
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    def test_create_nested_folder(self):
        sidebar = self.main_page.sidebar

        folder_create = self.main_page.folder_create
        folder_create.create_folder_in_inbox(self.FOLDER_NAME)

        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME),
                        "Nested folder not found after it was created")
        self.assertTrue(sidebar.is_folder_nested(
            self.FOLDER_NAME), "Folder is not nested")

        sidebar.delete_folder_by_name(self.FOLDER_NAME)
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")
