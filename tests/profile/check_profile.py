import unittest

from pages.profile_page import ProfilePage
from scenario.default_setup import default_setup
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

    def test_check_profile_email(self):
        is_equal = self.page.check_profile_email(self.margot_contacts['email'])
        self.assertTrue(is_equal)

    def tearDown(self):
        self.driver.quit()
