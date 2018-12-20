#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import time

from tests import get_webdriver, get_credentials, PageObject, LOGIN_PAGE_URL, FoldersActivities


class TestFoldersActivities(unittest.TestCase):
    # def __init__(self, arg=None):

    # def beforeAll(self):
        
    @classmethod
    def setUpClass(self):
        self.revert_data = []
        self.page = FoldersActivities()
        self.page.open(LOGIN_PAGE_URL)
        self.page.login()


    def test_same_name(self):
        result1 = self.page.create_folder_by_btn('0')
        if result1:
            self.revert_data.append(['0'])

        result2 = self.page.create_folder_by_btn('0')

        self.assertTrue(result1)
        self.assertFalse(result2)


    def test_diff_names(self):
        result1 = self.page.create_folder_by_btn('0')

        if result1:
            self.revert_data.append(['0'])

        result2 = self.page.create_folder_by_btn('1')

        if result2:
            self.revert_data.append(['1'])

        self.assertTrue(result1, result2)



    def test_creating_inside_folder(self):
        result1 = self.page.create_folder_by_btn('0')

        if result1:
            self.revert_data.append(['0'])

        result2 = self.page.create_folder_by_btn('1', '0')
        
        if result2:
            [['1', True]].extend(self.revert_data)

        self.page.delete_folder('1', True)

        self.assertTrue(result1, result2)



    def test_parent_similar_folder(self):
        result1 = self.page.create_folder_by_btn('0')

        if result1:
            self.revert_data.append(['0'])

        result2 = self.page.create_folder_by_btn('0', '0')
        
        if result2:
            [['0', True]].extend(self.revert_data)

        self.assertTrue(result1, result2)


    def test_parent_diff_folders(self):
        self.page.create_folder_by_btn('0')

        result1 = self.page.create_folder_by_btn('1', '0')

        if result1:
            [['1', True]].extend(self.revert_data)

        result2 = self.page.create_folder_by_btn('2', '0')

        if result2:
            [['2', True]].extend(self.revert_data)

        self.revert_data.append(['0'])


    def tearDown(self):
        for data in self.revert_data:
            self.page.delete_folder(*data)
            time.sleep(2)

        self.revert_data = []



    @classmethod
    def tearDownClass(self):
        self.page.close()
        self.driver.quit()
