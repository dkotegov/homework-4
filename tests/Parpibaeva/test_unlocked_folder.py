import unittest
import os

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = "Test_Nadya"
    FOLDER_PASSWORD = "kek_lol"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        # self.driver = webdriver.Chrome('./chromedriver_mac')

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

    def tearDown(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        self.driver.quit()

    def test_create_folder(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.create_new_dir()
        folder_create = main_page.folder_create
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.submit()
        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME), "Folder not found after it was created")

    def test_create_nested_folder(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        folder_create = main_page.folder_create
        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.create_new_dir()
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.click_more_settings()
        folder_create.click_select_parent_inbox()
        folder_create.select_parent_inbox()
        folder_create.submit()
        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME), "Nested folder not found after it was created")
        self.assertTrue(sidebar.is_folder_nested(self.FOLDER_NAME), "Folder is not nested")
