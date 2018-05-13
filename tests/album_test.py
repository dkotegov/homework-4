# -*- coding: utf-8 -*-

import os
import time

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.auth_page import AuthPage
from tests.pages.user_album_edit_page import UserAlbumEditPage
from tests.pages.user_album_page import UserAlbumPage


class AlbumTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def test_create_album(self):
        self.auth()

        create_album_page = UserAlbumEditPage(self.driver)
        create_album_page.open()
        create_form = create_album_page.form
        album_name = 'Test album #{}'.format(time.time())
        create_form.set_name(album_name)
        create_form.submit()

        album = UserAlbumPage(self.driver).empty_album_content
        self.assertEqual(album_name, album.title)
