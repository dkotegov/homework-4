import unittest

from steps.FoldersSteps import FoldersSteps
from casses.base.BaseTest import BaseTest


class CloseFolderFormTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(CloseFolderFormTest, self).setUp()
        self.__folder_steps = FoldersSteps(self.driver)
        self.__folder_steps.folders_page.open()
        self.__folder_steps.folders_page.add_folder.open()

    def test_close_add_folder_form(self):
        """ Проверка закрытия формы добавления папки с помощью крестика """

        self.__folder_steps.folders_page.add_folder.close()
        self.assertFalse(self.__folder_steps.folders_page.add_folder.form_opened)

    def test_cancel_add_folder_form(self):
        """ Проверка закрытия формы добавления папки с помощью кнопки отмена """

        self.__folder_steps.folders_page.add_folder.cancel()
        self.assertFalse(self.__folder_steps.folders_page.add_folder.form_opened)
