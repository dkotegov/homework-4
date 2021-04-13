import os
import time
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.folder_tests.src.auth_page import AuthPage
from tests.folder_tests.src.main_page import MainPage


class FolderTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        # browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)
        # user_name = auth_page.top_menu.get_username()
        # self.assertEqual(self.LOGIN + '@mail.ru', user_name)

        main_page = MainPage(self.driver)
        main_form = main_page.main_form

        folder_name = 'Добавленная папка'
        main_form.add_folder_popup()
        folder_form = main_page.add_folder_form
        folder_form.create_folder(folder_name)
        time.sleep(2)

        main_form.remove_folder_popup()
        folder_form_remove = main_page.remove_folder_form
        time.sleep(2)
        folder_form_remove.remove_folder(folder_name)
        time.sleep(2)
