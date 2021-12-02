from tests.default import Test
from components.search_popup import SearchPopup
from pages.main import MainPage
import constants
from pages.details import DetailsPage
from pages.actor import ActorPage


class ClosePopupTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.close()

        self.assertFalse(search_popup.is_visible())


class FindMovieTest(Test):
    MOVIE_TITLE = constants.SEARCH_MOVIE_TITLE

    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.search(self.MOVIE_TITLE)
        search_popup.click_on_named_founded_item(self.MOVIE_TITLE)

        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)

        self.assertEqual(
            self.MOVIE_TITLE,
            details_page.get_title()
        )


class FindActorTest(Test):
    ACTOR_NAME = constants.SEARCH_ACTOR_NAME

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


class EnterLetterTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        search_popup = SearchPopup(self.driver)
        search_popup.open()
        search_popup.search('г')
        count_founded_items = search_popup.count_found_items()
        search_popup.search('гн')

        self.assertNotEqual(
            count_founded_items,
            search_popup.count_found_items()
        )
