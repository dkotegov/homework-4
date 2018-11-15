# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote

class FolderDeleteTest(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = 'Test_Timur'
    FOLDER_PASSWORD = 'passw0rd'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver')

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
        folder_create.click_more_settings()
        folder_create.click_set_password()
        folder_create.submit()
        folder_create.set_password(self.FOLDER_PASSWORD)
        folder_create.set_password_repeat(self.FOLDER_PASSWORD)
        folder_create.set_question(self.FOLDER_PASSWORD)
        folder_create.set_answer(self.FOLDER_PASSWORD)
        folder_create.set_user_password(self.PASSWORD)
        folder_create.submit()
        sidebar.click_by_folder(self.FOLDER_NAME)
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_block_folder()

    def tearDown(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        folder_unlock = main_page.forlder_unlock
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_unlock_folder()
        folder_unlock.set_password(self.FOLDER_PASSWORD)
        folder_unlock.submit()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        self.driver.quit()

    def test(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar

        main_page.redirectToQa()
        sidebar.click_to_inbox()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        try_delete = sidebar.try_click_delete()
        self.assertFalse(try_delete)
