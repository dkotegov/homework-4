# -*- coding: utf-8 -*-

import os
import time
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.mobile.auth_page import AuthPage
from tests.pages.mobile.user_album_edit_page import UserAlbumEditPage
from tests.pages.mobile.user_album_page import UserAlbumPage
from tests.pages.mobile.user_albums_page import UserAlbumsPage


class MobileAlbumCreateTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.album_url = None

        AuthPage(self.driver).auth(self.LOGIN, self.PASSWORD)

    def tearDown(self):
        if self.album_url:
            album_page = UserAlbumPage(self.driver)
            album_page.open_url(self.album_url)
            album_page.remove_album()

        self.driver.quit()

    def test_create_album(self):
        albums_page = UserAlbumsPage(self.driver)
        albums_page.open()
        albums_page.header.create_album()

        album_name = 'Created test album #{}'.format(time.time())
        create_form = UserAlbumEditPage(self.driver).form
        create_form.set_name(album_name)
        create_form.submit()

        album_page = UserAlbumPage(self.driver)
        album_page.parse_album_id()
        self.assertEqual(album_name, album_page.empty_album.title)

        self.album_url = album_page.current_url

        albums_page.open()
        self.assertTrue(albums_page.albums_list.includes(album_name))

    def test_long_album_name(self):
        album_name = 'L' * 51
        create_page = UserAlbumEditPage(self.driver)
        create_page.create_album(album_name)
        create_form = create_page.form
        self.assertTrue(create_form.is_name_error())

        album_name = 'L' * 50
        create_form.set_name(album_name)
        create_form.submit()

        album_page = UserAlbumPage(self.driver)
        self.assertEqual(album_name, album_page.empty_album.title)

        self.album_url = album_page.current_url

    def test_empty_album_name(self):
        create_page = UserAlbumEditPage(self.driver)
        create_page.create_album('')
        create_form = create_page.form
        self.assertTrue(create_form.is_name_error())

    def test_xss(self):
        album_name = '<h1 id="xss">XSS</h1>'
        UserAlbumEditPage(self.driver).create_album(album_name)

        album_page = UserAlbumPage(self.driver)
        self.album_url = album_page.current_url
        self.assertFalse(album_page.is_xss)

        albums_page = UserAlbumsPage(self.driver)
        albums_page.open()
        self.assertFalse(albums_page.is_xss)

    def test_album_shows(self):
        album_name = 'Best friends and colleagues'
        create_page = UserAlbumEditPage(self.driver)
        create_page.open()

        create_form = UserAlbumEditPage(self.driver).form
        create_form.set_name(album_name)
        self.assertEqual(1, create_form.shows_checkboxes_count)
        create_form.shows_all()
        self.assertEqual(2, create_form.shows_checkboxes_count)
        create_form.shows_friends()
        self.assertEqual(9, create_form.shows_checkboxes_count)
        create_form.shows_friends()
        self.assertEqual(2, create_form.shows_checkboxes_count)
        create_form.shows_friends()
        self.assertEqual(9, create_form.shows_checkboxes_count)
        create_form.shows_best_friends()
        create_form.shows_colleagues()
        create_form.submit()

        album_page = UserAlbumPage(self.driver)
        self.assertEqual(album_name, album_page.empty_album.title)

        self.album_url = album_page.current_url

        toolbar = album_page.toolbar
        toolbar.open()
        toolbar.edit()

        edit_form = UserAlbumEditPage(self.driver).form
        self.assertTrue(edit_form.is_shows_best_friends())
        self.assertTrue(edit_form.is_shows_colleagues())
