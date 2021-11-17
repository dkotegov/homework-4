import unittest
import time

from tests.default_setup import default_setup
from tests.pages.user.profile import UserProfilePage
from tests.steps.auth_user import auth_setup


class ChangeUserAvatarSuccessTests(unittest.TestCase):

    def setUp(self):
        default_setup(self)
        auth_setup(self)
        self.profile_page = UserProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_change_avatar(self):
        self.profile_page.add_avatar()
        time.sleep(10)
