import unittest

from pages.main_page import MainPage
from setup.default_setup import default_setup


class CheckFilmPopup(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = MainPage(self.driver)
        self.page.open()

    def test_popup_like(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        is_auth_right = self.page.check_auth()
        self.assertTrue(is_auth_right)
        self.page.open_popup()
        self.page.click_infoblock_like_button()
        is_all_right = self.page.check_infoblock_liked()
        self.assertTrue(is_all_right)

    def test_popup_dislike(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        is_auth_right = self.page.check_auth()
        self.assertTrue(is_auth_right)
        self.page.open_popup()
        self.page.click_infoblock_dislike_button()
        is_all_right = self.page.check_infoblock_disliked()
        self.assertTrue(is_all_right)

    def test_genre_redirect(self):
        self.page.open_popup()
        self.page.click_genre()
        is_all_right = self.page.check_genre_redirect()
        self.assertTrue(is_all_right)

    def test_actor_redirect(self):
        self.page.open_popup()
        self.page.click_actor()
        is_all_right = self.page.check_actor_redirect()
        self.assertTrue(is_all_right)

    def test_director_redirect(self):
        self.page.open_popup()
        self.page.click_director()
        is_all_right = self.page.check_director_redirect()
        self.assertTrue(is_all_right)

    def test_same_film_open(self):
        while True:
            self.page.open_popup()
            if self.page.is_same_films():
                break
            else:
                self.page.open()
        self.page.click_same_film()
        is_all_right = self.page.check_same_film_popup_open()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
