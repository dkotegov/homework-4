from time import sleep

from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestReview:
    def test_eng(self):

        Genre.open_genre_page()
        Genre.click_more_button()
