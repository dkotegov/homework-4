import unittest

from setup.default_setup import default_setup
from setup.auth import setup_auth

class CheckProfile(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

    def test_check_profile_email(self):
        setup_auth(self)

    def tearDown(self):
        self.driver.quit()
