from pages.actor import ActorPage
from pages.details import DetailsPage

import constants

from tests.default import Test


class ClickOnActorNameTest(Test):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        actor_name = details_page.get_name_of_last_actor()
        details_page.click_on_last_actor()

        actor_page = ActorPage(self.driver, constants.ID_OF_ACTOR)

        self.assertEqual(
            actor_name,
            actor_page.get_name_of_actor()
        )
