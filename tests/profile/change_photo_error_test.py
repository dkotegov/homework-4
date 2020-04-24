import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile_steps import ProfileSteps
from tests.base_test import BaseTest


class ChangePhotoErrorTest(BaseTest):
    ERROR = 'Этот формат файла не поддерживается. Загрузите файл в JPG, PNG, GIF или BMP.'
    PHOTO = 'tests/testing_pics/test.txt'

    def test(self):
        driver = self.driver
        AuthSteps(driver).auth()

        profile_steps = ProfileSteps(self.driver)
        profile_steps.open()
        profile_steps.upload_photo_button()
        profile_steps.choose_photo(self.PHOTO)

        self.assertEqual(self.ERROR,  profile_steps.photo_error())
