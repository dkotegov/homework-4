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
        sidebar.clear_trash()
        sidebar.create_new_dir()
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.click_more_settings()
        folder_create.click_select_parent_inbox()
        folder_create.select_parent_inbox()
        folder_create.submit()

    def tearDown(self):
        MainPage(self.driver).sidebar.clear_trash()
        self.driver.quit()

    def test(self):
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
        self.assertTrue(isFolderDeleted)
        main_page.redirectToQa()
        sidebar.go_to_trash()
        mailFromInTrash = letters.get_mail_from()
        mailTextInTrash = letters.get_mail_text()
        mailTimeInTrash = letters.get_mail_time()
        self.assertEqual(mailFrom, mailFromInTrash)
        self.assertEqual(mailText, mailTextInTrash)
        self.assertEqual(mailTime, mailTimeInTrash)
