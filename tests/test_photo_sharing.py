from tests.pages.primary.photo_page import PhotoPage
from tests.test_photo_manipulation import PhotoManipulationTest

import unittest


class PhotoSharingTest(PhotoManipulationTest):
    @unittest.expectedFailure
    def test_share_photo(self):
        photo_page = PhotoPage(self.driver)
        photo_page.goto()
        photos = self.driver.current_url
        photo = photo_page.get_photo()
        photo.open_overlay()
        toolbar = photo.toolbar()
        shares_before = toolbar.get_left_toolbar().shares_count()
        toolbar.get_left_toolbar().share()
        shares_after = toolbar.get_left_toolbar().shares_count()
        self.assertNotEquals(shares_before, shares_after)
        self.driver.get(photos)
        toolbar.get_left_toolbar().unshare()
        self.driver.get(photos)
        photo.open_overlay()
        likes_after_cancel = toolbar.get_left_toolbar().shares_count()
        self.driver.get(photos)
        self.assertEquals(shares_before, likes_after_cancel)

