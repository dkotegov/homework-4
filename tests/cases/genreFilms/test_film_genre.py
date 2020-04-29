from time import sleep

from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestReview:
    def test_eng(self):

        Genre.open_genre_page()
        genre = Genre.click_genre()
        Genre.click_film()
        Film.wait_for_container()
        Film.check_genre(genre)
