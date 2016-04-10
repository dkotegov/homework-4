# -*- coding: utf-8 -*-
# from page_objects import *
from pages import *
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote


class TestCase(unittest.TestCase):
    def defaultSetUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class BaseTestCase(TestCase):
    def setUp(self):
        self.defaultSetUp()
        self.login()
        self.home_page = HomePage(self.driver)

    def login(self):
        USEREMAIL = 'selenium.panichkina'
        PASSWORD = os.environ['HW4PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.enter.go()
        auth_form = auth_page.form
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit.go()

    def click(self, btn):
        btn.is_clickable(self)
        btn.do_click(self)
        btn.check_click(self)

    def init(self):
        self.home_page.upload.go()
        self.upload_form = self.home_page.form


class AuthTest(BaseTestCase):
    USEREMAIL = 'selenium.panichkina'
    USERDOMAIN = '@mail.ru'
    USERNAME = USEREMAIL + USERDOMAIN

    def test(self):
        user_name = self.home_page.user_name.get()
        self.assertEqual(self.USERNAME, user_name)


class CloseTest(BaseTestCase):

    def test_for_X(self):
        self.init()
        # Действия теста
        self.upload_form.close.go()


class UploadTest(BaseTestCase):
    file1 = "test.png"
    file2 = "test2.png"

    def delete_file(self, filename):
        self.home_page.select_file(filename)
        self.home_page.toolbar_buttons.delete.go()
        self.home_page.toolbar_buttons.delete_window.delete_submit.go()

    def test_for_select(self):
        file = self.file1
        self.init()
        self.upload_form.input_file.go(file)
        self.delete_file(file)

    def test_for_drop(self):
        file = self.file2
        self.init()
        self.upload_form.drag_and_drop.go(file)
        self.delete_file(file)


# class DeleteTest(BaseTestCase): #TODO проверить есть ли что удалять
#     def test_delete_all(self):
#         # Подготовка
#         buttons = self.home_page.toolbar_buttons
#
#         if not buttons.cloud_is_empty():
#         # self.assertFalse(buttons.cloud_is_empty())
#             buttons.checkbox.go()
#             self.assertTrue(buttons.cloud_is_empty())
#         # toolbar_group.load_page()
#         # # Действия теста
#         # toolbar_group.select_all()
#         # toolbar_group.start_remove_dialog()
#         # toolbar_group.load_dialog()
#         # toolbar_group.remove()
#         # # Проверка
#         # self.assertTrue(toolbar_group.check_delete(), "Delete Fail")