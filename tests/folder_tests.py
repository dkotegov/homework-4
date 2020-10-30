import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from Auth import AuthPage
from Home import HomePage


class FolderTests(unittest.TestCase):
    def setUp(self) -> None:
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = 'alexersh.test'
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_create_and_delete_folder(self):
        FOLDER_NAME = "Folder"

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.folders.create_folder(FOLDER_NAME)

        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(FOLDER_NAME))

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + FOLDER_NAME)
        home_page.folders.delete_folder()

        home_page.open()
        self.assertFalse(home_page.folders.check_folder_exists(FOLDER_NAME))

    def test_create_and_delete_folder_inside_folder(self):
        FOLDER_NAME = "Folder"
        INNER_FOLDER_NAME = "Inside folder"

        home_page = HomePage(self.driver)
        home_page.open()

        # site redirects to created folder, so after this we would be on BASE_URL/PATH/<FOLDER_NAME>
        home_page.folders.create_folder(FOLDER_NAME)

        home_page.folders.create_folder(INNER_FOLDER_NAME)

        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(FOLDER_NAME))

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + FOLDER_NAME)
        self.assertTrue(home_page.folders.check_folder_exists(INNER_FOLDER_NAME))

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + FOLDER_NAME + '/' + INNER_FOLDER_NAME)
        home_page.folders.delete_folder()

        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + FOLDER_NAME)
        self.assertFalse(home_page.folders.check_folder_exists(INNER_FOLDER_NAME))
        home_page.folders.delete_folder()

        home_page.open()
        self.assertFalse(home_page.folders.check_folder_exists(FOLDER_NAME))