# -*- coding: utf-8 -*-
import os
import unittest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

import utils
from Auth import AuthPage
from Home import HomePage


class CreatingDocumentsTest(unittest.TestCase):
    DOC_NAME = 'Новый документ.docx'
    PRES_NAME = 'Новая презентация.pptx'
    TABLE_NAME = 'Новая таблица.xlsx'

    def setUp(self):
        self.driver = utils.standard_set_up_auth()

    def tearDown(self):
        utils.standard_tear_down_cleanup(self.driver)

    def test_create_doc(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.utils.close_banner_if_exists()

        home_page.creating_documents.create_simple_document()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.DOC_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.DOC_NAME))
        home_page.utils.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()

    def test_create_pres(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.utils.close_banner_if_exists()
        home_page.utils.close_mini_banner_if_exists()
        home_page.creating_documents.create_presentation()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.PRES_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.PRES_NAME))
        home_page.utils.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()

    def test_create_table(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.utils.close_banner_if_exists()
        home_page.creating_documents.create_table()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.TABLE_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.TABLE_NAME))
        home_page.utils.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()
