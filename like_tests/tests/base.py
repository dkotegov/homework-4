# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from like_tests.elements.user.pages import UserPage
from like_tests.elements.photo.components import PhotoUploadButton


class BaseTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.user_page = UserPage(self.driver)
        self.user_page.login()

    def tearDown(self):
        self.driver.quit()


class BasePhotoTest(BaseTest):

    def setUp(self):
        super(BasePhotoTest, self).setUp()
        PhotoUploadButton(self.driver).load_photo(os.path.join(os.getcwd(), "uploads/lion.jpeg"))

