# -*- coding: utf-8 -*-
import os
import unittest
from casses.base.BaseTest import BaseTest
from pages.FoldersPage import FoldersPage
from pages.UpdateFolderPage import UpdateFolderPage
from pages.UpdatePasswordPage import UpdatePasswordPage
from steps.FoldersSteps import FoldersSteps


class UpdateFolderTest(BaseTest, unittest.TestCase):
    def setUp(self) -> None:
        super(UpdateFolderTest, self).setUp()
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

    def tearDown(self) -> None:
        self.folderSteps.delete_folder(self.__folder_name)
        self.go_to_main_folders()
        super(UpdateFolderTest, self).tearDown()

    def go_to_main_folders(self):
        self.main_page_folders.open(
            self.main_page_folders.BASE_URL + self.main_page_folders.PATH
        )

    def test_update_folder_name(self):
        self.assertTrue(self.update_folder.fill_name("newFolder"))
        self.__folder_name = "newFolder"

    def test_select_top_folder(self):
        self.assertTrue(self.update_folder.fill_nested_folder("high_level"))
        self.assertTrue(self.update_folder.save_changes())

    def test_update_nested_folder_incoming(self):
        self.update_folder.fill_nested_folder("incoming")
        self.assertTrue(self.update_folder.save_changes())

    def test_update_nested_folder_high_level(self):
        self.update_folder.fill_nested_folder("high_level")
        self.assertTrue(self.update_folder.save_changes())

    def test_update_nested_folder_drafts(self):
        self.update_folder.fill_nested_folder("drafts")
        self.assertTrue(self.update_folder.save_changes())