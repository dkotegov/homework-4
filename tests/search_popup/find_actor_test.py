import constants
from tests.default import Test
from components.search_popup import SearchPopup
from pages.main import MainPage
from pages.actor import ActorPage


class FindActorTest(Test):
    ACTOR_NAME = 'солейл мун фрай'

    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.search(self.ACTOR_NAME)
        search_popup.click_on_founded_item()

        details_page = ActorPage(self.driver, constants.ID_OF_ACTOR)

        self.assertEqual(
            self.ACTOR_NAME,
            details_page.get_name_of_actor().lower()
        )
