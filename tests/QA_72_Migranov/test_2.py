# -*- coding: utf-8 -*-

import unittest
import os
import time
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote

class Test_2(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        main_page = MainPage(self.driver)

        sidebar = main_page.sidebar
        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.click_to_inbox()

        sidebar.clear_folder('Отправленные')
        sidebar.clear_trash()
        
        letters = main_page.letters
        
        letters.move_letter_to_folder('Корзина')
        letters.move_letter_to_folder('Корзина')

        sidebar.go_to_trash()

        letters_in_trash_expected = 2
        letters_in_trash_actual = len(letters.get_letters)
        
        self.assertEqual(
            letters_in_trash_expected, 
            letters_in_trash_actual, 
            'Letters in trash: expected: {}, actual: {}'.format(letters_in_trash_expected, letters_in_trash_actual)
        )

        main_page.logout.submit()

    def tearDown(self):
        sidebar = MainPage(self.driver).sidebar
        sidebar.clear_folder('Отправленные')
        sidebar.clear_folder('Корзина')

        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        main_page = MainPage(self.driver)

        sidebar = main_page.sidebar
        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.click_to_inbox()

        sidebar.go_to_trash()

        letters = main_page.letters
        topbar = main_page.topbar
        letters.move_all_letters_to_folder('Отправленные', topbar)

        sidebar.go_to_folder('Отправленные')

        letters_in_expected = 2
        letters_in_actual = len(letters.get_letters)
        
        self.assertEqual(
            letters_in_expected, 
            letters_in_actual, 
            'Letters in trash: expected: {}, actual: {}'.format(letters_in_expected, letters_in_actual)
        )


       
