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


class AlbumTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        AuthPage(self.driver).auth(self.LOGIN, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def upload_photo_and_open(self):
        album_page = UserAlbumPage(self.driver)
        album_id = album_page.parse_album_id()

        UserAddAlbumPhotoPage(self.driver, album_id).upload_photo()

        album_page.open()
        photos_list = album_page.photos_list
        photos_list.first.click()

    def test_create_album(self):
        album_name = 'Created test album #{}'.format(time.time())
        UserAlbumEditPage(self.driver).create_album(album_name)

        album = UserAlbumPage(self.driver).empty_album
        self.assertEqual(album_name, album.title)

    def test_remove_album(self):
        album_name = 'Test album #{} for remove'.format(time.time())
        UserAlbumEditPage(self.driver).create_album(album_name)

        album_page = UserAlbumPage(self.driver)

        toolbar = album_page.toolbar
        toolbar.open()
        toolbar.delete()

        album_page.confirmation_modal.delete()

        albums_list = UserAlbumsPage(self.driver).albums_list
        self.assertFalse(albums_list.includes(album_name))

    def test_rename_album(self):
        UserAlbumEditPage(self.driver).create_album()

        album_page = UserAlbumPage(self.driver)

        toolbar = album_page.toolbar
        toolbar.open()
        toolbar.edit()

        album_name = 'Renamed test album #{}'.format(time.time())
        edit_form = UserAlbumEditPage(self.driver).form
        edit_form.set_name(album_name)
        edit_form.submit()

        self.assertEqual(album_name, album_page.empty_album.title)

    def test_like_album(self):
        album_name = 'Liked test album #{}'.format(time.time())
        UserAlbumEditPage(self.driver).create_album(album_name)
        UserAlbumsPage(self.driver).like_album(album_name)

        albums_page = UserAlbumsPage(self.driver)
        album_item = albums_page.albums_list.find(album_name)
        self.assertEqual(1, album_item.likes_count)

    def test_cancel_album_like(self):
        album_name = 'Liked test album #{}'.format(time.time())
        UserAlbumEditPage(self.driver).create_album(album_name)
        UserAlbumsPage(self.driver).like_album(album_name)

        # Дизлайк
        UserAlbumsPage(self.driver).like_album(album_name)

        albums_page = UserAlbumsPage(self.driver)
        album_item = albums_page.albums_list.find(album_name)
        self.assertEqual(0, album_item.likes_count)

    def test_add_photo(self):
        UserAlbumEditPage(self.driver).create_album()

        album_page = UserAlbumPage(self.driver)
        album_id = album_page.parse_album_id()

        UserAddAlbumPhotoPage(self.driver, album_id).upload_photo()

        edit_photo = UserEditAlbumPhotoPage(self.driver)
        edit_photo.form.save()
        self.assertEqual(1, album_page.photos_list.count)

    def test_add_photo_with_description(self):
        UserAlbumEditPage(self.driver).create_album()

        album_page = UserAlbumPage(self.driver)
        album_id = album_page.parse_album_id()

        UserAddAlbumPhotoPage(self.driver, album_id).upload_photo()

        edit_photo = UserEditAlbumPhotoPage(self.driver).form
        description = 'Photo description.'
        edit_photo.set_description(description)
        edit_photo.save()

        photos_list = album_page.photos_list
        self.assertEqual(1, photos_list.count)
        photos_list.first.click()
        photo = PhotoPage(self.driver).photo
        self.assertEqual(description, photo.description)

    def test_like_photo(self):
        UserAlbumEditPage(self.driver).create_album()
        self.upload_photo_and_open()

        photo = PhotoPage(self.driver).photo
        photo.like()
        self.assertEqual(1, photo.likes_count)

    def test_cancel_photo_like(self):
        UserAlbumEditPage(self.driver).create_album()
        self.upload_photo_and_open()

        photo = PhotoPage(self.driver).photo
        photo.like()
        self.driver.refresh()

        # Отмена лайка
        photo.cancel_like()
        self.assertEqual(0, photo.likes_count)

    def test_make_photo_album_cover(self):
        UserAlbumEditPage(self.driver).create_album()

        album_page = UserAlbumPage(self.driver)
        album_id = album_page.parse_album_id()

        UserAddAlbumPhotoPage(self.driver, album_id).upload_photo(abspath('tests/photos/test_photo.jpg'))
        UserAddAlbumPhotoPage(self.driver, album_id).upload_photo(abspath('tests/photos/test_photo2.jpeg'))

        album_page.open()
        photos_list = album_page.photos_list

        # Делаю первое фото обложкой
        first_photo_item = photos_list.get(0)
        first_photo_id = first_photo_item.image_id

        first_photo_item.click()
        PhotoPage(self.driver).make_photo_cover()

        album_page.open()
        self.assertEqual(first_photo_id, album_page.album_header.cover_id)

        # Делаю второе фото обложкой
        second_photo_item = photos_list.get(1)
        second_photo_id = second_photo_item.image_id

        second_photo_item.click()
        PhotoPage(self.driver).make_photo_cover()

        album_page.open()
        self.assertEqual(second_photo_id, album_page.album_header.cover_id)
