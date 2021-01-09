# -*- coding: utf-8 -*-
import os
import unittest
from casses.base.BaseTest import BaseTest
from pages.FoldersPage import FoldersPage
from pages.UpdateFolderPage import UpdateFolderPage
from pages.UpdatePasswordPage import UpdatePasswordPage
from steps.FoldersSteps import FoldersSteps


class UpdateFolderFormTest(BaseTest, unittest.TestCase):
    def setUp(self) -> None:
        super(UpdateFolderFormTest, self).setUp()

        self.main_page_folders = FoldersPage(self.driver)
        self.update_folder = UpdateFolderPage(self.driver)
        self.update_password = UpdatePasswordPage(self.driver)
        self.folderSteps = FoldersSteps(self.driver)

        self.__folder_name = "folder"
        self.__folderPasswordContext = {
            'folder_password': 'qwertyuiop',
            'folder_re_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

        self.folderSteps.add_folder(self.__folder_name, 'Входящие')
        self.folderSteps.wait_folder(self.__folder_name)
        self.go_to_main_folders()
        self.main_page_folders.click_pencil_icon()
        self.update_folder.fill_checkbox({"password": True})
        self.update_folder.save_changes()

    def tearDown(self) -> None:
        try:
            self.folderSteps.delete_folder(self.__folder_name)
            self.go_to_main_folders()
        finally:
            super(UpdateFolderFormTest, self).tearDown()

    def go_to_main_folders(self):
        self.main_page_folders.open(
            self.main_page_folders.BASE_URL + self.main_page_folders.PATH
        )

    def test_short_password(self):
        context = self.__folderPasswordContext.copy()
        context["folder_password"] = "ps"
        context["folder_re_password"] = "ps"
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidPassword"]
        )

    def test_invalid_re_password(self):
        context = self.__folderPasswordContext.copy()
        context["folder_re_password"] = context["folder_password"] + "text"
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidRePassword"]
        )

    def test_missing_secret_question(self):
        context = self.__folderPasswordContext.copy()
        context["question"] = ""
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidSecretQuestion"]
        )

    def test_missing_secret_question_answer(self):
        context = self.__folderPasswordContext.copy()
        context["question_answer"] = ""
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidSecretQuestionAnswer"]
        )

    def test_invalid_current_password(self):
        context = self.__folderPasswordContext.copy()
        context["current_password"] = ""
        self.update_password.set_password(context)
        self.assertTrue(
            self.update_password.get_password_form_errors["invalidUserPassword"]
        )

    def test_close_update_folder_form(self):
        context = self.__folderPasswordContext.copy()
        context["current_password"] = ""
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.close())

    def test_cancel_update_folder_form(self):
        context = self.__folderPasswordContext.copy()
        context["current_password"] = ""
        self.update_password.set_password(context)
        self.assertTrue(self.update_password.back())

    def test_valid_update_folder_form(self):
        context = self.__folderPasswordContext.copy()
        self.update_password.set_password(context)
        self.assertTrue(self.main_page_folders.click_pencil_icon())
        self.update_folder.fill_checkbox({"password": False})
        self.update_password.update_password_steps.set_current_password(
            context["current_password"]
        )
        self.update_password.update_password_steps.save()
