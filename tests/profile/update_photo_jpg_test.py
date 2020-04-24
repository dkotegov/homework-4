import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.profile.profile import ProfilePage
from steps.auth.auth_steps import AuthSteps
from steps.profile.profile_steps import ProfileSteps
from tests.base_test import BaseTest


class JpgPhotoTest(BaseTest):
    PHOTO = 'tests/testing_pics/photo.JPG'


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
