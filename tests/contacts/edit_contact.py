# coding=utf-8
import time
import unittest

from selenium.webdriver.common.keys import Keys

from pages.contact_edit_page import ContactEditPage
from setup.default_setup import default_setup


class EditContactTest(unittest.TestCase):
    def setUp(self):
        default_setup(self)

        self.page = ContactEditPage(self.driver)

        self.page.open()

        self.dmitry_contact = {
            "firstname": "Дмитрий".decode('utf-8'),
            "lastname": "Болдин".decode('utf-8'),
            "nick": "stalin",
            "company": "Mail.ru Group",
            "email": ["d.boldin@corp.mail.ru"],
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Иван Чашкин".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
        }

        self.page.create_contact(**self.dmitry_contact)

    def test_edit_empty(self):
        """
            Ошибка при заполнении контакта пустыми полями
        """

        empty_data = {
            "firstname": '',
            "lastname": '',
            "nick": '',
            "company": '',
            "email": [''],
            "phone": '',
            "comment": '',
            "job_title": '',
            "boss": '',
            "address": '',
        }
        self.page.edit_contact(**empty_data)
        time.sleep(100)

        self.assertTrue(self.page.has_error())
