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

    @unittest.skip('ok')
    def test_first_name_element(self):
        self.register_page.open()
        form = self.register_page.get_form()

        self.assertTrue(form.check_exists_by_xpath(form.FIRST_NAME_INPUT))
        self.driver.find_element_by_xpath(form.FIRST_NAME_INPUT).click()

        notification = form.get_first_name_notif()
        self.assertTrue(notification.is_displayed())

        form.unfocus()

        error = form.get_first_name_error()
        self.assertTrue(error.is_displayed())

    @unittest.skip('ok')
    def test_last_name_element(self):
        self.register_page.open()
        form = self.register_page.get_form()

        self.assertTrue(form.check_exists_by_xpath(form.LAST_NAME_INPUT))
        self.driver.find_element_by_xpath(form.LAST_NAME_INPUT).click()

        notification = form.get_last_name_notif()
        self.assertTrue(notification.is_displayed())

        form.unfocus()

        error = form.get_last_name_error()
        self.assertTrue(error.is_displayed())

    @unittest.skip('ok')
    def test_birth_date_right_date(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.select_day('11')
        form.select_month('March')
        form.select_year('1999')
        form.unfocus()

        birthdate_success = form.get_birthdate_success_el()
        self.assertTrue(birthdate_success.is_displayed())

    @unittest.skip('ok')
    def test_birth_date_wrong_date(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.select_day('30')
        form.select_month('February')
        form.select_year('1999')
        form.unfocus()

        birthdate_success = form.get_birthdate_success_el()
        birthdate_error = form.get_birthdate_error_el()

        self.assertFalse(birthdate_success.is_displayed())
        self.assertTrue(birthdate_error.is_displayed())

    @unittest.skip('ok')
    def test_birth_date_required_field(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.select_day('30')
        form.unfocus()

        birthdate_error = form.get_birthdate_error_el()
        self.assertTrue(birthdate_error.is_displayed())

    @unittest.skip('ok')
    def test_city_only_from_list(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.set_city(u'Гейсити')
        form.unfocus()

        city_error_el = form.get_city_error_el()
        self.assertTrue(city_error_el.is_displayed())

    def test_city_autocompletion(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.set_city(u'Москва')
        self.assertTrue(form.check_exists_by_xpath(form.CITY_HELPER))

        helper = form.get_city_helper_el()
        city = helper.find_element_by_tag_name('div')
        city.click()

        city_success_el = form.get_city_success_el()
        self.assertTrue(city_success_el.is_displayed())



    def tearDown(self):
        self.driver.quit()

