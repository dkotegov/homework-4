import unittest
from Pages.search_page import SearchPage
from tests.default_setup import default_setup

class ActorsSearchTests(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.search_page.open_actors()

    def tearDown(self):
        self.driver.quit()

    def test_search_actor_success(self):
        string = "Александр Паль"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        actors_list = self.search_page.get_actors_list()
        self.assertIn(string, actors_list)

    def test_search_actor_empty(self):
        string = "освоы"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        actors_list = self.search_page.get_actors_list()
        self.assertEqual(len(actors_list), 0)

    def test_search_actor_right_1(self):
        string = "пал"
        check = "Александр Паль"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        actors_list = self.search_page.get_actors_list()
        self.assertIn(check, actors_list)

    def test_search_actor_right_2(self):
        string = "а"
        check = "Александр Паль"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        actors_list = self.search_page.get_actors_list()
        self.assertIn(check, actors_list)

    def test_search_actor_wrong(self):
        string = "Алеп"
        check = "Александр Паль"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        actors_list = self.search_page.get_actors_list()
        self.assertNotIn(check, actors_list)
