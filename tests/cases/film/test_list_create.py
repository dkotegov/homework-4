
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film
from tests.steps.lists.steps import Steps as Lists
from tests.steps.review.steps import Steps as ReviewSteps
from tests.steps.profile.steps import Steps as ProfileSteps
from tests.conftest import open_user_profile

class TestListCreate:
    def test_in_created(self):
        Auth.auth()
        list_name = 'testlist'
        film_id = 2
        ReviewSteps.get_film(film_id)
        Lists.select_list(list_name)
        open_user_profile()
        ProfileSteps.open_lists_tab()
        ProfileSteps.check_film_in_list(list_name, film_id)
        
  #  def test_eng(self):
   #     name = "testlist"

        #TODO: Auth.simpleAuth()

      #  Genre.open_genre_page()
      #  Genre.click_film()

       # Film.wait_for_container()
       # Film.create_list(name)
       # Film.check_list_name(name)

        #TODO: logout

  #  def test_ru(self):
    #    name = "тестовый"

        #TODO: Auth.simpleAuth()

      #  Genre.open_genre_page()
       # Genre.click_film()

      #  Film.wait_for_container()
      #  Film.create_list(name)
      #  Film.check_list_name(name)

        #TODO: logout
  #  def test_symbols(self):
   #     name = "%;5;TEST"

        #TODO: Auth.simpleAuth()

      #  Genre.open_genre_page()
       # Genre.click_film()

       # Film.wait_for_container()
       # Film.create_list(name)
       # Film.check_list_name(name)

        #TODO: logout

  #  def test_cancel_creation(self):
    #    pass
        #TODO: Auth.simpleAuth()

      #  Genre.open_genre_page()
        #Genre.click_film()

      #  Film.wait_for_container()
        #Film.cancel_create_window()

        #TODO: logout