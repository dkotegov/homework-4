import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.account import AccountPage
from pages.profile import ProfilePage


class ChangePhotoErrorTest(unittest.TestCase):
    ERROR = 'Этот формат файла не поддерживается. Загрузите файл в JPG, PNG, GIF или BMP.'
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

        self.assertEqual(self.ERROR,  profile_steps.photo_error())
