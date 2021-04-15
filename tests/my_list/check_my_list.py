import unittest

from pages.film_page import FilmPage
from pages.main_page import MainPage
from pages.my_list_page import MyListPage
from setup.default_setup import default_setup


class CheckMyList(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.film_page = FilmPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.my_list_page = MyListPage(self.driver)
        self.main_page.open()

    def test_my_list_add(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        is_all_right = self.main_page.check_auth()
        self.assertTrue(is_all_right)
        self.my_list_page.open()
        self.my_list_page.count_films()
        self.film_page.open()
        self.film_page.open_infoblock()
        is_added = self.film_page.click_add_mylist_button()
        self.my_list_page.open()
        is_number_changed = self.my_list_page.check_films_number_changed(is_added)
        self.assertTrue(is_number_changed)

    def test_subscription_popup_open(self):
        self.main_page.open_auth_popup()
        self.main_page.auth(self.EMAIL, self.PASSWORD)
        is_all_right = self.main_page.check_auth()
        self.assertTrue(is_all_right)
        self.film_page.open()
        self.film_page.find_subscription_film()
        self.film_page.click_play_button()
        is_popup_open = self.film_page.check_subscription_popup_open()
        self.assertTrue(is_popup_open)

    def tearDown(self):
        self.driver.quit()
