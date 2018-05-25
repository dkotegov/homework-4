import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.primaryPhotoSection.AlbumPage import AlbumPage
from tests.pages.primaryPhotoSection.PhotoSectionPage import PhotoSectionPage
from tests.TestsMethods.AddImageTestsMethods import AddImageTestsMethods
from tests.TestsMethods.CommonMethods import CommonMethods
from tests.utils import Constants


class AddImageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get('BROWSER', 'CHROME')

        cls.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        cls.common_methods = CommonMethods(cls.driver)
        cls.methods = AddImageTestsMethods(cls.driver)

    def setUp(self):
        self.common_methods.authorize()
        self.common_methods.redirect_to_photo_section_from_feed_page()

    def tearDown(self):
        self.common_methods.quit_profile_from_any_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_image_add_in_default_album(self):
        self.methods.upload_image(Constants.TEST_IMAGE_NAME)

        add_photo_button = PhotoSectionPage(self.driver).add_photo_button
        self.assertTrue(add_photo_button.check_upload_start_successfully())

        self.methods.wait_until_photo_downloaded()

        uploaded_image_id = self.methods.get_image_id_on_uploaded_photo_editor_page()

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        self.methods.redirect_to_album_page_from_photo_section_page(Constants.DEFAULT_ALBUM_NAME)

        album_page = AlbumPage(self.driver)
        self.assertTrue(album_page.list_of_photos.check_photo_in_album_by_id(uploaded_image_id))

        self.methods.delete_photo_from_album_by_id(uploaded_image_id)

    def test_restore_image_after_delete(self):
        self.methods.upload_image(Constants.TEST_IMAGE_NAME)

        self.methods.wait_until_photo_downloaded()

        uploaded_image_id = self.methods.get_image_id_on_uploaded_photo_editor_page()

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        self.methods.redirect_to_album_page_from_photo_section_page(Constants.DEFAULT_ALBUM_NAME)

        self.methods.delete_photo_from_album_by_id(uploaded_image_id)

        self.methods.wait_until_photo_deleted()

        self.methods.restore_photo_after_delete()

        self.methods.redirect_from_edit_page_to_album_page()

        album_page = AlbumPage(self.driver)
        self.assertTrue(album_page.list_of_photos.check_photo_in_album_by_id(uploaded_image_id))

    def test_cancel_image_upload(self):

        number_of_photos_before_upload = self.methods.get_number_of_photos_in_default_album()

        self.methods.upload_image(Constants.BIG_PICTURE_NAME)

        add_photo_button = PhotoSectionPage(self.driver).add_photo_button
        add_photo_button.check_upload_start_successfully()

        self.methods.cancel_photo_uploading()

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        number_of_photos_after_upload = self.methods.get_number_of_photos_in_default_album()

        self.assertEqual(number_of_photos_before_upload, number_of_photos_after_upload)








