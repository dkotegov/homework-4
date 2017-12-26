# coding=utf-8

from os import getcwd
from time import sleep

from base_test import BaseTest
from pages import PhotoPage


class BasePhotoPageTest(BaseTest):
    REFERENCE_TO_PHOTOS = "//a[contains(text(), 'Фото')]"

    def setUp(self):
        super(BasePhotoPageTest, self).setUp()

        self.driver.find_element_by_xpath(self.REFERENCE_TO_PHOTOS).click()

    def tearDown(self):
        self.driver.quit()


class AddAndDeleteNewAlbum(BasePhotoPageTest):
    ALBUM_NAME = u'test'

    def test(self):
        photo_page = PhotoPage(self.driver)

        photo_page.new_album_click()

        photo_page.create_new_album(self.ALBUM_NAME)

        self.assertEqual(photo_page.get_album_name(), self.ALBUM_NAME)

        photo_page.album_edit_click()

        photo_page.delete_album()

        photo_page.delete_album_confirm()


class AddAndDeleteNewPhoto(BasePhotoPageTest):
    RELATIVE_PATH = '/tests_rogachev/image.jpg'

    def test(self):
        photo_page = PhotoPage(self.driver)
        photo_page.post_new_photo(getcwd() + self.RELATIVE_PATH)
        photo_page.remove_picture()
