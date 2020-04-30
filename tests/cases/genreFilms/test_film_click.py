
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestFilmClick:
    def test(self):

        Genre.open_genre_page()
        Genre.click_film()
        Film.wait_for_container()
