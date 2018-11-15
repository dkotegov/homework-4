# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote

class FolderWithSubdirDeleteTest(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = '_TEST_DIR'
    FOLDER_NAME_CHILD = '_TEST_DIR_C'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        folder_create = main_page.folder_create

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.click_to_inbox()

        sidebar.create_new_dir()
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.submit()
        sidebar.click_by_folder(self.FOLDER_NAME)
        sidebar.create_new_dir()
        folder_create.set_name(self.FOLDER_NAME_CHILD)
        folder_create.click_more_settings()
        folder_create.click_select_parent_inbox()
        folder_create.select_parent_folder(self.FOLDER_NAME)
        folder_create.submit()
        sidebar.click_by_folder(self.FOLDER_NAME_CHILD)

    def tearDown(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME_CHILD)
        sidebar.click_delete()
        sidebar.submit_delete()
        main_page.redirectToQa()
        sidebar.click_to_inbox()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        self.driver.quit()

    def test_folder_with_subdir(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar

        main_page.redirectToQa()
        sidebar.click_to_inbox()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        try_delete = sidebar.try_click_delete()
        self.assertFalse(try_delete)
