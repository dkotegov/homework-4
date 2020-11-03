# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
from Auth import AuthPage
from Home import HomePage


class CreatingDocumentsTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    DOC_NAME = 'Новый документ.docx'
    PRES_NAME = 'Новая презентация.pptx'
    TABLE_NAME = 'Новая таблица.xlsx'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_create_doc(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()

        home_page.creating_documents.create_simple_document()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.DOC_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.DOC_NAME))
        home_page.banners.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()

    def test_create_pres(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.banners.close_mini_banner_if_exists()
        home_page.creating_documents.create_presentation()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.PRES_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.PRES_NAME))
        home_page.banners.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()

    def test_create_table(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.creating_documents.create_table()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.TABLE_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.TABLE_NAME))
        home_page.banners.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()