# -*- coding: utf-8 -*-

import os
import time

import unittest
from os.path import abspath

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.mobile.auth_page import AuthPage
from tests.pages.mobile.photo_page import PhotoPage
from tests.pages.mobile.user_add_album_photo_page import UserAddAlbumPhotoPage
from tests.pages.mobile.user_album_edit_page import UserAlbumEditPage
from tests.pages.mobile.user_album_page import UserAlbumPage
from tests.pages.mobile.user_albums_page import UserAlbumsPage
from tests.pages.mobile.user_edit_album_photo_page import UserEditAlbumPhotoPage


class MobileAlbumTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        AuthPage(self.driver).auth(self.LOGIN, self.PASSWORD)

        self.album_name = 'Test album #{}'.format(time.time())
        UserAlbumEditPage(self.driver).create_album(self.album_name)

        self.album_page = UserAlbumPage(self.driver)
        self.album_id = self.album_page.parse_album_id()

    def tearDown(self):
        if self.album_page:
            self.album_page.open()
            self.album_page.remove_album()

        self.driver.quit()

    def upload_photo_and_open(self):
        album_id = self.album_page.parse_album_id()

        UserAddAlbumPhotoPage(self.driver, album_id).upload_photo()

        self.album_page.open()
        photos_list = self.album_page.photos_list
        photos_list.first.open()

    def test_remove_album(self):
        toolbar = self.album_page.toolbar
        toolbar.open()
        toolbar.delete()

        self.album_page.confirmation_modal.delete()

        albums_list = UserAlbumsPage(self.driver).albums_list
        self.assertFalse(albums_list.includes(self.album_name))

        self.album_page = None

    def test_rename_album(self):
        toolbar = self.album_page.toolbar
        toolbar.open()
        toolbar.edit()

        album_name = 'Renamed test album #{}'.format(time.time())
        edit_form = UserAlbumEditPage(self.driver).form
        edit_form.set_name(album_name)
        edit_form.submit()

        self.assertEqual(album_name, self.album_page.empty_album.title)

    def test_rename_album_to_long_name(self):
        toolbar = self.album_page.toolbar
        toolbar.open()
        toolbar.edit()

        album_name = 'L' * 51
        edit_form = UserAlbumEditPage(self.driver).form
        edit_form.set_name(album_name)
        edit_form.submit()
        self.assertTrue(edit_form.is_name_error())

        album_name = 'L' * 50
        edit_form.set_name(album_name)
        edit_form.submit()
        self.assertEqual(album_name, self.album_page.empty_album.title)

    def test_like_album_at_albums_page(self):
        albums_page = UserAlbumsPage(self.driver)
        albums_page.open()
        like_component = albums_page.albums_list.first.like
        like_component.like()
        self.assertEqual(1, like_component.likes_count)

    def test_like_album(self):
        UserAddAlbumPhotoPage(self.driver, self.album_id).upload_photo()
        self.album_page.open()

        like_component = self.album_page.like
        like_component.like()
        self.assertEqual(1, like_component.likes_count)

    def test_cancel_album_like(self):
        albums_page = UserAlbumsPage(self.driver)
        albums_page.open()
        like_component = albums_page.albums_list.first.like
        like_component.like()
        albums_page.touch_overlay()

        like_component.cancel_like()
        self.assertEqual(0, like_component.likes_count)

    def test_add_photo(self):
        UserAddAlbumPhotoPage(self.driver, self.album_id).upload_photo()

        edit_photo = UserEditAlbumPhotoPage(self.driver)
        edit_photo.form.save()
        self.assertEqual(1, self.album_page.photos_list.count)

    def test_add_photo_with_description(self):
        UserAddAlbumPhotoPage(self.driver, self.album_id).upload_photo()

        edit_photo = UserEditAlbumPhotoPage(self.driver).form
        description = 'Photo description.'
        edit_photo.set_description(description)
        edit_photo.save()

        photos_list = self.album_page.photos_list
        self.assertEqual(1, photos_list.count)
        photos_list.first.open()
        photo = PhotoPage(self.driver).photo
        self.assertEqual(description, photo.description)

    def test_xss_in_photo_description(self):
        UserAddAlbumPhotoPage(self.driver, self.album_id).upload_photo()

        edit_photo = UserEditAlbumPhotoPage(self.driver).form
        description = '<h1 id="xss">XSS</h1>'
        edit_photo.set_description(description)
        edit_photo.save()

        self.album_page.photos_list.first.open()
        photo_page = PhotoPage(self.driver)
        self.assertFalse(photo_page.is_xss)

    def test_upload_not_image(self):
        add_photo_page = UserAddAlbumPhotoPage(self.driver, self.album_id)
        add_photo_page.upload_photo(abspath('tests/photos/not_image.txt'))
        add_photo_form = add_photo_page.form
        self.assertTrue(add_photo_form.is_error)

        add_photo_form.upload_photo(abspath('tests/photos/not_image.jpg'))
        self.assertTrue(add_photo_form.is_error)

    def test_like_photo(self):
        self.upload_photo_and_open()

        like_component = PhotoPage(self.driver).photo.like
        like_component.like()
        self.assertEqual(1, like_component.likes_count)

    def test_cancel_photo_like(self):
        self.upload_photo_and_open()

        photo_page = PhotoPage(self.driver)
        like_component = photo_page.photo.like
        like_component.like()
        photo_page.touch_overlay()

        like_component.cancel_like()
        self.assertEqual(0, like_component.likes_count)

    def test_make_photo_album_cover(self):
        UserAddAlbumPhotoPage(self.driver, self.album_id).upload_photo(abspath('tests/photos/test_photo.jpg'))
        UserAddAlbumPhotoPage(self.driver, self.album_id).upload_photo(abspath('tests/photos/test_photo2.jpeg'))

        self.album_page.open()
        photos_list = self.album_page.photos_list

        # Делаю фото обложкой
        photo_item = photos_list.get(1)
        photo_id = photo_item.image_id

        photo_item.open()
        PhotoPage(self.driver).make_photo_cover()

        self.album_page.open()
        self.assertEqual(photo_id, self.album_page.album_header.cover_id)
