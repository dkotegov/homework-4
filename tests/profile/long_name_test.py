import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile_steps import ProfileSteps
from tests.base_test import BaseTest


class NameTest(BaseTest):
    LONG_NAME = "i love testing i love testing i love testing i love testing"
    LONG_STRING_ERROR = 'Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов'


    def test(self):
        driver = self.driver
        AuthSteps(driver).auth()

        profile_steps = ProfileSteps(self.driver)
        profile_steps.open()
        profile_steps.set_name(self.LONG_NAME)
        profile_steps.save()

        self.assertEqual(self.LONG_STRING_ERROR, profile_steps.name_error_message())