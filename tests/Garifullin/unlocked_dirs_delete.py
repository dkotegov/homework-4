# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote

class UnlockedFolderDeleteTest(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = '_TEST_DIR'
    FOLDER_PASSWORD = 'passw0rd'


    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        folder_create = main_page.folder_create

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
        folder_name = sidebar.get_text_by_folder_name(self.FOLDER_NAME)
        self.assertEqual(self.FOLDER_NAME, folder_name)
        sidebar.clear_trash()

    def tearDown(self):
        MainPage(self.driver).sidebar.clear_trash()
        self.driver.quit()

    def test_unlocked_dir_delete(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        letters = main_page.letters

        sidebar.click_to_inbox()
        mailFrom = letters.get_mail_from()
        mailText = letters.get_mail_text()
        mailTime = letters.get_mail_time()
        letters.move_letter_to_folder(self.FOLDER_NAME)
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted)
        main_page.redirectToQa()
        sidebar.go_to_trash()
        mailFromInTrash = letters.get_mail_from()
        mailTextInTrash = letters.get_mail_text()
        mailTimeInTrash = letters.get_mail_time()
        self.assertEqual(mailFrom, mailFromInTrash)
        self.assertEqual(mailText, mailTextInTrash)
        self.assertEqual(mailTime, mailTimeInTrash)
