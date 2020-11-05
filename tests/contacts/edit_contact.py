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

        self.sergey_contact = {
            "firstname": "Сергей".decode('utf-8'),
            "lastname": "Петренко".decode('utf-8'),
            "nick": "sergey",
            "company": "KTS",
            "email": ["s.petrenko@kts.studio"],
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Алексндр Апришко".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
        }

        self.data_for_edit = {
            "firstname": "Дмитрий измененный".decode('utf-8'),
            "email": ["test_edit@mail.ru"]
        }

        self.page.create_contact(**self.dmitry_contact)
        self.invalid_emails = [
            "это_имейл@mail.ru".decode('utf-8'),
            "email@email",
            "email.ru",
        ]

    def tearDown(self):
        self.page.open()

        self.page.delete_all_contacts()
        self.driver.quit()

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

        self.assertTrue(self.page.has_error())

    def test_invalid_email(self):
        """
         Ошибка при вводе невалидной почты
        """
        self.page.edit_contact(email=[self.invalid_emails[0]])
        self.assertTrue(self.page.has_validation_errors())

        for email in self.invalid_emails[1:]:
            self.page.fill_form_and_save(email=[email])
            self.assertTrue(self.page.has_validation_errors())

    def test_edit_ok(self):
        """
        Проврека успешного редактирования контакта
        """
        self.page.edit_contact(**self.data_for_edit)
        self.page.open()
        self.assertTrue(self.page.contact_exists(self.data_for_edit['email'][0]))

    def test_only_email(self):
        """
        Оставить заполненным только email
        """

        only_email = {
            "firstname": '',
            "lastname": '',
            "nick": '',
            "company": '',
            "email": ['new@email.com'],
            "phone": '',
            "comment": '',
            "job_title": '',
            "boss": '',
            "address": '',
        }
        self.page.edit_contact(**only_email)

        self.assertFalse(self.page.has_error())

    def test_edit_latin(self):
        """
        Проверка редактирования контакта только с латинскими символами в имени
        """
        only_email = {
            "nick": "some nick"
        }

        self.page.edit_contact(**only_email)
        self.assertFalse(self.page.has_any_error())

    def test_unicode(self):
        """
        Проверка редактирования контакта с нетипичными unicode символами
        """
        only_nick = {
            "nick": "ђћ∆".decode("utf-8")
        }

        self.page.edit_contact(**only_nick)
        self.assertFalse(self.page.has_any_error())

    def test_same_contacts(self):
        """
        Исправление контакта на уже существующий
        """
        self.page.open()
        self.page.create_contact(**self.sergey_contact)
        self.page.edit_contact(**self.dmitry_contact)
        self.assertFalse(self.page.has_any_error())
