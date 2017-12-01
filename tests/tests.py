# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from .pages import AuthPage, PhotoPage

LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']
name_alb = 'new_alb'
new_name_alb = 'new_name_alb'

WAIT_TIME = 10

class BaseTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(WAIT_TIME)
        self.login()

    def tearDown(self):
        self.driver.quit()

    def login(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(LOGIN)
        auth_form.set_password(PASSWORD)
        auth_form.submit()


class BaseAlbumCreateTest(BaseTest):
    def setUp(self):
        super(BaseAlbumCreateTest,self).setUp()
        self.photo_page = PhotoPage(self.driver)
        self.photo_page.open_photos.check_click()

    def delAlbum(self):
        self.photo_page.album.edit_click()
        self.photo_page.album.del_click()


class BaseAlbumEditTest(BaseTest):
    def setUp(self):
        super(BaseAlbumEditTest,self).setUp()
        self.photo_page = PhotoPage(self.driver)
        self.photo_page.open_photos.check_click()
        self.createAlbum()

    def tearDown(self):
        self.delAlbum()
        super(BaseAlbumEditTest,self).tearDown()

    def createAlbum(self):
        self.photo_page.create_album.check_click()
        self.photo_page.create_album.create_name_album(name_alb)
        self.photo_page.create_album.create_album_click()
        self.photo_page.album.photo_click()

    def delAlbum(self):
        self.photo_page.album.del_click()


class PhotoSectionTest(BaseTest):
    def test(self):
        self.photo_page = PhotoPage(self.driver)
        self.assertTrue(self.photo_page.open_photos.check_click())


class CreateAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())


class CancelCreateAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.cancel_click())


class CheckboxesAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.check_checkboxes())


class CheckboxesAllFriendAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.check_all_friend_checkboxes())


class CheckboxesNotAllFriendAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.check_not_all_friend_checkboxes())


class CheckboxesNotEmptyAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.check_not_empty_checkboxes())


class NameAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.create_name_album(name_alb))


class CreatedAlbumTest(BaseAlbumCreateTest):
    def test(self):
        self.assertTrue(self.photo_page.create_album.check_click())
        self.assertTrue(self.photo_page.create_album.create_name_album(name_alb))
        self.assertTrue(self.photo_page.create_album.create_album_click())
        self.delAlbum()


class OpenAlbumTest(BaseAlbumEditTest):
    def test(self):
        self.assertTrue(self.photo_page.album.open_click(name_alb))
        self.assertTrue(self.photo_page.album.edit_click())


class EditAlbumTest(BaseAlbumEditTest):
    def test(self):
        self.assertTrue(self.photo_page.album.open_click(name_alb))
        self.assertTrue(self.photo_page.album.edit_click())


class RenameAlbumTest(BaseAlbumEditTest):
    def test(self):
        self.assertTrue(self.photo_page.album.open_click(name_alb))
        self.assertTrue(self.photo_page.album.edit_click())
        self.assertTrue(self.photo_page.album.check_rename(new_name_alb))
        self.assertTrue(self.photo_page.album.check_rename(name_alb))


class BackAlbumTest(BaseAlbumEditTest):
    def test(self):
        self.assertTrue(self.photo_page.album.open_click(name_alb))
        self.assertTrue(self.photo_page.album.edit_click())
        self.assertTrue(self.photo_page.album.back_click())
        self.assertTrue(self.photo_page.album.edit_click())


class EditPrivateAlbumTest(BaseAlbumEditTest):
    def test(self):
        self.assertTrue(self.photo_page.album.open_click(name_alb))
        self.assertTrue(self.photo_page.album.edit_click())
        self.assertTrue(self.photo_page.album.edit_private_click())
        self.assertTrue(self.photo_page.album.cancel_click())


class DeleteAlbumTest(BaseTest):
    def setUp(self):
        super(DeleteAlbumTest,self).setUp()
        self.photo_page = PhotoPage(self.driver)
        self.photo_page.open_photos.check_click()
        self.createAlbum()

    def createAlbum(self):
        self.photo_page.create_album.check_click()
        self.photo_page.create_album.create_name_album(name_alb)
        self.photo_page.create_album.create_album_click()
        self.photo_page.album.photo_click()

    def test(self):
        self.assertTrue(self.photo_page.album.open_click(name_alb))
        self.assertTrue(self.photo_page.album.edit_click())
        self.assertTrue(self.photo_page.album.del_click())


buklin_tests = [
    unittest.TestSuite((
        unittest.makeSuite(PhotoSectionTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CreateAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CancelCreateAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CheckboxesAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CheckboxesAllFriendAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CheckboxesNotAllFriendAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CheckboxesNotEmptyAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(NameAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(CreatedAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(OpenAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(EditAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(RenameAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(BackAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(EditPrivateAlbumTest),
    )),
    unittest.TestSuite((
        unittest.makeSuite(DeleteAlbumTest),
    )),
]
