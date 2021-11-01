from pages.movies import MoviesPage
from pages.genre import GenrePage
from tests.default import Test


class ClickOnGenreTest(Test):
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
