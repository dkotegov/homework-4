import os
import unittest

from steps.FoldersSteps import FoldersSteps
from casses.Base.BaseTest import BaseTest


class InvalidFolderPasswordFormTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(InvalidFolderPasswordFormTest, self).setUp()

        self.folderSteps = FoldersSteps(self.driver)
        self.__folder_name = 'folder'
        self.__folder_password_context = {
            'folder_password': 'qwertyuiop',
            'folder_re_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

    def test_short_password(self):
        context = self.__folder_password_context.copy()
        context['folder_password'] = 'ps'
        context['folder_re_password'] = 'ps'
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_long_password(self):
        context = self.__folder_password_context.copy()
        context['folder_password'] = 'ps' * 32
        context['folder_re_password'] = 'ps' * 32
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_password_started_with_space(self):
        context = self.__folder_password_context.copy()
        context['folder_password'] = ' ' + context['password']
        context['folder_re_password'] = ' ' + context['password']
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_password_ended_with_space(self):
        context = self.__folder_password_context.copy()
        context['folder_password'] = context['password'] + ' '
        context['folder_re_password'] = context['password'] + ' '
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_invalid_password(self):
        context = self.__folder_password_context.copy()
        context['folder_password'] = '@#$%^&*()askdl'
        context['folder_re_password'] = context['password']
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_invalid_re_password(self):
        context = self.__folder_password_context.copy()
        context['folder_re_password'] = context['password'] + 'text'
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidRePassword'])

    def test_missing_secret_question(self):
        context = self.__folder_password_context.copy()
        context['question'] = ''
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidSecretQuestion'])

    def test_missing_secret_question_answer(self):
        context = self.__folder_password_context.copy()
        context['question_answer'] = ''
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidSecretQuestionAnswer'])

    def test_invalid_current_password(self):
        context = self.__folder_password_context.copy()
        context['current_password'] = ''
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidUserPassword'])
