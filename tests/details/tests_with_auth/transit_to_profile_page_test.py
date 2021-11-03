from pages.details import DetailsPage
from pages.profile import ProfilePage

import constants

from tests.default_authorized import TestAuthorized


class TransitToProfileTest(TestAuthorized):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_PAID_MOVIE)
        details_page.open()

        details_page.transit_by_stub()

        profile_page = ProfilePage(self.driver)
        title_of_page = profile_page.get_title_of_page()

        self.assertEqual(
            title_of_page,
            constants.TITLE_OF_PROFILE_PAGE
        )
