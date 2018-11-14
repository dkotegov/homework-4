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
    FOLDER_NAME_CHILD = 'Test_Timur_C'

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

        #  new
        #  prepare
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

        #  begin
        main_page.redirectToQa()
        sidebar.click_to_inbox()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        try_delete = sidebar.try_click_delete()
        self.assertFalse(try_delete)
        #  end

        
        #  cleaning
        sidebar.right_click_by_folder(self.FOLDER_NAME_CHILD)
        sidebar.click_delete()
        sidebar.submit_delete()
        main_page.redirectToQa()
        sidebar.click_to_inbox()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
