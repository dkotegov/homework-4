# coding=utf-8
import unittest

from os import getcwd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_test import BaseTest
from pages import PhotoPage


class BasePhotoPageTest(BaseTest):
    REFERENCE_TO_PHOTOS = '//div[@id="hook_Block_MiddleColumnTopCard_MenuUser"]/div/a[3]'

    def setUp(self):
        super(BasePhotoPageTest, self).setUp()

        self.driver.find_element_by_xpath(self.REFERENCE_TO_PHOTOS).click()

    def tearDown(self):
        self.driver.quit()


class AddAndDeleteNewAlbum(BasePhotoPageTest):
    ALBUM_NAME = u'test'

    def test(self):
        photo_page = PhotoPage(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                photo_page.PHOTO_ALBUMS_HEADER
            ))
        )

        photo_page.new_album_click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                photo_page.NEW_ALBUM_MENU
            ))
        )

        photo_page.create_new_album(self.ALBUM_NAME)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                photo_page.ALBUM_NAME_HEADER
            ))
        )

        photo_page.album_edit_click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                photo_page.ALBUM_NAME_EDIT
            ))
        )

        photo_page.delete_album()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                photo_page.ALBUM_DELETE_CONFIRM_TABLE
            ))
        )

        photo_page.delete_album_confirm()


class AddAndDeleteNewPhoto(BasePhotoPageTest):
    RELATIVE_PATH = '/tests_rogachev/image.jpg'

    def test(self):
        photo_page = PhotoPage(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                photo_page.PHOTO_ALBUMS_HEADER
            ))
        )
        photo_page.post_new_photo(getcwd() + self.RELATIVE_PATH)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                photo_page.NEW_PICTURE_CREATED_CSS
            ))
        )
        photo_page.remove_picture()

photos_page_tests = [
    unittest.TestSuite((
       unittest.makeSuite(AddAndDeleteNewAlbum)
    )),
    unittest.TestSuite((
        unittest.makeSuite(AddAndDeleteNewPhoto)
    )),
]