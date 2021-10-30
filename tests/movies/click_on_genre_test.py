import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.movies import MoviesPage
from pages.genre import GenrePage


class ClickOnGenreTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        movies_page = MoviesPage(self.driver)
        genre_page = GenrePage(self.driver)

        movies_page.open()
        genre_name = movies_page.get_name_of_first_genre()
        movies_page.click_on_first_genre()

        self.assertEqual(
            genre_name,
            genre_page.get_genre_name()
        )
