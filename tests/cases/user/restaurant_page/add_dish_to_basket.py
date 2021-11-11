import os

import unittest

from tests.default_setup import default_setup


class AddDishToBasketTest(unittest.TestCase):
    def setUp(self):
        default_setup(self)

    def tearDown(self):
        self.driver.quit()

    def test(self):
        self.driver.get("https://delivery-borscht.ru/store/1")
