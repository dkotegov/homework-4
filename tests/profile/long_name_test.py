import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile import ProfileSteps


class NameTest(unittest.TestCase):
    LONG_NAME = "i love testing i love testing i love testing i love testing"
    LONG_STRING_ERROR = 'Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов'

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
        profile_steps.set_name(self.LONG_NAME)
        profile_steps.save()

        self.assertEqual(self.LONG_STRING_ERROR, profile_steps.name_error_message())