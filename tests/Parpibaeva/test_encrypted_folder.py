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

    def tearDown(self):
        self.driver.quit()

    def test_create_encrypted_folder(self):
        folder_create = self.main_page.folder_create
        folder_create.create_folder_with_password(self.FOLDER_NAME, self.FOLDER_PASSWORD, self.PASSWORD)

        sidebar = self.main_page.sidebar
        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME),
                        "Encrypted folder not found after it was created")

        sidebar.delete_folder_by_name(self.FOLDER_NAME)
        # reload page for folder to disappear
        self.main_page._redirect_to_qa()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    def test_create_nested_folder_in_encrypted_folder(self):
        folder_create = self.main_page.folder_create
        folder_create.create_folder_with_password(self.FOLDER_NAME, self.FOLDER_PASSWORD, self.PASSWORD)

        sidebar = self.main_page.sidebar
        sidebar.block_folder_by_name(self.FOLDER_NAME)

        folder_create.create_nested_folder_in_encrypted_folder(self.main_page, self.FOLDER_NAME_NESTED,
                                                               self.FOLDER_NAME, self.FOLDER_PASSWORD)

        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME_NESTED),
                        "Nested folder not found after it was created")

        self.main_page._redirect_to_qa()
        sidebar.open_folder_wrapper()

        # delete nested
        sidebar.delete_folder_by_name(self.FOLDER_NAME_NESTED)
        # reload page for folder to disappear
        self.main_page._redirect_to_qa()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME_NESTED)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

        # delete upper level
        sidebar.delete_folder_by_name(self.FOLDER_NAME)
        # reload page for folder to disappear
        self.main_page._redirect_to_qa()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    def test_lock_encrypted_folder(self):
        folder_create = self.main_page.folder_create
        folder_create.create_folder_with_password(self.FOLDER_NAME, self.FOLDER_PASSWORD, self.PASSWORD)

        sidebar = self.main_page.sidebar
        sidebar.block_folder_by_name(self.FOLDER_NAME)

        sidebar.right_click_by_folder(self.FOLDER_NAME)
        self.assertTrue(sidebar.is_folder_locked(
        ), "Folder 'unlock' option not found in menu after it was locked")

        sidebar.click_unlock_folder()
        folder_unlock = self.main_page.folder_unlock
        self.assertTrue(folder_unlock.is_created(),
                        "Unlock folder window didn't appear")
        folder_unlock.set_password(self.FOLDER_PASSWORD)
        folder_unlock.submit()

        sidebar.delete_folder_by_name(self.FOLDER_NAME)
        # reload page for folder to disappear
        self.main_page._redirect_to_qa()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    # folder is unlocked by default,
    # we need to block it and unlock again to test anything
    def test_unlock_encrypted_folder(self):
        folder_create = self.main_page.folder_create
        folder_create.create_folder_with_password(self.FOLDER_NAME, self.FOLDER_PASSWORD, self.PASSWORD)

        sidebar = self.main_page.sidebar
        sidebar.block_folder_by_name(self.FOLDER_NAME)

        folder_unlock = self.main_page.folder_unlock
        folder_unlock.unlock_folder(self.FOLDER_NAME, self.FOLDER_PASSWORD)

        sidebar.right_click_by_folder(self.FOLDER_NAME)
        self.assertTrue(sidebar.is_folder_unlocked(),
                        '''Folder "lock" option not found in 
                        menu after it was unlocked'''
                        )

        sidebar.delete_folder_by_name(self.FOLDER_NAME)
        # reload page for folder to disappear
        self.main_page._redirect_to_qa()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")
