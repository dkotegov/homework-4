import unittest

from setup.default_setup import default_setup


class CheckProfile(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

    def tearDown(self):
        self.driver.quit()
