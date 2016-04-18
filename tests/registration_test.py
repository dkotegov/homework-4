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
        self.register_page.open()
        self.form = self.register_page.get_form()

    def test_first_name_element(self):
        self.assertTrue(self.form.check_exists_by_xpath(self.form.FIRST_NAME_INPUT))
        self.driver.find_element_by_xpath(self.form.FIRST_NAME_INPUT).click()

        notification = self.form.get_first_name_notif()
        self.assertTrue(notification.is_displayed())

        self.form.unfocus()

        error = self.form.get_first_name_error()
        self.assertTrue(error.is_displayed())

    def test_last_name_element(self):
        self.assertTrue(self.form.check_exists_by_xpath(self.form.LAST_NAME_INPUT))
        self.driver.find_element_by_xpath(self.form.LAST_NAME_INPUT).click()

        notification = self.form.get_last_name_notif()
        self.assertTrue(notification.is_displayed())

        self.form.unfocus()

        error = self.form.get_last_name_error()
        self.assertTrue(error.is_displayed())

    def test_birth_date_right_date(self):
        self.form.select_day('11')
        self.form.select_month('Март')
        self.form.select_year('1999')
        self.form.unfocus()

        birthdate_success = self.form.get_birthdate_success_el()
        self.assertTrue(birthdate_success.is_displayed())

    def test_birth_date_wrong_date(self):
        self.form.select_day('30')
        self.form.select_month('Февраль')
        self.form.select_year('1999')
        self.form.unfocus()

        birthdate_success = self.form.get_birthdate_success_el()
        birthdate_error = self.form.get_birthdate_error_el()
        error_text = self.form.get_birthdate_error_text()

        self.assertFalse(birthdate_success.is_displayed())
        self.assertTrue(birthdate_error.is_displayed())
        self.assertEqual(error_text, u'Неверная дата')

    def test_birth_date_required_field(self):
        self.form.select_day('30')
        self.form.unfocus()

        birthdate_error = self.form.get_birthdate_error_el()
        error_text = self.form.get_birthdate_error_text()

        self.assertTrue(birthdate_error.is_displayed())
        self.assertEqual(error_text, u'Укажите дату рождения полностью')

    def test_city_only_from_list(self):
        self.form.set_city(u'Гейсити')
        self.form.unfocus()

        city_error_el = self.form.get_city_error_el()
        self.assertTrue(city_error_el.is_displayed())

    def test_city_autocompletion(self):
        self.form.set_city(u'Москва')
        self.assertTrue(self.form.check_exists_by_xpath(self.form.CITY_HELPER))

        city = self.form.get_city_auto_variant()
        city.click()

        city_success_el = self.form.get_city_success_el()
        self.assertTrue(city_success_el.is_displayed())

    def test_sex_choices(self):
        buttons = self.form.get_sex_buttons()
        button1 = buttons.pop()
        button1.click()

        sex_choice_success = self.form.get_sex_success_el()
        self.assertTrue(sex_choice_success.is_displayed())

    def test_email_required_field(self):
        email_input = self.form.get_email_input()
        email_input.click()
        self.form.unfocus()

        email_error_el = self.form.get_email_error_el()
        self.assertTrue(email_error_el.is_displayed())

    def test_email_input(self):
        self.form.set_email(self.EMAIL)

        email_success_el = self.form.get_email_success_el()
        self.assertTrue(email_success_el.is_displayed())

    def test_password_notif_and_required_field(self):
        pass_input = self.form.get_pass_input()
        pass_input.click()

        pass_notif = self.form.get_pass_notif_el()
        self.assertTrue(pass_notif.is_displayed())

        self.form.unfocus()

        pass_error = self.form.get_pass_error_el()
        self.assertTrue(pass_error.is_displayed())

    def test_password_match(self):
        self.form.set_pass(self.PASSWORD)
        self.form.set_passverify(self.PASSWORD)
        self.form.unfocus()

        success_el = self.form.get_passverify_success_el()
        self.assertTrue(success_el.is_displayed())

    def test_password_not_match(self):

        self.form.set_pass(self.PASSWORD)
        self.form.set_passverify('BROKEN{}'.format(self.PASSWORD))
        self.form.unfocus()

        error_el = self.form.get_passverify_error_el()
        self.assertTrue(error_el.is_displayed())

    def test_password_strength_appears(self):
        self.form.set_pass(self.PASSWORD)
        strengths = self.form.get_pass_strength_list()

        appeared = False
        for el in strengths:
            if el.is_displayed():
                appeared = True
                break

        self.assertTrue(appeared)

    def test_phone_input_succeeds(self):
        self.form.clear_phone_input()
        self.form.set_phone(self.PHONE)

        success_el = self.form.get_phone_success_el()
        self.assertTrue(success_el.is_displayed())

    def test_extra_email(self):
        self.form.get_no_phone_link().click()

        extra_input = self.form.get_extra_email_input()
        self.assertTrue(extra_input.is_displayed())

        self.form.set_extra_email('kek')
        self.form.unfocus()

        error_el = self.form.get_extra_email_error_el()
        self.assertTrue(error_el.is_displayed())

        self.form.clear_extra_email()
        self.form.set_extra_email('test@sashqua.com')
        self.form.unfocus()

        success_el = self.form.get_extra_email_success_el()
        self.assertTrue(success_el.is_displayed())

    def tearDown(self):
        self.driver.quit()

