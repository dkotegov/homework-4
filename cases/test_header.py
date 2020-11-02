import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.boards_page import BoardsPage
from pages.profile_page import ProfilePage

wait = WebDriverWait(webdriver, 10)

class HeaderTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        login_page = LoginPage(self.driver)
        login_page.open()
        login = os.environ.get('LOGIN')
        login_page.login_form.set_login(login)
        password = os.environ.get('PASSWORD')
        login_page.login_form.set_password(password)
        login_page.login_form.submit()

        boards_page = BoardsPage(self.driver)
        boards_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_open_profile(self):
        boards_page = BoardsPage(self.driver)
        boards_page.main_header.open_profile()

    def test_open_boards(self):
        profile_page = ProfilePage(self.driver)
        profile_page.main_header.open_boards()

    def test_open_notifications(self):
        boards_page = BoardsPage(self.driver)
        boards_page.main_header.open_notifications()

    def test_logout(self):
        boards_page = BoardsPage(self.driver)
        boards_page.main_header.logout()
