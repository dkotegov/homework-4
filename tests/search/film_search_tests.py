import unittest
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
        self.assertIn(string, film_list)


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
        self.assertIn(check, film_list)

    def test_search_film_right_2(self):
        string = "кок"
        check = "Тайна Коко"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        self.assertIn(check, film_list)

    def test_search_film_wrong(self):
        string = "кор"
        check = "Тайна Коко"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        self.assertNotIn(check, film_list)

    def test_search_film_wrong_2(self):
        string = "корп"
        check = "Король Лев"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        self.assertNotIn(check, film_list)

