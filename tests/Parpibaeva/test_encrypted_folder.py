import unittest
import os

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    FOLDER_NAME = "Test_Nadya"
    FOLDER_NAME_NESTED = "Test_Nadya_Nested"
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
        # CREATE LOCKED FOLDER
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        folder_create = main_page.folder_create
        sidebar.waitForVisible()
        main_page.redirectToQa()
        sidebar.create_new_dir()
        folder_create.set_name(self.FOLDER_NAME)
        folder_create.click_more_settings()
        folder_create.click_set_password()
        folder_create.submit()
        folder_create.set_password(self.FOLDER_PASSWORD)
        folder_create.set_password_repeat(self.FOLDER_PASSWORD)
        folder_create.set_question(self.FOLDER_PASSWORD)
        folder_create.set_answer(self.FOLDER_PASSWORD)
        folder_create.set_user_password(self.PASSWORD)
        folder_create.submit()

    def tearDown(self):
        self.driver.refresh()
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        if sidebar.is_folder_locked():
            sidebar.click_unlock_folder()
            folder_unlock = main_page.folder_unlock
            folder_unlock.set_password(self.FOLDER_PASSWORD)
            folder_unlock.submit()
            sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_delete()
        sidebar.submit_delete()
        self.driver.quit()

    def test_create_encrypted_folder(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME),
                        "Encrypted folder not found after it was created")

    def test_create_nested_folder_in_encrypted_folder(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_block_folder()

        sidebar.create_new_dir()
        folder_create = main_page.folder_create
        folder_create.set_name(self.FOLDER_NAME_NESTED)
        folder_create.click_more_settings()
        folder_create.click_select_parent_inbox()
        folder_create.select_parent_inbox_folder_with_password()
        folder_create.submit()

        folder_unlock = main_page.folder_unlock
        folder_unlock.set_password(self.FOLDER_PASSWORD)
        folder_unlock.submit()

        folder_create = main_page.folder_create
        folder_create.submit()
        self.assertTrue(sidebar.is_folder_created(self.FOLDER_NAME_NESTED),
                        "Nested folder not found after it was created")

        main_page.redirectToQa()
        sidebar.open_folder_wrapper()
        sidebar.right_click_by_folder(self.FOLDER_NAME_NESTED)
        sidebar.click_delete()
        sidebar.submit_delete()

    def test_lock_encrypted_folder(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_block_folder()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        self.assertTrue(sidebar.is_folder_locked(), "Folder 'unlock' option not found in menu after it was locked")

        sidebar.click_unlock_folder()
        folder_unlock = main_page.folder_unlock
        self.assertTrue(folder_unlock.is_created(), "Unlock folder window didn't appear")
        folder_unlock.set_password(self.FOLDER_PASSWORD)
        folder_unlock.submit()

    # folder is unlocked by default, we need to block it and unlock again to test anything
    def test_unlock_encrypted_folder(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_block_folder()
        sidebar.right_click_by_folder(self.FOLDER_NAME)
        sidebar.click_unlock_folder()
        folder_unlock = main_page.folder_unlock
        folder_unlock.set_password(self.FOLDER_PASSWORD)
        folder_unlock.submit()

        sidebar.right_click_by_folder(self.FOLDER_NAME)
        self.assertTrue(sidebar.is_folder_unlocked(),
                        "Folder 'lock' option not found in menu after it was unlocked ")
