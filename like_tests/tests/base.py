# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from like_tests.elements.user.pages import UserPage
from like_tests.elements.photo.components import *
from like_tests.elements.photo.pages import *


class BaseTest(unittest.TestCase):
    IMPLICIT_TIMEOUT = 5

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(self.IMPLICIT_TIMEOUT)
        self.user_page = UserPage(self.driver)
        self.user_page.open()
        self.user_page.login_1()

    def tearDown(self):
        self.driver.quit()


class BasePhotoTest(BaseTest):
    PHOTO_PATH = os.path.join(os.getcwd(), "uploads/lion.jpeg")

    def setUp(self):
        super(BasePhotoTest, self).setUp()
        self.photo = AlbumPage(self.driver).load_photo(self.PHOTO_PATH).photo

       # AvatarUploadButton(self.driver).click()

    def tearDown(self):
        # todo login u_1
        photo_page = PhotoPage(self.driver, self.photo.url)
        photo_page.open()
        photo_page.delete_photo()
        super(BasePhotoTest, self).tearDown()


