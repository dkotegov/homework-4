# -*- coding: utf-8 -*-
import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from register_page import RegisterPage


class RegistrationTest(unittest.TestCase):
    BROWSER = os.environ['HW4BROWSER']

    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.BROWSER).copy()
        )

        self.register_page = RegisterPage(self.driver)

    def test_firstname_element(self):
        self.register_page.open()
        form = self.register_page.get_form()

        self.assertTrue(form.check_exists_by_xpath(form.FIRST_NAME_INPUT))
        self.driver.find_element_by_xpath(form.FIRST_NAME_INPUT).click()

        notification = form.get_first_name_notif()
        self.assertTrue(notification.is_displayed())

        form.unfocus()

        error = form.get_first_name_error()
        self.assertTrue(error.is_displayed())


    def tearDown(self):
        self.driver.quit()

