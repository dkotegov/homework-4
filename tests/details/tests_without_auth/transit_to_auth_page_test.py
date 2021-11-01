from pages.details import DetailsPage
from pages.login import LoginPage

import constants

from tests.default import Test


class TransitToAuthTest(Test):
    def test(self):
        details_page = DetailsPage(self.driver, constants.ID_OF_MOVIE)
        details_page.open()

        details_page.transit_to_auth_page()

        login_page = LoginPage(self.driver)
        title_of_page = login_page.get_title_of_page()

        self.assertEqual(
            title_of_page,
            constants.TITLE_OF_LOGIN_PAGE
        )
