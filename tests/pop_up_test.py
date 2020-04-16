import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.account import AccountPage
from pages.profile import ProfilePage


class PopUpTest(unittest.TestCase):
    PHOTO = 'tests/testing_pics/test.txt'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        driver = self.driver
        auth_page = AccountPage(driver)
        auth_page.open()
        auth_page.auth()

        profile_page = ProfilePage(driver)
        profile_page.open()
        profile_steps = profile_page.steps
        profile_steps.upload_photo_button()
        profile_steps.choose_photo(self.PHOTO)
        profile_steps.cross_pop_up()

        assert "No results found." not in driver.page_source