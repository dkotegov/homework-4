import constants
from pages.actor import ActorPage
from pages.details import DetailsPage
from tests.default import Test


class ClickOnMovieNameTest(Test):
    def test(self):
        actor_page = ActorPage(self.driver, constants.ID_OF_ACTOR)
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        actor_page.open()
        
        title = actor_page.get_title_of_first_movie()
        actor_page.click_on_first_movie_name()

        self.assertEqual(
            title,
            details_page.get_title()
        )
