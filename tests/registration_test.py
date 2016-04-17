# -*- coding: utf-8 -*-
import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from register_page import RegisterPage


class RegistrationTest(unittest.TestCase):
    BROWSER = os.environ['HW4BROWSER']
    EMAIL = os.environ['HW4EMAIL']
    PASSWORD = os.environ['HW4PASSWORD']
    PHONE = os.environ['HW4PHONE']

    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.BROWSER).copy()
        )

        self.register_page = RegisterPage(self.driver)

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

    def test_birth_date_right_date(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.select_day('11')
        form.select_month('Март')
        form.select_year('1999')
        form.unfocus()

        birthdate_success = form.get_birthdate_success_el()
        self.assertTrue(birthdate_success.is_displayed())

    def test_birth_date_wrong_date(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.select_day('30')
        form.select_month('Февраль')
        form.select_year('1999')
        form.unfocus()

        birthdate_success = form.get_birthdate_success_el()
        birthdate_error = form.get_birthdate_error_el()

        self.assertFalse(birthdate_success.is_displayed())
        self.assertTrue(birthdate_error.is_displayed())

    def test_birth_date_required_field(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.select_day('30')
        form.unfocus()

        birthdate_error = form.get_birthdate_error_el()
        self.assertTrue(birthdate_error.is_displayed())

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

    def test_sex_choices(self):
        self.register_page.open()
        form = self.register_page.get_form()

        buttons = form.get_sex_buttons()
        button1 = buttons.pop()
        button1.click()

        sex_choice_success = form.get_sex_success_el()
        self.assertTrue(sex_choice_success.is_displayed())

    def test_email_required_field(self):
        self.register_page.open()
        form = self.register_page.get_form()

        email_input = form.get_email_input()
        email_input.click()
        form.unfocus()

        email_error_el = form.get_email_error_el()
        self.assertTrue(email_error_el.is_displayed())

    def test_email_input(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.set_email(self.EMAIL)

        email_success_el = form.get_email_success_el()
        self.assertTrue(email_success_el.is_displayed())

    def test_password_notif_and_required_field(self):
        self.register_page.open()
        form = self.register_page.get_form()

        pass_input = form.get_pass_input()
        pass_input.click()

        pass_notif = form.get_pass_notif_el()
        self.assertTrue(pass_notif.is_displayed())

        form.unfocus()

        pass_error = form.get_pass_error_el()
        self.assertTrue(pass_error.is_displayed())

    def test_password_match(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.set_pass(self.PASSWORD)
        form.set_passverify(self.PASSWORD)
        form.unfocus()

        success_el = form.get_passverify_success_el()
        self.assertTrue(success_el.is_displayed())

    def test_password_not_match(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.set_pass(self.PASSWORD)
        form.set_passverify('BROKEN{}'.format(self.PASSWORD))
        form.unfocus()

        error_el = form.get_passverify_error_el()
        self.assertTrue(error_el.is_displayed())

    def test_password_strength_appears(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.set_pass(self.PASSWORD)
        strengths = form.get_pass_strength_list()

        appeared = False
        for el in strengths:
            if el.is_displayed():
                appeared = True
                break

        self.assertTrue(appeared)

    def test_phone_input_succeeds(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.clear_phone_input()
        form.set_phone(self.PHONE)

        success_el = form.get_phone_success_el()
        self.assertTrue(success_el.is_displayed())

    def test_extra_email(self):
        self.register_page.open()
        form = self.register_page.get_form()

        form.get_no_phone_link().click()

        extra_input = form.get_extra_email_input()
        self.assertTrue(extra_input.is_displayed())

        form.set_extra_email('kek')
        form.unfocus()

        error_el = form.get_extra_email_error_el()
        self.assertTrue(error_el.is_displayed())

        form.clear_extra_email()
        form.set_extra_email('kek@gmail.com')
        form.unfocus()

        success_el = form.get_extra_email_success_el()
        self.assertTrue(success_el.is_displayed())

    def tearDown(self):
        self.driver.quit()

