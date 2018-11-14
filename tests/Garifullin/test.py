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

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.click_to_inbox()

        #  create a simple folder
        #  begin
        sidebar.create_new_dir()
        folder_create = main_page.folder_create
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.submit()
        folder_name = sidebar.get_text_by_folder_name(self.FOLDER_NAME)
        self.assertEqual(self.FOLDER_NAME, folder_name)
        #  end
        
        sidebar.clear_trash()

        letters = main_page.letters

        #  delete a folder and then check letters in a trash
        #  begin
        mailFrom = letters.get_mail_from()
        mailText = letters.get_mail_text()
        mailTime = letters.get_mail_time()
        letters.move_letters_to_folder(self.FOLDER_NAME)
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted)
        main_page.redirectToQa()
        sidebar.click_to_inbox()
        sidebar.go_to_trash()
        mailFromInTrash = letters.get_mail_from()
        mailTextInTrash = letters.get_mail_text()
        mailTimeInTrash = letters.get_mail_time()
        self.assertEqual(mailFrom, mailFromInTrash)
        self.assertEqual(mailText, mailTextInTrash)
        self.assertEqual(mailTime, mailTimeInTrash)
        #  end

        # import time
        # time.sleep(10)