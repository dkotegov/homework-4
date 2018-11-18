# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage
from tests.pages.old_settings_folders_page import SettingsFolders
from selenium.webdriver import DesiredCapabilities, Remote

class SubFolderDeleteTest(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = '_TEST_DIR'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

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
        main_page.redirectToQa()
        sidebar.click_to_inbox()

    def tearDown(self):
        self.driver.quit()

    def test_subdir_old_menu(self):
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
        self.assertTrue(isFolderDeleted, "Folder wasn't created")

    def test_subdir_context_menu(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        letters = main_page.letters


        mailFrom = letters.get_mail_from()
        mailText = letters.get_mail_text()
        mailTime = letters.get_mail_time()
        letters.move_letter_to_folder(self.FOLDER_NAME)
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted, "Folder wasn't created")
        main_page.redirectToQa()
        sidebar.go_to_trash()
        mailFromInTrash = letters.get_mail_from()
        mailTextInTrash = letters.get_mail_text()
        mailTimeInTrash = letters.get_mail_time()
        self.assertEqual(mailFrom, mailFromInTrash, "Mail sender in letter from trash doesn't equal with mail sender from letter in a deleted folder")
        self.assertEqual(mailText, mailTextInTrash, "Text in letter from trash doesn't equal with text from letter in a deleted folder")
        self.assertEqual(mailTime, mailTimeInTrash, "Time in letter from trash doesn't equal with time from letter in a deleted folder")
