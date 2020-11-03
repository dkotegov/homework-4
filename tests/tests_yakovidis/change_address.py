import os
import unittest
from tests.pages.address_page import AddressPage

from selenium.webdriver import DesiredCapabilities, Remote


class AddressTest(unittest.TestCase):
    DEFAULT_PHOTO = 'data/test_prod_photo.jpg'
    PROFILE_PHOTO = 'data/test_rest_photo.jpg'
    BIG_PROFILE_PHOTO = 'data/test_big_photo.jpg'
    WRONG_PROFILE_PHOTO = 'data/test_non_photo_file'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.address_page = AddressPage(self.driver)
        self.address_page.open()

        self.address_form = self.address_page.form

    def test_wrong_address_input(self):
        self.address_form.wait_open()

        self.address_form.set_address('some address')
        address_error = self.address_form.get_input_error()

        self.assertEqual(address_error, 'с точностью до дома')

    def test_help_block(self):
        self.address_form.wait_open()

        self.address_form.set_address('Маяковская')

        self.assertEqual(self.address_form.wait_help_block(), True)

    def tearDown(self):
        self.driver.quit()
