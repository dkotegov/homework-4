# -*- coding: utf-8 -*-
import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage
from tests.pages.old_settings_folders_page import SettingsFolders

from selenium.webdriver import DesiredCapabilities, Remote


class FolderDeleteTests(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME1 = '_TEST_DIR1'
    FOLDER_NAME2 = '_TEST_DIR2'
    FOLDER_NAME3 = '_TEST_DIR3'
    FOLDER_NAME4 = '_TEST_DIR4'
    FOLDER_NAME5 = '_TEST_DIR5'
    FOLDER_NAME_CHILD1 = '_TEST_DIR_C1'
    FOLDER_PASSWORD = '1234'
    TRASH_FOLDER = 'Корзина'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)  # Авторизация
        auth_page.form.authorize(self.USEREMAIL, self.PASSWORD)
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_delete_unlocked_folder(self):
        sidebar = self.main_page.sidebar
        letters = self.main_page.letters
        folder_create = self.main_page.folder_create

        folder_create.create_folder_with_password(
            self.FOLDER_NAME1, self.FOLDER_PASSWORD, self.PASSWORD)
        sidebar.click_by_folder(self.FOLDER_NAME1)

        sidebar.click_to_inbox()
        mailFrom = letters.get_mail_from()
        mailText = letters.get_mail_text()
        mailTime = letters.get_mail_time()

        letters.move_letter_to_folder(self.FOLDER_NAME1)
        sidebar.clear_trash()
        # папка иногда не исчезает со страницы после удаления
        # (видимо баг в почте)
        sidebar.delete_folder_by_name(self.FOLDER_NAME1)

        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME1)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

        sidebar.go_to_folder(self.TRASH_FOLDER)
        mailFromInTrash = letters.get_mail_from()
        mailTextInTrash = letters.get_mail_text()
        mailTimeInTrash = letters.get_mail_time()
        self.assertEqual(mailFrom, mailFromInTrash,
                         '''Mail sender in letter from trash doesn't equal
                         with mail sender from letter in a deleted folder''')
        self.assertEqual(mailText, mailTextInTrash,
                         '''Text in letter from trash doesn't equal
                          with text from letter in a deleted folder''')
        self.assertEqual(mailTime, mailTimeInTrash,
                         '''Time in letter from trash doesn't equal
                          with time from letter in a deleted folder''')
        self.main_page.sidebar.clear_trash()

    def test_delete_subdir_context_menu(self):
        sidebar = self.main_page.sidebar
        folder_create = self.main_page.folder_create

        folder_create.create_folder_in_inbox(self.FOLDER_NAME2)
        sidebar.click_by_folder(self.FOLDER_NAME2)

        sidebar.delete_folder_by_name(self.FOLDER_NAME2)
        sidebar.click_to_inbox()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME2)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    def test_delete_subdir_old_menu(self):
        folders_setting_page_old = SettingsFolders(self.driver)
        sidebar = self.main_page.sidebar
        folder_settings = folders_setting_page_old.settings_form
        folder_create = self.main_page.folder_create

        folder_create.create_folder_in_inbox(self.FOLDER_NAME3)

        folders_setting_page_old.open()
        folder_settings.delete_my_folder()
        self.main_page._redirect_to_qa()
        sidebar.click_to_inbox()
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME3)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    def test_delete_locked_folder(self):
        sidebar = self.main_page.sidebar
        folder_unlock = self.main_page.folder_unlock
        folder_create = self.main_page.folder_create

        folder_create.create_folder_with_password(
            self.FOLDER_NAME4, self.FOLDER_PASSWORD, self.PASSWORD)
        sidebar.block_folder_by_name(self.FOLDER_NAME4)

        self.main_page._redirect_to_qa()
        sidebar.click_to_inbox()
        try_delete = sidebar.try_delete_folder(self.FOLDER_NAME4)
        self.assertFalse(
            try_delete, "Folder was deleted. Must be protected.")

        folder_unlock.unlock_folder(self.FOLDER_NAME4, self.FOLDER_PASSWORD)
        self.main_page._redirect_to_qa()
        sidebar.click_to_inbox()
        sidebar.delete_folder_by_name(self.FOLDER_NAME4)
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME4)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")

    def test_delete_folder_with_subdir(self):
        sidebar = self.main_page.sidebar
        folder_create = self.main_page.folder_create

        folder_create.create_folder(self.FOLDER_NAME5)
        sidebar.click_by_folder(self.FOLDER_NAME5)
        folder_create.create_folder_with_subfolder(
            self.FOLDER_NAME5, self.FOLDER_NAME_CHILD1)

        self.main_page._redirect_to_qa()
        sidebar.click_to_inbox()
        try_delete = sidebar.try_delete_folder(self.FOLDER_NAME5)
        self.assertFalse(
            try_delete, "Folder was deleted. Must be protected.")

        sidebar.delete_folder_by_name(self.FOLDER_NAME_CHILD1)
        sidebar.click_by_folder(self.FOLDER_NAME5)
        sidebar.delete_folder_by_name(self.FOLDER_NAME5)
        isFolderDeleted = sidebar.is_folder_deleted(self.FOLDER_NAME5)
        self.assertTrue(isFolderDeleted, "Folder wasn't deleted")
