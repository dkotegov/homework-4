import unittest

from pages.profile_page import ProfilePage
from tests.default_setup import default_setup
from scenario.auth import setup_auth


class CheckProfile(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        setup_auth(self)

        self.page = ProfilePage(self.driver)
        self.page.open()

        self.margot_contacts = {
            "firstname": "margot",
            "lastname": "margot",
            "email": "margot@margot.ru"
        }


    def tearDown(self):
        self.driver.quit()
