from pages.favourites import FavouritesPage
from tests.default import Test


class NotOpenedTest(Test):
    def test(self):
        favourites_page = FavouritesPage(self.driver)
        favourites_page.open()

        self.assertEqual(
            False,
            favourites_page.is_has_favourites()
        )
