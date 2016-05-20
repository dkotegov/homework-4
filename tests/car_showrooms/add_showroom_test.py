# -*- coding: utf-8 -*-

import os
import unittest

import time
from random import randint

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.car_showrooms.pages.pages import ShowroomPage, Component


class AddShowroomForm(Component):
    TITLE = u'ДОБАВИТЬ АВТОСАЛОН'

    __OPEN_BUTTON = 'button.button.button_wide.button_type-1.js-show_form'
    __FORM_TITLE = 'div.box__title'
    __FIO_EDIT = 'manager_fio'
    __PHONE_EDIT = '//input[@name="manager_phone"]/..' \
                   '//input[@class="input__data__value js-phone__number js-phone__part"]'
    __EMAIL_EDIT = 'manager_email'
    __NAME_EDIT = 'name'
    __ADDRESS_EDIT = 'address_salon'
    __SHOWROOM_PHONE1_EDIT = '//input[@name="phone1"]/..' \
                             '//input[@class="input__data__value js-phone__number js-phone__part"]'
    __SHOWROOM_EMAIL_EDIT = 'email_salon'
    __SHOWROOM_SITE_EDIT = 'url_salon'
    __SUBMIT_BUTTON = '//span[@class="button__text" and text()="Отправить заявку"]'
    __SUBMIT_OK_TITLE = '//div[@class="box__title" and text()="Ваша заявка отправлена"]'

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

    def __get_phone_edit_element(self):
        return self.driver.find_element_by_xpath(self.__PHONE_EDIT)

    def set_phone(self, phone):
        phone_edit = self.__get_phone_edit_element()
        phone_edit.clear()
        phone_edit.send_keys(phone)

    def is_phone_valid(self):
        parent = self.__get_phone_edit_element().find_element_by_xpath('../../../../..')
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

    def set_address(self, address):
        address_edit = self.driver.find_element_by_name(self.__ADDRESS_EDIT)
        address_edit.clear()
        address_edit.send_keys(address)

    def __get_showroom_phone_edit_element(self):
        return self.driver.find_element_by_xpath(self.__SHOWROOM_PHONE1_EDIT)

    def set_showroom_phone(self, phone):
        phone_edit = self.__get_showroom_phone_edit_element()
        phone_edit.clear()
        phone_edit.send_keys(phone)

    def is_showroom_phone_valid(self):
        parent = self.__get_showroom_phone_edit_element().find_element_by_xpath('../../../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_showroom_email(self, email):
        email_edit = self.driver.find_element_by_name(self.__SHOWROOM_EMAIL_EDIT)
        email_edit.clear()
        email_edit.send_keys(email)

    def is_showroom_email_valid(self):
        parent = self.driver.find_element_by_name(self.__SHOWROOM_EMAIL_EDIT).find_element_by_xpath('../../..')
        return 'invalid' not in parent.get_attribute('class')

    def set_showroom_site(self, site):
        site_edit = self.driver.find_element_by_name(self.__SHOWROOM_SITE_EDIT)
        site_edit.clear()
        site_edit.send_keys(site)

    def is_showroom_site_valid(self):
        parent = self.driver.find_element_by_name(self.__SHOWROOM_SITE_EDIT).find_element_by_xpath('../../..')
        return 'invalid' not in parent.get_attribute('class')

    def submit(self):
        self.driver.find_element_by_xpath(self.__SUBMIT_BUTTON).click()

    def is_correct_submit(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.__SUBMIT_OK_TITLE))
        )
        return True


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

        add_showroom_form.set_phone(u'9091111111')
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

    # def test_invalid_email(self):
    #     invalid_emails = [u'test', u'13256', u' ', u'']
    #
    #     page = ShowroomPage(self.driver)
    #     page.open()
    #
    #     add_showroom_form = page.add_showroom_form
    #     add_showroom_form.open_form()
    #
    #     add_showroom_form.set_required_fields('test', '9091111111', invalid_emails[0], 'name', 'address', '9091111111')
    #     add_showroom_form.submit()
    #     self.assertFalse(add_showroom_form.is_email_valid(), 'email = "' + invalid_emails[0] + '"')
    #     for invalid_email in invalid_emails[1:]:
    #         add_showroom_form.set_email(invalid_email)
    #         add_showroom_form.submit()
    #         self.assertFalse(add_showroom_form.is_email_valid(), 'email = "' + invalid_email + '"')

    def test_valid_showroom_phone(self):
        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        add_showroom_form.set_showroom_phone(u'9091111111')
        add_showroom_form.submit()
        self.assertTrue(add_showroom_form.is_showroom_phone_valid())

    def test_invalid_showroom_phone(self):
        invalid_phones = [u'90912', u'test', u'909test909', u'test_test_', u'', u' ']

        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        for invalid_phone in invalid_phones:
            add_showroom_form.set_showroom_phone(invalid_phone)
            add_showroom_form.submit()
            self.assertFalse(add_showroom_form.is_showroom_phone_valid())

    def test_invalid_showroom_site(self):
        invalid_sites = [u'test', u' ']

        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        for invalid_site in invalid_sites:
            add_showroom_form.set_showroom_site(invalid_site)
            add_showroom_form.submit()
            self.assertFalse(add_showroom_form.is_showroom_site_valid())

    # def test_invalid_showroom_email(self):
    #     invalid_emails = [u'test', u'123456789', u' ']
    #
    #     page = ShowroomPage(self.driver)
    #     page.open()
    #
    #     add_showroom_form = page.add_showroom_form
    #     add_showroom_form.open_form()
    #
    #     add_showroom_form.set_required_fields('test', '9091111111', 'email@mail.ru', 'name', 'address', '9091111111')
    #     for invalid_email in invalid_emails[1:]:
    #         add_showroom_form.set_showroom_email(invalid_email)
    #         add_showroom_form.submit()
    #         self.assertFalse(add_showroom_form.is_showroom_email_valid(), 'email = "' + invalid_email + '"')

    # def test_correct_submit(self):
    #     page = ShowroomPage(self.driver)
    #     page.open()
    #
    #     add_showroom_form = page.add_showroom_form
    #     add_showroom_form.open_form()
    #
    #     add_showroom_form.set_required_fields(u'Иванов Иван Иванович', u'9091111111', u'test@mail.ru',
    #                                           u'Showroom' + unicode(randint(1, 100000)), u'Адрес', u'9091111111')
    #     add_showroom_form.submit()
    #     self.assertTrue(add_showroom_form.is_correct_submit())
