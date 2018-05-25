# -*- coding: utf-8 -*-

import os

import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote

from tests.Pages.PhotoSectionPage import PhotoSectionPage
from tests.TestsMethods.CommonMethods import CommonMethods
from tests.TestsMethods.CreateAlbumTestsMethods import CreateAlbumTestsMethods
from tests.Utils import Constants


class CreateAlbumTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        browser = os.environ.get('BROWSER', 'CHROME')

        cls.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        cls.common_methods = CommonMethods(cls.driver)
        cls.methods = CreateAlbumTestsMethods(cls.driver)

    def setUp(self):
        self.common_methods.authorize()
        self.common_methods.redirect_to_photo_section_from_feed_page()

    def tearDown(self):
        self.common_methods.quit_profile_from_any_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_create_album_with_common_name(self):

        self.methods.create_album_from_photo_section_page(Constants.COMMON_NAME)

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        photo_album_list = PhotoSectionPage(self.driver).photo_albums_list_bar

        self.assertTrue(photo_album_list.check_album_with_name(Constants.COMMON_NAME))

        self.methods.delete_album_from_photo_section(Constants.COMMON_NAME)

    def test_create_album_with_empty_name(self):

        try:
            self.methods.create_album_from_photo_section_page(Constants.EMPTY_NAME)
        except TimeoutException:
            self.methods.close_create_album_popup()

        photo_album_list = PhotoSectionPage(self.driver).photo_albums_list_bar

        self.assertFalse(photo_album_list.check_album_with_name(Constants.EMPTY_NAME))

    def test_create_album_with_more_than_acceptable_name(self):

        try:
            self.methods.create_album_from_photo_section_page(Constants.FIFTY_ONE_LETTERS_NAME)
        except TimeoutException:
            self.methods.close_create_album_popup()

        photo_album_list = PhotoSectionPage(self.driver).photo_albums_list_bar

        self.assertFalse(photo_album_list.check_album_with_name(Constants.FIFTY_ONE_LETTERS_NAME))

    def test_create_album_with_spaced_name(self):

        self.methods.create_album_from_photo_section_page(Constants.SPACED_NAME)

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        photo_album_list = PhotoSectionPage(self.driver).photo_albums_list_bar

        self.assertFalse(photo_album_list.check_album_with_name(Constants.SPACED_NAME))

        self.assertTrue(photo_album_list.check_album_with_name(Constants.SPACED_NAME_TO_CHECK))

        self.methods.delete_album_from_photo_section(Constants.SPACED_NAME_TO_CHECK)
