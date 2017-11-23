# -*- coding: utf-8 -*-

import unittest

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities, Remote
from like_tests.elements.user.pages import *
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
        self.photo_url = AlbumPage(self.driver).load_photo(self.PHOTO_PATH).url

    def tearDown(self):
        self.user_page.open()
        try:
            self.user_page.open()
            username = self.user_page.user_header.get_username()
            assert(username == AuthPage.USER_LOGIN1)
        except AssertionError:
            self.user_page.logout()
            self.user_page.login_1()
        except WebDriverException:
            self.user_page.login_1()

        print(self.photo_url)
        photo_page = PhotoPage(self.driver, self.photo_url)
        photo_page.open()
        photo_page.delete_photo()
        super(BasePhotoTest, self).tearDown()


