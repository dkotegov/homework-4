from time import sleep

from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestLinks:
    def test_same_film(self):

        Genre.open_genre_page()
       # Genre.click_film()

       # Film.wait_for_container()
       # Film.go_to_same_film()
       # Film.wait_for_container()

    def test_year(self):

        Genre.open_genre_page()
     #   Genre.click_film()

      #  Film.wait_for_container()
      #  year = Film.click_year()


    def test_actor(self):
        Genre.open_genre_page()
      #  Genre.click_film()

      #  Film.wait_for_container()
      #  Film.check_actor()

    def test_country(self):
    
        Genre.open_genre_page()
      #  Genre.click_film()
        #Film.wait_for_container()
      #  country = Film.click_country()


    def test_genre(self):
        Genre.open_genre_page()
      #  Genre.click_film()
      #  Film.wait_for_container()
      #  genre = Film.click_genre()

