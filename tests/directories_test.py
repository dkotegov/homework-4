import os
import unittest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

import utils
from Auth import AuthPage
from Home import HomePage


class DirectoryTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = utils.get_remote_driver(browser)

        LOGIN = 'alexersh.testing'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_create_directory(self):
        dir_name = "directory_test"

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.utils.close_banner_if_exists()

        home_page.folders.create_folder(dir_name)

        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(dir_name))

        home_page.utils.close_mini_banner_if_exists()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)

        home_page.folders.delete_folder()
        home_page.open()

    def test_create_subdirectory(self):
        dir_name = "directory_test"
        subdir_name = "subdirectory_test"
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.utils.close_banner_if_exists()
        home_page.folders.create_folder(dir_name)
        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(dir_name))
        home_page.utils.close_mini_banner_if_exists()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)

        home_page.folders.create_folder(subdir_name)
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)
        self.assertTrue(home_page.folders.check_folder_exists(subdir_name))
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name + "/" + subdir_name)
        home_page.folders.delete_folder()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)
        home_page.folders.delete_folder()
