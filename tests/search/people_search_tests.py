import unittest
from Pages.search_page import SearchPage
from tests.default_setup import default_setup


class PeopleSearchTests(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        self.search_page = SearchPage(self.driver)
        self.search_page.open()
        self.search_page.open_people()

    def tearDown(self):
        self.driver.quit()

    def test_search_people_success(self):
        string = "nnnnn"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        people_list = self.search_page.get_people_list()
        self.assertIn(string, people_list)

    def test_search_people_empty(self):
        string = "bhcdnjkas"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        people_list = self.search_page.get_people_list()
        self.assertEqual(len(people_list), 0)

    def test_search_people_low_register(self):
        string = "erik"
        check = "Erik123"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        people_list = self.search_page.get_people_list()
        self.assertIn(check, people_list)

    def test_search_people_high_register(self):
        string = "Erik"
        check = "Erik123"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        people_list = self.search_page.get_people_list()
        self.assertIn(check, people_list)

    def test_search_people_wrong(self):
        string = "Ers"
        check = "Erik123"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        people_list = self.search_page.get_people_list()
        self.assertNotIn(check, people_list)
