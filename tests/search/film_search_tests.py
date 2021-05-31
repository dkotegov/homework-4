import unittest
from utils.in_list import in_list
from utils.not_in import not_in
from Pages.search_page import SearchPage
from tests.default_setup import default_setup

class FilmSearchTests(unittest.TestCase):
    def setUp(self):
        default_setup(self)
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.search_page.open_films()

    def tearDown(self):
        self.driver.quit()

    def test_search_film_success(self):
        string = "Корпорация монстров"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        is_in = in_list(string, film_list)
        self.assertTrue(is_in)


    def test_search_film_empty(self):
        string = "карпарация монстрав"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        self.assertEqual(len(film_list), 0)

    def test_search_film_right(self):
        string = "к"
        check = "Как приручить дракона"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        is_in = in_list(check, film_list)
        self.assertTrue(is_in)

    def test_search_film_right_2(self):
        string = "кок"
        check = "Тайна Коко"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        is_in = in_list(check, film_list)
        self.assertTrue(is_in)

    def test_search_film_wrong(self):
        string = "кор"
        check = "Тайна Коко"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        is_not_in = not_in(check, film_list)
        self.assertTrue(is_not_in)

    def test_search_film_wrong_2(self):
        string = "корп"
        check = "Король Лев"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        is_not_in = not_in(check, film_list)
        self.assertTrue(is_not_in)

