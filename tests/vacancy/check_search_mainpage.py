import unittest

from pages.main_page import MainPage
from setup.default_setup import default_setup


class CheckSearch(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.page = MainPage(self.driver)

        self.page.open()

    def test_search(self):
        self.page.search_by_profession(proffesion="Воспитатель")

        self.assertTrue(self.page)

    def tearDown(self):
        self.driver.quit()
