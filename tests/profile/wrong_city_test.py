import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile_steps import ProfileSteps
from tests.base_test import BaseTest


class WrongCityTest(BaseTest):
    WRONG_CITY = 'QWERTY'
    CITY_ERROR = 'Проверьте название города'


    def test(self):
        driver = self.driver
        AuthSteps(driver).auth()

        profile_steps = ProfileSteps(self.driver)
        profile_steps.open()
        profile_steps.set_city(self.WRONG_CITY)
        profile_steps.save()

        self.assertEqual(self.CITY_ERROR, profile_steps.city_error())