# -*- coding: utf-8 -*-
import os
import random
import string
import unittest
from enum import Enum

from selenium.webdriver import DesiredCapabilities, Remote

from casses.base.BaseTest import BaseTest
from pages.AuthPage import AuthPage
from pages.FoldersPage import FoldersPage
from pages.UpdateFolderPage import UpdateFolderPage
from pages.UpdatePasswordPage import UpdatePasswordPage
from steps.FoldersSteps import FoldersSteps


class FoldersTestSecond(BaseTest, unittest.TestCase):
    def setUp(self) -> None:
        browser = os.environ.get("BROWSER", "CHROME")
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

        LOGIN = os.environ["LOGIN"]
        PASSWORD = os.environ["PASSWORD"]

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

        self.main_page_folders = FoldersPage(self.driver)
        self.update_folder = UpdateFolderPage(self.driver)
        self.update_password = UpdatePasswordPage(self.driver)
        self.folderSteps = FoldersSteps(self.driver)

        self.folderSteps.add_folder('folder', 'Входящие')
        self.folderSteps.wait_folder('folder')

        self.__folderPasswordContext = {
            'folder_password': 'qwertyuiop',
            'folder_re_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }
        self.go_to_main_folders()

    def tearDown(self) -> None:
        self.folderSteps.delete_folder("folder")
        self.go_to_main_folders()
        self.driver.quit()

    def go_to_main_folders(self):
        self.main_page_folders.open(
            self.main_page_folders.BASE_URL + self.main_page_folders.PATH
        )

    def test_update_folder_name(self):
        self.main_page_folders.click_pencil_icon()
        is_filled = self.update_folder.fill_name("newFolder")
        self.assertTrue(is_filled)

    def test_select_top_folder(self):
        self.main_page_folders.click_pencil_icon()
        self.assertTrue(self.update_folder.fill_nested_folder("high_level"))
        status = self.update_folder.save_changes()
        self.assertTrue(status)

    def test_update_nested_folder(self):
        self.main_page_folders.click_pencil_icon()

        class EnumForDropList(Enum):
            a = "incoming"
            b = "high_level"
            c = "drafts"

        self.update_folder.fill_nested_folder(
            random.choice(list(EnumForDropList)).value
        )
        status = self.update_folder.save_changes()
        self.assertTrue(status)

    def test_short_password(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["folder_password"] = "ps"
        context["folder_re_password"] = "ps"
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidPassword"]
        )

    def test_invalid_re_password(self):
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["folder_re_password"] = context["folder_password"] + "text"
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidRePassword"]
        )

    def test_missing_secret_question(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["question"] = ""
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidSecretQuestion"]
        )

    def test_missing_secret_question_answer(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["question_answer"] = ""
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidSecretQuestionAnswer"]
        )

    def test_invalid_current_password(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["current_password"] = ""
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidUserPassword"]
        )

    def test_close_update_folder_form(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["current_password"] = ""
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.close())

    def test_cancel_update_folder_form(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        context["current_password"] = ""
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.back())

    def test_valid_update_folder_form(self):
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()
        context = self.__folderPasswordContext.copy()
        self.update_password.set_password(context)
        ok = self.main_page_folders.click_pencil_icon()
        self.assertTrue(ok)
        self.update_folder.fill_checkbox({"password": False})
        self.update_password.update_password_steps.set_current_password(
            context["current_password"]
        )
        self.update_password.update_password_steps.save()
