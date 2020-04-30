
from tests.steps.genreFilm.steps import Steps as Genre


class TestMoreButton:
    def test(self):

        Genre.open_genre_page()
        Genre.click_more_button()
