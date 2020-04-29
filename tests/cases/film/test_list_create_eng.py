from time import sleep

from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestListCreateENG:
    def test(self):
        name = "testlist"

        #TODO: Auth.simpleAuth()

       # Genre.open_genre_page()
       # Genre.click_film()

        #Film.wait_for_container()
       # Film.create_list(name)
       # Film.check_list_name(name)

        #TODO: logout
