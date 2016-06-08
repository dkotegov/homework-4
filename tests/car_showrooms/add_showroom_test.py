# -*- coding: utf-8 -*-

import os
import time
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.car_showrooms.pages.pages import ShowroomPage


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

    def test_invalid_email(self):
        invalid_emails = [u'test', u'13256', u' ', u'']

        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        add_showroom_form.set_required_fields('test', '9091111111', invalid_emails[0], 'name',
                                              'address', '9091111111', 'http://site.ru')
        add_showroom_form.submit()
        self.assertTrue(add_showroom_form.is_email_invalid(), 'email = "' + invalid_emails[0] + '"')
        for invalid_email in invalid_emails[1:]:
            add_showroom_form.set_email(invalid_email)
            add_showroom_form.submit()
            self.assertTrue(add_showroom_form.is_email_invalid(), 'email = "' + invalid_email + '"')

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

    def test_invalid_showroom_email(self):
        invalid_emails = [u'test', u'123456789', u' ']

        page = ShowroomPage(self.driver)
        page.open()

        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        add_showroom_form.set_required_fields('test', '9091111111', 'email@mail.ru', 'name',
                                              'address', '9091111111', 'http://site.ru')
        for invalid_email in invalid_emails:
            add_showroom_form.set_showroom_email(invalid_email)
            add_showroom_form.submit()
            self.assertTrue(add_showroom_form.is_showroom_email_invalid(), 'email = "' + invalid_email + '"')

    def test_correct_submit(self):
        page = ShowroomPage(self.driver)
        page.open()
    
        add_showroom_form = page.add_showroom_form
        add_showroom_form.open_form()

        current_time_in_millis = int(round(time.time() * 1000))
        add_showroom_form.set_required_fields(u'Иванов Иван Иванович', u'9091111111',
                                              u'test' + unicode(current_time_in_millis) + u'@mail.ru',
                                              u'Showroom' + unicode(current_time_in_millis),
                                              u'Адрес', u'9091111111', 'http://site.ru')
        add_showroom_form.submit()
        self.assertTrue(add_showroom_form.is_correct_submit())
