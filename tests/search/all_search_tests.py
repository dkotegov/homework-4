import unittest
from Pages.search_page import SearchPage
from tests.default_setup import default_setup


class AllSearchTests(unittest.TestCase):
    search_string = "по"

    def setUp(self):
        default_setup(self)
        self.search_page = SearchPage(self.driver)
        self.search_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_search_film(self):
        check = "Бегущий по лезвию 2049"
        self.search_page.fill_search(self.search_string)
        self.search_page.wait_for_end_of_search()
        film_list = self.search_page.get_films_list()
        self.assertIn(check, film_list)

    def test_search_actor(self):
        check = "Натали Портман"
        self.search_page.fill_search(self.search_string)
        self.search_page.wait_for_end_of_search()
        actor_list = self.search_page.get_actors_list()
        self.assertIn(check, actor_list)

    def test_search_person(self):
        self.search_page.fill_search(self.search_string)
        self.search_page.wait_for_end_of_search()
        people_list = self.search_page.get_people_list()
        self.assertEqual(len(people_list), 0)
