import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile_steps import ProfileSteps
from tests.base_test import BaseTest


class NarrowPhotoTest(BaseTest):
    ERROR = 'Ширина и высота фото должны быть больше 160 пикселей'
    PHOTO = 'tests/testing_pics/narrow.png'


    def test(self):
        driver = self.driver
        AuthSteps(driver).auth()

        profile_steps = ProfileSteps(self.driver)
        profile_steps.open()
        profile_steps.upload_photo_button()
        profile_steps.choose_photo(self.PHOTO)

        self.assertEqual(self.ERROR, profile_steps.photo_size_error())
