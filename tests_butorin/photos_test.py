# -*- coding: utf-8 -*-

from base_test import BaseTest, LOGIN
from page import PhotosPage, MainPage


class BasePhotoTest(BaseTest):

    def setUp(self):
        super(BasePhotoTest, self).setUp()

        self.added_photos = []

        self.photos_page = PhotosPage(self.driver, LOGIN)
        self.photos_page.open()
        self.photos = self.photos_page.photos()

    def tearDown(self):
        self.photos_page.open()
        for photo in self.added_photos:
            self.delete_photo(photo)
        super(BasePhotoTest, self).tearDown()

    def add_photo(self):
        id = self.photos.upload_and_get_photo()
        self.added_photos.append(id)
        self.photos_page.open()
        return id

    def delete_photo(self, id):
        self.photos.open_photo(LOGIN, id)
        self.photos.click_delete()
        self.added_photos.remove(id)


class UploadPhotoTest(BasePhotoTest):
    def test(self):
        self.photos.upload_photo()
        self.assertIsNotNone(self.photos.get_uploaded_photo())

    def tearDown(self):
        self.added_photos.append(self.photos.get_last_photo())
        super(UploadPhotoTest, self).tearDown()


class OpenPhotoTest(BasePhotoTest):
    def test(self):
        id = self.add_photo()
        self.photos.click_on_photo(LOGIN, id)
        self.assertIsNotNone(self.photos.get_opened_photo())


class MakeMainPhotoTest(BasePhotoTest):
    def test(self):
        id = self.add_photo()
        self.photos.submit_main(LOGIN, id)

        self.main_page = MainPage(self.driver, LOGIN)
        self.main_page.open()
        self.assertEqual(id, self.main_page.get_photo_id())


class ClosePhotoOverlayTest(BasePhotoTest):
    def test(self):
        id = self.add_photo()
        self.photos.open_photo(LOGIN, id)
        self.photos.click_overlay()
        self.assertTrue(self.photos.is_photo_disappeared())


class ClosePhotoButtonTest(BasePhotoTest):
    def test(self):
        id = self.add_photo()
        self.photos.open_photo(LOGIN, id)
        self.photos.click_close()
        self.assertTrue(self.photos.is_photo_disappeared())


class DeletePhotoTest(BasePhotoTest):
    def test(self):
        id = self.add_photo()
        count = self.photos.get_photos_count()

        self.delete_photo(id)

        self.photos_page.open()
        self.assertNotEqual(count, self.photos.get_photos_count())


class RestorePhotoTest(BasePhotoTest):
    def test(self):
        id = self.add_photo()
        self.photos_page.open()
        count = self.photos.get_photos_count()
        self.photos.open_photo(LOGIN, id)
        self.photos.click_delete()

        self.photos.click_restore()
        self.photos.click_close()
        self.photos_page.open()
        self.assertEqual(count, self.photos.get_photos_count())


class AddDescriptionTest(BasePhotoTest):
    def test(self):
        description = "Some description"
        id = self.add_photo()
        self.photos.open_photo(LOGIN, id)
        self.photos.add_description(description)
        self.driver.refresh()
        self.assertEqual(description, self.photos.get_description())


class ShowLinkTest(BasePhotoTest):
    def test(self):
        link = "https://ok.ru/{}/pphotos/{}"
        id = self.add_photo()
        self.photos.open_photo(LOGIN, id)
        self.assertEqual(link.format(LOGIN, id), self.photos.get_link())


class AddCommentTest(BasePhotoTest):
    def test(self):
        comment = "Some comment"
        id = self.add_photo()
        self.photos.open_photo(LOGIN, id)
        self.photos.add_comment(comment)

        self.assertEqual(comment, self.photos.get_comment())
