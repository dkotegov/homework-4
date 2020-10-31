import os
import unittest

from tests.pages.address_page import AddressPage

from selenium.webdriver import DesiredCapabilities, Remote


class FirstTest(unittest.TestCase):
    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy() 
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        addr_page = AddressPage(self.driver)
        addr_page.open()

        addr_form = addr_page.form
        addr_form.wait_open()
        addr_form.set_address(self.ADDRESS)
        addr_form.submit()
