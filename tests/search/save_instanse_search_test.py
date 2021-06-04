import unittest
from Pages.search_page import SearchPage
from tests.default_setup import default_setup


class SaveInstanceSearchTests(unittest.TestCase):
    def setUp(self):
        default_setup(self)
        self.search_page = SearchPage(self.driver)
        self.search_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_save_instance(self):
        string = "nnnnn"
        self.search_page.fill_search(string)
        self.search_page.wait_for_end_of_search()
        self.search_page.click_people()
        self.driver.back()
        input_value = self.search_page.get_search_value()
        self.assertEqual(input_value, string)
