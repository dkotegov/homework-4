# -*- coding: utf-8 -*-

import os
import unittest

import time
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.car_showrooms.pages import ShowroomPage, Component


class AddShowroomForm(Component):
    TITLE = u'ДОБАВИТЬ АВТОСАЛОН'

    __OPEN_BUTTON = 'button.button.button_wide.button_type-1.js-show_form'
    __FORM_TITLE = 'div.box__title'
    __FIO_EDIT = 'manager_fio'
    __PHONE_EDIT = 'input.input__data__value.js-phone__number.js-phone__part'
    __EMAIL_EDIT = 'manager_email'
    __NAME_EDIT = 'name'
    __ADDRESS_EDIT = 'address_salon'
    __SHOWROOM_PHONE = '//div[@class="form__fieldset__item form__fieldset__item_phone clear js-module js-field_cont" ' \
                       'and @data-module="PhoneInput"]'
    __SUBMIT_BUTTON = '//span[@class="button__text" and text()="Отправить заявку"]'

    def open_form(self):
        self.driver.find_element_by_css_selector(self.__OPEN_BUTTON).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.__FORM_TITLE))
        )

    def set_required_fields(self, fio, phone, email, name, address, showroom_phone):
        self.set_fio(fio)
        self.set_phone(phone)
        self.set_email(email)
        self.set_name(name)
        self.set_address(address)
        self.set_showroom_phone(showroom_phone)

    def get_title(self):
        return self.driver.find_element_by_css_selector(self.__FORM_TITLE).text

    def set_fio(self, fio):
        fio_edit = self.driver.find_element_by_name(self.__FIO_EDIT)
        fio_edit.clear()
        fio_edit.send_keys(fio)

    def set_phone(self, phone):
        phone_edit = self.driver.find_element_by_css_selector(self.__PHONE_EDIT)
        phone_edit.clear()
        phone_edit.send_keys(phone)

    def is_phone_valid(self):
        parent = self.driver.find_element_by_css_selector(self.__PHONE_EDIT).find_element_by_xpath('../../../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_email(self, email):
        email_edit = self.driver.find_element_by_name(self.__EMAIL_EDIT)
        email_edit.clear()
        email_edit.send_keys(email)

    def is_email_valid(self):
        parent = self.driver.find_element_by_name(self.__EMAIL_EDIT).find_element_by_xpath('../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_name(self, name):
        name_edit = self.driver.find_element_by_name(self.__NAME_EDIT)
        name_edit.clear()
        name_edit.send_keys(name)

    def is_name_valid(self):
        return

    def set_address(self, address):
        address_edit = self.driver.find_element_by_name(self.__ADDRESS_EDIT)
        address_edit.clear()
        address_edit.send_keys(address)

    def is_address_valid(self):
        return

    def set_showroom_phone(self, phone):
        phone_parent = self.driver.find_element_by_xpath(self.__SHOWROOM_PHONE)
        phone_edit = phone_parent.find_element_by_css_selector(self.__PHONE_EDIT)
        phone_edit.clear()
        phone_edit.send_keys(phone)

    def is_showroom_phone_valid(self):
        return

    def submit(self):
        self.driver.find_element_by_xpath(self.__SUBMIT_BUTTON).click()


class AddShowroomFormTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_open(self):
        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        self.assertEqual(add_showroom_form.get_title(), add_showroom_form.TITLE)

    def test_valid_phone(self):
        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        add_showroom_form.set_phone(u'1111111111')
        add_showroom_form.submit()
        self.assertTrue(add_showroom_form.is_phone_valid())

    def test_invalid_phone(self):
        invalid_phones = [u'90912', u'test', u'909test909', u'test_test_', u'', u' ']

        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        for invalid_phone in invalid_phones:
            add_showroom_form.set_phone(invalid_phone)
            add_showroom_form.submit()
            self.assertFalse(add_showroom_form.is_phone_valid())

    def test_invalid_email(self):
        invalid_emails = [u'test', u'test@test', u'test@test.ru@test', u'', u' ']

        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        add_showroom_form.set_required_fields('test', '9091111111', invalid_emails[0], 'name', 'address', '9091111111')
        for invalid_email in invalid_emails[1:]:
            add_showroom_form.set_email(invalid_email)
            add_showroom_form.submit()

            time.sleep(2)
            self.assertFalse(add_showroom_form.is_email_valid())
