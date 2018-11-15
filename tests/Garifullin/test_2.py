# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage
from tests.pages.old_settings_folders_page import SettingsFolders
from selenium.webdriver import DesiredCapabilities, Remote

class FolderDeleteTest(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = 'Test_Timur'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        main_page = MainPage(self.driver)
        folder_create = main_page.folder_create
        sidebar = main_page.sidebar
        
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
        folder_create.click_select_parent_inbox()
        folder_create.select_parent_inbox()
        folder_create.submit()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        main_page = MainPage(self.driver)
        folders_setting_page_old = SettingsFolders(self.driver)
        sidebar = main_page.sidebar
        folder_settings = folders_setting_page_old.settings_form

        folders_setting_page_old.open()
        folder_settings.click_delete()
        folder_settings.click_submit_delete()
        main_page.redirectToQa()
        sidebar.click_to_inbox()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted)
