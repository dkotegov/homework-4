import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile import ProfileSteps


class BmpPhotoTest(unittest.TestCase):
    PHOTO = 'tests/testing_pics/photo.BMP'

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
        AuthSteps(driver).auth()

        profile_steps = ProfileSteps(self.driver)
        profile_steps.open()
        profile_steps.upload_photo_button()
        profile_steps.choose_photo(self.PHOTO)
        profile_steps.save_photo()
        profile_steps.save()

        assert "No results found." not in driver.page_source
